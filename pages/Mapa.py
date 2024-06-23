import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Mapa", page_icon="📈")

st.markdown("# Mapa d'ubicacions")
st.sidebar.header("Mapa")
st.write("""Aquest mapa de València mostra les ubicacions dels diferents contenedors i papereres distribuïdes a València. Les dades s'han obtingut 
         del [`Portal de dades obertes de València`](https://valencia.opendatasoft.com/pages/home/) """)

html_file_path = "../mapa_contenedores_valencia_2.html"

try:
    with open(html_file_path, 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()
        components.html(html_content, height=600, scrolling=True)
except FileNotFoundError:
    st.error("Hi ha un problema: no es troba l'HTML del mapa. Revisa la ruta.")

st.button("Re-run")
