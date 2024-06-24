import osmnx as ox
import networkx as nx
import geopandas as gpd
import streamlit as st
import folium
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim

# Configuración de la página
st.set_page_config(page_title="Buscador", page_icon="🛤️")

# Título de la página
st.markdown("# Ruta más rápida al reciclaje")
st.sidebar.header("Búsqueda")
st.write("""Esta página te ayuda a encontrar el contenedor más cercano de València. Para ello, debes introducir tu ubicación actual. Intenta
         que sea lo más precisa posible para conseguir mejores resultados. Estos pueden tardar varios minutos.""")

# Coordenada de origen predeterminada
coordenada_origen_default = (39.469, -0.376)  # Latitud, Longitud

# Verifica si st.session_state ya tiene una ruta almacenada
if 'ruta_optima' not in st.session_state:
    st.session_state['ruta_optima'] = None
    st.session_state['distancia_minima'] = None
    st.session_state['contenedor_cercano'] = None
    st.session_state['coordenada_origen'] = coordenada_origen_default

# Obtener la dirección del usuario
user_address = st.text_input("Introduce tu dirección en Valencia (ej. Pl. de l'Ajuntament, Ciutat Vella, 46002 València, Valencia):")

# Si el usuario ha introducido una dirección nueva
if user_address:
    geolocator = Nominatim(user_agent="recycling_app")
    location = geolocator.geocode(user_address)
    if location:
        if "Valencia" not in location.address:
            st.warning("La dirección proporcionada no está en Valencia. Usando la ubicación por defecto (Ayuntamiento de València).")
            st.session_state['coordenada_origen'] = coordenada_origen_default
        else:
            st.success(f"Ubicación encontrada: {location.address}")
            st.session_state['coordenada_origen'] = (location.latitude, location.longitude)
    else:
        st.warning("Si dejas este espacio en blanco, se utilizará la ubicación por defecto (Ayuntamiento de València).")
        st.session_state['coordenada_origen'] = coordenada_origen_default
else:
    st.write("Si no has introducido una dirección, se utilizará la ubicación por defecto.")

# Tipos de contenedores disponibles
tipos_contenedores = {
    'ACEITE',
    'ENVASES LIGEROS',
    'ORGANICO',
    'PAPEL / CARTON',
    'PAPELERAS',
    'PILAS',
    'RESTO',
    'ROPA',
    'VIDRIO'
}

# Widget de selección del tipo de contenedor con confirmación
tipo_seleccionado = st.selectbox("Selecciona el tipo de contenedor", list(tipos_contenedores))
confirmado = st.checkbox("Confirmar selección de tipo de contenedor")

if not confirmado:
    st.warning("Por favor, confirma la selección del tipo de contenedor para proceder.")
    st.stop()

# Cargar los datos
try:
    contenedores_gdf = gpd.read_file('./processed_data/reciclatge.geojson')
    graph = ox.load_graphml(filepath="./processed_data/valencia_street_graph.graphml")
except FileNotFoundError as e:
    st.error(f"Error al cargar los archivos de datos: {e}")
    st.stop()
except Exception as e:
    st.error(f"Error inesperado al cargar los archivos de datos: {e}")
    st.stop()

# Filtrar el DataFrame por el tipo de contenedor seleccionado
contenedores_gdf = contenedores_gdf[contenedores_gdf['tipo'] == tipo_seleccionado]

# Asegurar que los datos estén en EPSG:4326
contenedores_gdf = contenedores_gdf.to_crs("EPSG:4326")

# Seleccionar aleatoriamente el 10% de las filas
if len(contenedores_gdf) > 0:
    contenedores_sampled = contenedores_gdf.sample(frac=0.1, random_state=1)
else:
    st.warning("No se encontraron filas para el tipo de contenedor seleccionado.")

# Verificar si el grafo contiene nodos
nodes, edges = ox.graph_to_gdfs(graph)
if len(nodes) == 0:
    st.error("El grafo cargado no contiene nodos.")
    st.stop()

