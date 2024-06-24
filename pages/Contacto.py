import streamlit as st


st.set_page_config(page_title="Contacta", page_icon="📞")

st.markdown("# Contacta")
st.sidebar.header("Contacta")
st.write("¿Has visto un contenedor que requiera de atención? !Ponte en contacto! De esta forma podremos optimizar los esfuerzos municipales.")


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
