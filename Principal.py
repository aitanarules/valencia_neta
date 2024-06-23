import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(
    page_title="ValènciaNetApp",
    page_icon="♻️",
)

# Título de la página
st.write("# Bienvenido/a a València Neta! 👋")

# Mensaje en la barra lateral
st.sidebar.success("Selecciona una página.")

# Información inicial
st.markdown(
    """
    Esta página es una guía para un reciclaje eficaz. A continuación, te mostramos los diferentes tipos de contenedores de reciclaje y ejemplos de lo que puedes depositar en cada uno.
    """
)

# Información adicional y enlaces
st.markdown(
    """
    ### ¿Quieres saber más?
    En la izquierda podrás encontrar diferentes páginas con las que podrás:
    - Conocer qué residuos deben ir en cada contenedor [Ir a Aprende]()
    - Visualizar los contenedores que hay en València [Ir a Mapa](https://valencianeta-csow8jrrvjysugbmymzp44.streamlit.app/Mapa)
    - Encontrar la ruta más rápida para acceder a uno de ellos [Ir a Buscador](https://valencianeta-csow8jrrvjysugbmymzp44.streamlit.app/Buscador)
    """
)
