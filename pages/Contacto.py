import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Contacta", page_icon="📞")

st.markdown("# Contacta")
st.sidebar.header("Contacta")
st.write("¿Has visto un contenedor que requiera de atención? ¡Ponte en contacto! De esta forma podremos optimizar los esfuerzos municipales.")

# Define la dirección de correo
email_address = "tucorreo@example.com"  # Reemplaza esto con la dirección de correo real

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

# Formulario de contacto
contact_form = f"""
<form action="https://formsubmit.co/{email_address}" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Tu nombre" required>
    <input type="email" name="email" placeholder="Tu email" required>
    <input type="text" name="text" placeholder="La ubicación del contenedor" required>
    <textarea name="message" placeholder="Tu mensaje aquí." required></textarea>
    <button type="submit">Enviar</button>
</form>
"""

# Renderiza los estilos y el formulario en la página
st.markdown(css_style, unsafe_allow_html=True)
st.markdown(contact_form, unsafe_allow_html=True)
