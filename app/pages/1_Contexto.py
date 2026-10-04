import streamlit as st
import pandas as pd

st.set_page_config(page_title="Contexto y Datos", layout="wide")

st.title("Contexto, Estructura y Calidad de los Datos")

CSV_PATH = "data/raw/datos_colisiones_granbretaña_2021-2025.csv"

@st.cache_data
def contar_universo_total(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        return sum(1 for _ in f) - 1 

@st.cache_data
def cargar_muestra(ruta):
    cols = [
        'collision_index', 'collision_severity', 'collision_year', 'date', 'time',
        'day_of_week', 'weather_conditions', 'light_conditions', 'speed_limit',
        'road_type', 'road_surface_conditions', 'urban_or_rural_area'
    ]
    return pd.read_csv(ruta, usecols=cols)

try:
    total_universo = contar_universo_total(CSV_PATH)
    df = cargar_muestra(CSV_PATH)
except Exception:
    CSV_PATH = "datos_colisiones_granbretaña_2021-2025.csv"
    total_universo = contar_universo_total(CSV_PATH)
    df = cargar_muestra(CSV_PATH)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Registros analizados", f"{len(df):,}".replace(",", "."))
col2.metric("Total universo base", f"{total_universo:,}".replace(",", "."))
col3.metric("Variables seleccionadas", f"{len(df.columns)}")
col4.metric("Período temporal", f"{df['collision_year'].min()} - {df['collision_year'].max()}")

st.subheader("1. Calidad de Datos y Decisiones de Limpieza")
st.markdown("""
* **Codificación STATS19:** Se empleo la guia oficial (`2024_code_list`) para decodificar las categorias.
* **Valores desconocidos:** Los codigos `-1`, `9` y `99` (indicados como *Missing / Unknown*) fueron identificados para aislarlos y no sesgar los calculos.
* **Depuracion de velocidades:** Se filtran valores no validos de `speed_limit` (quedando solo limites reglamentarios de 20 a 70 mph).
* **Tratamiento temporal:** La variable `date` se convierte a formato de fecha para analizar estacionalidad.
""")

st.subheader("2. Vista Preliminar de Variables Clave")
cols_vista = [
        'collision_index', 'collision_severity', 'collision_year', 'date', 'time',
        'day_of_week', 'weather_conditions', 'light_conditions', 'speed_limit',
        'road_type', 'road_surface_conditions', 'urban_or_rural_area'
    ]
st.dataframe(df[cols_vista].head(8), use_container_width=True)

st.subheader("3. Estructura de Tipos y Detección de Inconsistencias")

calidad_df = pd.DataFrame({
    'Tipo de Variable': df.dtypes.astype(str),
    'Valores NaN': df.isna().sum(),
    'Codigos Desconocidos (-1, 9, 99)': df.isin([-1, 9, 99]).sum()
})

codigos_oficiales = {
    'collision_index': 'Clave alfanumerica (sin nulos)',
    'collision_severity': 'Sin codigos faltantes (1, 2, 3 obligatorios)',
    'collision_year': 'Año completo (sin nulos)',
    'date': 'Formato fecha (DD/MM/AAAA)',
    'day_of_week': 'Dia 1 a 7 (sin nulos)',
    'time': 'Formato hora (HH:MM)',
    'road_type': '-1 (Faltante), 9 (Desconocido)',
    'speed_limit': '-1 (Faltante), 99 (Desconocido)',
    'light_conditions': '-1 (Faltante), 7 (Oscuridad desconocida)',
    'weather_conditions': '-1 (Faltante), 9 (Desconocido)',
    'road_surface_conditions': '-1 (Faltante), 9 (Desconocido)',
    'urban_or_rural_area': '-1 (Faltante), 3 (No asignado)'
}

calidad_df['Codigo Oficial de Faltante'] = calidad_df.index.map(codigos_oficiales)

st.dataframe(calidad_df, use_container_width=True)