import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="DataFrame Demo", page_icon="📊")

st.markdown("# Aprende con datos")
st.sidebar.header("Aprende")
st.write(
    """Esta página muestra gráficamente las cantidades desperdiciadas registradas en cada país por año. Los datos están en toneladas.
    Los datos han sido recabados de la siguiente [página](https://data.un.org/Data.aspx?d=ENV&f=variableID%3a1814)
    
    El año 1998 solo representa datos relativos a residuos farmacéuticos."""
)

df = pd.read_csv("./data/amount_wasted.csv")

try:
    countries = st.multiselect(
        "Escoge país", df['Country or Area'].unique(), ["Spain", "Andorra"]
    )
    if not countries:
        st.error("Selecciona al menos un país, por favor.")
    else:
        # Usar .loc para evitar SettingWithCopyWarning
        data_selected = df.loc[df['Country or Area'].isin(countries)]

        # Convertir unidades si es necesario
        # Suponiendo que queremos mostrar 'Value' en unidades de 1000 toneladas
        data_selected.loc[:, 'Value'] = data_selected['Value']

        st.write("### Cantidad de residuos registrados (en toneladas)")
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

except BaseException as e:
    st.error(
        "Ha ocurrido un error: {}".format(e)
    )
