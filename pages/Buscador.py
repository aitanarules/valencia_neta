import osmnx as ox
import networkx as nx
import geopandas as gpd
from shapely.geometry import Point

import streamlit as st
from streamlit_folium import st_folium
import folium

# Configuración de la página
st.set_page_config(page_title="Ruta al Contenedor", page_icon="🛤️")

# Título de la página
st.markdown("# Ruta al Contenedor más Cercano")

# Coordenada de origen (por ejemplo, centro de Valencia)
coordenada_origen = (39.469, -0.376)  # Latitud, Longitud

# Cargar los datos
try:
    contenedores_gdf = gpd.read_file('./processed_data/reciclatge.geojson')
    graph = ox.load_graphml(filepath="./processed_data/valencia_street_graph.graphml")
except FileNotFoundError:
    st.error("Error: No se encontraron los archivos de datos necesarios. Por favor, verifica las rutas y vuelve a intentarlo.")
    st.stop()

# Encontrar el nodo más cercano en la red de calles al punto de origen
try:
    origen_node = ox.distance.nearest_nodes(graph, X=coordenada_origen[1], Y=coordenada_origen[0])
except ImportError as e:
    st.error(f"Error al encontrar el nodo más cercano: {e}")
    st.stop()
except Exception as e:
    st.error(f"Error inesperado al encontrar el nodo más cercano: {e}")
    st.stop()

# Inicializar variables para encontrar la ruta óptima
distancia_minima = float("inf")
ruta_optima = None
contenedor_cercano = None

# Calcular la ruta más corta
for idx, contenedor in contenedores_gdf.iterrows():
    try:
        destino_geom = contenedor['geometry']

        # Convertir a WGS84 si es necesario
        if contenedores_gdf.crs != "EPSG:4326":
            destino_geom = destino_geom.to_crs("EPSG:4326")

        destino_x, destino_y = destino_geom.x, destino_geom.y

        # Encontrar el nodo más cercano en la red de calles al punto de destino
        destino_node = ox.distance.nearest_nodes(graph, X=destino_x, Y=destino_y)

        # Calcular la ruta más corta usando NetworkX
        ruta = nx.shortest_path(graph, origen_node, destino_node, weight='length')
        distancia_ruta = nx.shortest_path_length(graph, origen_node, destino_node, weight='length')

        if distancia_ruta < distancia_minima:
            distancia_minima = distancia_ruta
            ruta_optima = ruta
            contenedor_cercano = destino_geom

    except nx.NetworkXNoPath:
        st.warning(f"No se encontró una ruta hacia el contenedor en índice {idx}.")
    except Exception as e:
        st.error(f"Error al calcular la ruta hacia el contenedor en índice {idx}: {e}")

# Visualizar la ruta óptima si se encontró
if ruta_optima:
    st.markdown("### Ruta óptima encontrada")
    st.write(f"Distancia aproximada: {distancia_minima:.2f} metros.")

    # Crear un mapa centrado en la coordenada de origen
    mapa = folium.Map(location=[coordenada_origen[0], coordenada_origen[1]], zoom_start=14)

    # Añadir el marcador del punto de origen
    folium.Marker(
        location=[coordenada_origen[0], coordenada_origen[1]],
        popup='Origen',
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(mapa)

    # Añadir el marcador del contenedor cercano
    if contenedor_cercano is not None:
        folium.Marker(
            location=[contenedor_cercano.y, contenedor_cercano.x],
            popup='Contenedor Cercano',
            icon=folium.Icon(color='green', icon='info-sign')
        ).add_to(mapa)

    # Añadir la ruta óptima
    ruta_coords = [(graph.nodes[node]['y'], graph.nodes[node]['x']) for node in ruta_optima]
    folium.PolyLine(ruta_coords, color='red', weight=5, opacity=0.7).add_to(mapa)

    # Mostrar el mapa en Streamlit
    st_folium(mapa, width=700, height=500)

else:
    st.error("No se encontró una ruta óptima hacia ningún contenedor cercano.")