# Función para encontrar el nodo más cercano
def find_nearest_node(graph, point):
    min_dist = float('inf')
    nearest_node = None
    for node in graph.nodes():
        dist = ox.distance.great_circle_vec(graph.nodes[node]['y'], graph.nodes[node]['x'], point[0], point[1])
        if dist < min_dist:
            min_dist = dist
            nearest_node = node
    return nearest_node

# Solo recalcula la ruta si se ha proporcionado una nueva dirección
if user_address:
    try:
        origen_node = ox.distance.nearest_nodes(graph, X=st.session_state['coordenada_origen'][1], Y=st.session_state['coordenada_origen'][0])
        st.write("Búsqueda iniciada. Este proceso puede tardar unos minutos.")
    except ImportError as e:
        st.error(f"Error al encontrar el nodo más cercano: {e}. Asegúrate de tener scikit-learn instalado.")
        st.stop()
    except Exception as e:
        st.error(f"Error inesperado al encontrar el nodo más cercano: {e}")
        st.stop()

    # Inicializar variables para encontrar la ruta óptima
    distancia_minima = float("inf")
    ruta_optima = None
    contenedor_cercano = None

    # Barra de progreso
    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()

    # Calcular la ruta más corta
    for idx, contenedor in enumerate(contenedores_sampled.iterrows()):
        try:
            destino_geom = contenedor[1]['geometry']
            destino_x, destino_y = destino_geom.x, destino_geom.y

            # Encontrar el nodo más cercano en la red de calles al punto de destino
            destino_node = find_nearest_node(graph, (destino_y, destino_x))

            # Calcular la ruta más corta usando NetworkX
            ruta = nx.shortest_path(graph, origen_node, destino_node, weight='length')
            distancia_ruta = nx.shortest_path_length(graph, origen_node, destino_node, weight='length')

            if distancia_ruta < distancia_minima:
                distancia_minima = distancia_ruta
                ruta_optima = ruta
                contenedor_cercano = destino_geom

            # Actualizar la barra de progreso
            progress = int((idx + 1) / len(contenedores_sampled) * 100)
            progress_bar.progress(progress)
            status_text.text(f"Explorando rutas... {progress}% completado")

        except nx.NetworkXNoPath:
            st.warning(f"No se encontró una ruta hacia el contenedor en índice {idx}.")
        except Exception as e:
            st.error(f"Error al calcular la ruta hacia el contenedor en índice {idx}: {e}")

    # Almacenar la ruta calculada en st.session_state
    st.session_state['ruta_optima'] = ruta_optima
    st.session_state['distancia_minima'] = distancia_minima
    st.session_state['contenedor_cercano'] = contenedor_cercano

# Visualizar la ruta óptima si se encontró
if st.session_state['ruta_optima']:
    # Crear un mapa centrado en la coordenada de origen
    mapa = folium.Map(location=[st.session_state['coordenada_origen'][0], st.session_state['coordenada_origen'][1]], zoom_start=14)

    # Añadir el marcador del punto de origen
    folium.Marker(
        location=[st.session_state['coordenada_origen'][0], st.session_state['coordenada_origen'][1]],
        popup='Origen',
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(mapa)

    # Añadir el marcador del contenedor cercano
    if st.session_state['contenedor_cercano'] is not None:
        folium.Marker(
            location=[st.session_state['contenedor_cercano'].y, st.session_state['contenedor_cercano'].x],
            popup='Contenedor Cercano',
            icon=folium.Icon(color='green', icon='info-sign')
        ).add_to(mapa)

    # Añadir la ruta óptima
    ruta_coords = [(graph.nodes[node]['y'], graph.nodes[node]['x']) for node in st.session_state['ruta_optima']]
    folium.PolyLine(ruta_coords, color='red', weight=5, opacity=0.7).add_to(mapa)

    # Mostrar el mapa
    st.markdown("### Mapa de la ruta óptima")
    st.markdown(f"Distancia aproximada: {st.session_state['distancia_minima']:.2f} metros.")
    st_folium(mapa)

st.button("Volver a cargar")
