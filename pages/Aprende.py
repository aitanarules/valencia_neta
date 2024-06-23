import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Aprende", page_icon="📊")

st.markdown("# Aprende con datos")
st.sidebar.header("Aprende")
st.write(
    """Esta página muestra la cantidad de residuos registrados en cada país por año. Los datos están representados en 1000 toneladas. En el año 1998 solo se incluyen residuos farmacéuticos.
    Los datos utilizados para generar esta visualización se encuentra en [UNdata](https://data.un.org/Data.aspx?d=ENV&f=variableID%3a1814)."""
)


df = pd.read_csv("./data/amount_wasted_original.csv")

try:
    countries = st.multiselect(
        "Escoge países", df['Country or Area'].unique(), ["Spain"]
    )
    if not countries:
        st.error("Escoge al menos un país, por favor.")
    else:
        data_selected = df[df['Country or Area'].isin(countries)]

        data_selected['Value'] = data_selected['Value']

        st.write("### Cantidad de residuos registrados (medido en 1000 toneladas)")
        st.write(data_selected)

        chart = (
            alt.Chart(data_selected)
            .mark_area(opacity=0.3)
            .encode(
                x='Year:O',
                y=alt.Y('Value:Q', stack=None),
                color='Country or Area:N'
            )
        )
        st.altair_chart(chart, use_container_width=True)


except Exception as e:
    st.error(
        "Ha ocurrido el siguiente error: {}".format(e)
    )
