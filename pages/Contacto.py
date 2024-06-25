import streamlit as st
from sqlalchemy import create_engine, Column, String, Text, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la página
st.set_page_config(page_title="Contacta", page_icon="📞")

st.markdown("# Contacta")
st.sidebar.header("Contacta")
st.write("¿Has visto un contenedor que requiera de atención? ¡Ponte en contacto! De esta forma podremos optimizar los esfuerzos municipales.")

# Crear una conexión a la base de datos SQLite
engine = create_engine('sqlite:///contactos.db')
Base = declarative_base()

# Definir la estructura de la tabla en la base de datos
class Contacto(Base):
    __tablename__ = 'contactos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    ubicacion = Column(String(100), nullable=False)
    mensaje = Column(Text, nullable=False)

# Crear la tabla en la base de datos si no existe
Base.metadata.create_all(engine)

# Crear una sesión de base de datos
Session = sessionmaker(bind=engine)
session = Session()

# Controladores de estado para el formulario
form_state = st.session_state.setdefault('form_state', {
    'nombre': '',
    'email': '',
    'ubicacion': '',
    'mensaje': ''
})

# Formulario de contacto
with st.form(key='contact_form'):
    nombre = st.text_input("Nombre", value=form_state['nombre'])
    email = st.text_input("Email", value=form_state['email'])
    ubicacion = st.text_input("La ubicación del contenedor.", value=form_state['ubicacion'])
    mensaje = st.text_area("Tu mensaje aquí.", value=form_state['mensaje'])
    submit_button = st.form_submit_button(label='Enviar')

# Validación de campos
if submit_button:
    if not nombre:
        st.error("Por favor, introduce tu nombre.")
    elif not email:
        st.error("Por favor, introduce tu email.")
    elif not ubicacion:
        st.error("Por favor, introduce la ubicación del contenedor.")
    elif not mensaje:
        st.error("Por favor, introduce tu mensaje.")
    else:
        # Guardar los datos en la base de datos
        nuevo_contacto = Contacto(nombre=nombre, email=email, ubicacion=ubicacion, mensaje=mensaje)
        session.add(nuevo_contacto)
        session.commit()
        st.success("¡Tu mensaje ha sido enviado con éxito!")
        
        # Limpiar los campos del formulario después de enviar
        form_state['nombre'] = ''
        form_state['email'] = ''
        form_state['ubicacion'] = ''
        form_state['mensaje'] = ''

# Mostrar los datos almacenados (opcional, solo para demostración)
st.markdown("### Reseñas")

contactos = session.query(Contacto).all()

# Verificar si hay contactos
if contactos:
    for contacto in contactos:
        st.markdown(f"""
        <div style="background-color: #f9f9f9; padding: 10px; border-radius: 5px; margin-bottom: 10px;">
            <h4 style="color: #4CAF50;">{contacto.nombre}</h4>
            <p><strong>Ubicación:</strong> {contacto.ubicacion}</p>
            <p><strong>Mensaje:</strong> {contacto.mensaje}</p>
        </div>
        """, unsafe_allow_html=True)
else:
    st.write("No hay reseñas disponibles.")

# Botón para borrar los datos
if st.button("Borrar todas las reseñas"):
    session.query(Contacto).delete()
    session.commit()
    st.warning("Todas las reseñas han sido borradas.")
    st.experimental_rerun()  # Recargar la aplicación para reflejar los cambios
