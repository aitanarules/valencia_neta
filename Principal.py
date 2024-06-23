import streamlit as st
from PIL import Image
import os

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

# Función para cargar imágenes con verificación de existencia
def load_image(image_path):
    if os.path.exists(image_path):
        return Image.open(image_path)
    else:
        st.error(f"No se encuentra la imagen en la ruta: {image_path}")
        return None

# Crear dos columnas
col1, col2 = st.columns(2)

# Contenedor amarillo con carrusel de imágenes en la primera columna
with col1:
    st.markdown("## Contenedor amarillo")
    images_yellow = [
        {"file": "images/contenedor_amarillo_1.jpg", "caption": "Botellas de plástico"},
        {"file": "images/contenedor_amarillo_2.jpg", "caption": "Latas de bebida"},
        {"file": "images/contenedor_amarillo_3.jpg", "caption": "Envases de brik"}
    ]

    selected_image_yellow = st.select_slider(
        "Selecciona un tipo de residuo para el contenedor amarillo",
        options=[img['caption'] for img in images_yellow]
    )

    image_file_yellow = next(img['file'] for img in images_yellow if img['caption'] == selected_image_yellow)
    image_yellow = load_image(image_file_yellow)
    if image_yellow:
        st.image(image_yellow, caption=f"Contenedor amarillo: {selected_image_yellow}")

# Contenedor azul con carrusel de imágenes en la segunda columna
with col2:
    st.markdown("## Contenedor azul")
    images_blue = [
        {"file": "images/contenedor_azul_1.jpg", "caption": "Papeles y revistas"},
        {"file": "images/contenedor_azul_2.jpg", "caption": "Cajas de cartón"}
    ]

    selected_image_blue = st.select_slider(
        "Selecciona un tipo de residuo para el contenedor azul",
        options=[img['caption'] for img in images_blue]
    )

    image_file_blue = next(img['file'] for img in images_blue if img['caption'] == selected_image_blue)
    image_blue = load_image(image_file_blue)
    if image_blue:
        st.image(image_blue, caption=f"Contenedor azul: {selected_image_blue}")

# Contenedor verde con carrusel de imágenes en la primera columna
with col1:
    st.markdown("## Contenedor verde")
    images_green = [
        {"file": "images/contenedor_verde_1.jpg", "caption": "Botellas de vidrio"},
        {"file": "images/contenedor_verde_2.jpg", "caption": "Frascos de vidrio"}
    ]

    selected_image_green = st.select_slider(
        "Selecciona un tipo de residuo para el contenedor verde",
        options=[img['caption'] for img in images_green]
    )

    image_file_green = next(img['file'] for img in images_green if img['caption'] == selected_image_green)
    image_green = load_image(image_file_green)
    if image_green:
        st.image(image_green, caption=f"Contenedor verde: {selected_image_green}")

# Contenedor marrón con carrusel de imágenes en la segunda columna
with col2:
    st.markdown("## Contenedor marrón")
    images_brown = [
        {"file": "images/contenedor_marron_1.jpg", "caption": "Restos de comida"},
        {"file": "images/contenedor_marron_2.jpg", "caption": "Material vegetal"}
    ]

    selected_image_brown = st.select_slider(
        "Selecciona un tipo de residuo para el contenedor marrón",
        options=[img['caption'] for img in images_brown]
    )

    image_file_brown = next(img['file'] for img in images_brown if img['caption'] == selected_image_brown)
    image_brown = load_image(image_file_brown)
    if image_brown:
        st.image(image_brown, caption=f"Contenedor marrón: {selected_image_brown}")

# Contenedor gris con carrusel de imágenes en la primera columna
with col1:
    st.markdown("## Contenedor gris")
    images_gray = [
        {"file": "images/contenedor_gris_1.jpg", "caption": "Cerámica"},
        {"file": "images/contenedor_gris_2.jpg", "caption": "Juguetes rotos"},
        {"file": "images/contenedor_gris_3.jpg", "caption": "Pañales"}
    ]

    selected_image_gray = st.select_slider(
        "Selecciona un tipo de residuo para el contenedor gris",
        options=[img['caption'] for img in images_gray]
    )

    image_file_gray = next(img['file'] for img in images_gray if img['caption'] == selected_image_gray)
    image_gray = load_image(image_file_gray)
    if image_gray:
        st.image(image_gray, caption=f"Contenedor gris: {selected_image_gray}")


with col2:
    st.markdown("## Otros contenedores")
    images_battery = [
        {"file": "images/contenedor_pilas.jpg", "caption": "Contenedor de pilas y baterías"},
        {"file": "images/contenedor_ropa.jpg", "caption": "Contenedor de ropa"},
        {"file": "images/contenedor_aceite.jpg", "caption": "Contenedor de aceite"}

    ]

    selected_image_battery = st.select_slider(
        "Otros contenedores que también existen",
        options=[img['caption'] for img in images_battery]
    )

    image_file_battery = next(img['file'] for img in images_battery if img['caption'] == selected_image_battery)
    image_battery = load_image(image_file_battery)
    if image_battery:
        st.image(image_battery, caption=f"Otro tipo de contenedores: {selected_image_battery}")


# Información adicional y enlaces
st.markdown(
    """
    ## ¿Quieres saber más?
    En la izquierda podrás encontrar diferentes páginas con las que podrás:
    - Conocer estadísticas de reciclaje y contenedores [Ir a Aprende]()
    - Visualizar los contenedores que hay en València [Ir a Mapa](https://valencianeta-csow8jrrvjysugbmymzp44.streamlit.app/Mapa)
    - Encontrar la ruta más rápida para acceder a uno de ellos [Ir a Buscador](https://valencianeta-csow8jrrvjysugbmymzp44.streamlit.app/Buscador)
    """
)
