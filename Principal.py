import streamlit as st

st.set_page_config(
    page_title="ValènciaNetApp",
    page_icon="♻️",
)

#config
st.set_page_config(page_title="ValènciaNetApp", page_icon="♻️", layout="wide")
# local_css("style/style.css")


with st.container():
    st.subheader("Hola! Som València neta:")
    st.title("L'aplicació que t'ajudarà a reciclar més fàcilment")
    st.write(
        "Som unes estudiants de Ciència de dades i aquesta és la nostra app amb la que volem ajudar el mediambient mitjançant la tecnologia."  ("[Conéixer més >>](https://valerapp.com/)")
    )

st.sidebar.success("Selecciona una pantalla.")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)
