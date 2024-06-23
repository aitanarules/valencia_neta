import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(
    page_title="ValènciaNetApp",
    page_icon="♻️",
)

# Título de la página
st.write("# Benvingut/da a València Neta! 👋")

# Mensaje en la barra lateral
st.sidebar.success("Selecciona una pàgina.")

# Información inicial
st.markdown(
    """
    Bienvenido/a a València Neta, tu guía para un reciclaje eficaz. A continuación, te mostramos los diferentes tipos de contenedores de reciclaje y ejemplos de lo que puedes depositar en cada uno.
    """
)

# Información adicional y enlaces
st.markdown(
    """
    ### Quieres saber más?
    - [Sitio oficial de Streamlit](https://streamlit.io)
    - [Documentación de Streamlit](https://docs.streamlit.io)
    - [Foros de la comunidad](https://discuss.streamlit.io)
    """
)
