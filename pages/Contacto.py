import streamlit as st
import pandas as pd
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="Contacta", page_icon="📞")

st.markdown("# Contacta")
st.sidebar.header("Contacta")
st.write("¿Has visto un contenedor que requiera de atención? ¡Ponte en contacto! De esta forma podremos optimizar los esfuerzos municipales.")

# Estilos CSS
css_style = """
<style>
/* Style inputs with type="text", select elements and textareas */
input[type=message], input[type=email], input[type=text], textarea {
  width: 100%; /* Full width */
  padding: 12px; /* Some padding */ 
  border: 1px solid #ccc; /* Gray border */
  border-radius: 4px; /* Rounded borders */
  box-sizing: border-box; /* Make sure that padding and width stays in place */
  margin-top: 6px; /* Add a top margin */
  margin-bottom: 16px; /* Bottom margin */
  resize: vertical; /* Allow the user to vertically resize the textarea (not horizontally) */
}

/* Style the submit button with a specific background color etc */
button[type=submit] {
  background-color: #04AA6D;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

/* When moving the mouse over the submit button, add a darker green color */
button[type=submit]:hover {
  background-color: #45a049;
}

/* Hide Streamlit Branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""

# Define la función para guardar los datos en un CSV
def save_to_csv(data):
    df = pd.DataFrame([data])
    with open("comments.csv", "a") as f:
        df.to_csv(f, header=f.tell()==0, index=False)

# Si el formulario es enviado, procesa los datos
if st.button("Enviar"):
    name = st.text_input("Tu nombre")
    email = st.text_input("Tu email")
    location = st.text_input("La ubicación del contenedor")
    message = st.text_area("Tu mensaje aquí.")

    if st.button("Enviar"):
        if name and email and location and message:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data = {
                "name": name,
                "email": email,
                "location": location,
                "message": message,
                "timestamp": timestamp
            }
            save_to_csv(data)
            st.success("¡Formulario enviado correctamente!")
        else:
            st.error("Por favor, completa todos los campos.")

# Renderiza los estilos y el formulario en la página
st.markdown(css_style, unsafe_allow_html=True)

# Renderiza el formulario HTML
form = """
<form action="" method="post">
    <input type="text" name="name" placeholder="Tu nombre" required>
    <input type="email" name="email" placeholder="Tu email" required>
    <input type="text" name="location" placeholder="La ubicación del contenedor" required>
    <textarea name="message" placeholder="Tu mensaje aquí." required></textarea>
    <button type="submit">Enviar</button>
</form>
"""

st.markdown(form, unsafe_allow_html=True)
