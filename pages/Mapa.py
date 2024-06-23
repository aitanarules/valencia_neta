from streamlit_folium import folium_static
import streamlit as st
import geopandas as gpd
import folium

st.set_page_config(page_title="Mapa", page_icon="🗺️")
st.markdown("# Mapa de ubicaciones")
st.sidebar.header("Mapa")
st.write("""Este mapa de València muestra las ubicaciones de los diferentes contenedores y papeleras repartidos por la ciudad. Los datos han sido
         obtenidos desde el [Portal de dades obertes de València](https://valencia.opendatasoft.com/pages/home/)""")

# Leer el archivo GeoJSON
gdf = gpd.read_file('./processed_data/reciclatge.geojson')

# Crear un mapa centrado en Valencia
valencia_coords = [39.4699, -0.3763]
mapa = folium.Map(location=valencia_coords, zoom_start=13)

# Diccionario para colores e iconos por tipo
iconos = {
    'Aceite': ('green', 'oil-can'),
    'Envases ligeros': ('orange', 'recycle'),
    'Organico': ('lightgreen', 'leaf'),
    'Papel / carton': ('blue', 'file-text'),
    'Papeleras': ('purple', 'trash'),
    'Pilas': ('gray', 'battery-quarter'),
    'Resto': ('darkred', 'globe'),
    'Ropa': ('pink', 'tshirt'),
    'Vidrio': ('green', 'glass-martini')
}

# Añadir contenedores al mapa
for idx, row in gdf.iterrows():
    tipo = row['tipo'].capitalize()
    location = [row['lat'], row['long']]
    
    # Obtener el color y el icono correspondiente al tipo
    if tipo in iconos:
        color, icon = iconos[tipo]
    else:
        color, icon = 'gray', 'info-sign'
    
    folium.Marker(
        location=location,
        popup=f"Tipo: {tipo}",
        icon=folium.Icon(color=color, icon=icon, prefix='fa')
    ).add_to(mapa)

# Añadir el control de capas al mapa
folium.LayerControl(collapsed=False).add_to(mapa)

# Mostrar el mapa en Streamlit
folium_static(mapa)
