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

# Datos de los contenedores
contenedores = {
    'Aceite': ('#32CD32', 'oil-can', 'aceite.jpg', 'aceite.jpg'),  # green
    'Envases ligeros': ('#FFA500', 'recycle', 'envases.jpg', 'botellas-plastico.jpg'),  # orange
    'Organico': ('#90EE90', 'leaf', 'organico.jpg', 'residuos-organicos.jpg'),  # lightgreen
    'Papel / carton': ('#1E90FF', 'file-text', 'papel-carton.jpg', 'papel.jpg'),  # blue
    'Papeleras': ('#800080', 'trash', 'papelera.jpg', 'papelera.jpg'),  # purple
    'Pilas': ('#808080', 'battery-quarter', 'pilas.jpg', 'pilas.jpg'),  # gray
    'Resto': ('#8B0000', 'globe', 'resto.jpg', 'resto.jpg'),  # darkred
    'Ropa': ('#FFC0CB', 'tshirt', 'ropa.jpg', 'ropa.jpg'),  # pink
    'Vidrio': ('#32CD32', 'glass-martini', 'vidrio.jpg', 'vidrio.jpg'),  # green
}

# Función para mostrar el carrusel
def mostrar_carrusel():
    st.write("### Carrusel de Contenedores de Reciclaje")
    for contenedor, (color, icono, ejemplo_img, contenedor_img) in contenedores.items():
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(f'images/{contenedor_img}', caption=f"Contenedor de {contenedor}", use_column_width=True)
        with col2:
            st.write(f"## {contenedor}")
            st.markdown(f"<i class='fa fa-{icono}' style='font-size:48px;color:{color}'></i>", unsafe_allow_html=True)
            st.write("### Ejemplos de objetos:")
            st.image(f'images/{ejemplo_img}', caption=f"Ejemplos para {contenedor}", use_column_width=True)

# Llamar a la función para mostrar el carrusel
mostrar_carrusel()

# Información adicional y enlaces
st.markdown(
    """
    ### Quieres saber más?
    - [Sitio oficial de Streamlit](https://streamlit.io)
    - [Documentación de Streamlit](https://docs.streamlit.io)
    - [Foros de la comunidad](https://discuss.streamlit.io)
    """
)
