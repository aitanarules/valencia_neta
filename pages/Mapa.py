import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Mapa", page_icon="📈")

st.markdown("# Mapa d'ubicacions")
st.sidebar.header("Mapa")
st.write("Aquest mapa de València mostra les ubicacions dels diferents contenedors i papereres distribuïdes a València.")

# Leer el archivo HTML y cargarlo en la aplicación de Streamlit
html_file_path = '../mapa_contenedores_valencia_2.html'

# Asegurarse de que el archivo HTML exista
try:
    with open(html_file_path, 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()
        components.html(html_content, height=600, scrolling=True)
except FileNotFoundError:
    st.error("El archivo HTML del mapa no se encuentra. Por favor, verifica la ruta y asegúrate de que el archivo haya sido generado correctamente.")

st.button("Re-run")
