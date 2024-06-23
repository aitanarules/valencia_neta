from streamlit_folium import folium_static
import streamlit as st
import geopandas as gpd
import folium
import streamlit.components.v1 as components


st.set_page_config(page_title="Mapa", page_icon="🗺️")
st.markdown("# Mapa de ubicaciones")
st.sidebar.header("Mapa")
st.write("""Este mapa de València muestra las ubicaciones de los diferentes contenedores y papeleras repartidos por la ciudad. Los datos han sido
         obtenidos desde el [Portal de dades obertes de València](https://valencia.opendatasoft.com/pages/home/)""")

html_file_path = "./processed_data/mapa_contenedores_valencia.html"

try:
    with open(html_file_path, 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()
        components.html(html_content, height=600, scrolling=True)
except FileNotFoundError:
    st.error("No se encuentra la página.")

# st.markdown("# Mapa de ubicaciones interactivo")
# st.write("""Este mapa es equivalente al que se muestra en la franaja superior y, adicionalmente, puedes filtrar los contenedores
#          para observar solo los de un tipo. Puede tardar varios minutos en cargar. """)


# html_file_path = "./processed_data/selecciona_contenedores.html"

# try:
#     with open(html_file_path, 'r', encoding='utf-8') as html_file:
#         html_content = html_file.read()
#         components.html(html_content, height=600, scrolling=True)
# except FileNotFoundError:
#     st.error("No se encuentra la página.")