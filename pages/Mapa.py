import streamlit as st
import geopandas as gpd

# Verificar si el archivo existe
file_path = './pages/reciclatge.geojson'
try:
    # Intentar leer el archivo
    gdf = gpd.read_file(file_path)
    st.success('Archivo cargado exitosamente.')
except FileNotFoundError:
    st.error(f'El archivo {file_path} no se encontró.')
except Exception as e:
    st.error(f'Error al leer el archivo: {e}')

# Mostrar el contenido de GeoDataFrame
if 'gdf' in locals():
    st.write(gdf.head())
