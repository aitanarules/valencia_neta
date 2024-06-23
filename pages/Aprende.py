import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="DataFrame Demo", page_icon="📊")

st.markdown("# DataFrame Demo")
st.sidebar.header("DataFrame Demo")
st.write(
    """This demo shows how to use `st.write` to visualize Pandas DataFrames."""
)

df = pd.read_csv("./data/amount_wasted.csv")

try:
    countries = st.multiselect(
        "Choose countries", df['Country or Area'].unique(), ["Spain", "Andorra"]
    )
    if not countries:
        st.error("Please select at least one country.")
    else:
        data_selected = df[df['Country or Area'].isin(countries)]

        # Convertir unidades si es necesario
        # Suponiendo que queremos mostrar 'Value' en unidades de 1000 tonnes
        data_selected['Value'] = data_selected['Value']

        st.write("### Agricultural Production (1000 tonnes)")
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
        "An error occurred: {}".format(e)
    )
