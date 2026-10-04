import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Análisis Exploratorio (EDA)", layout="wide")

st.title("Analisis Exploratorio de Datos (EDA)")
st.markdown("""
En esta seccion se exploran las distribuciones individuales y frecuencias de la variable objetivo (**$Y$**) 
y las principales variables explicativas del entorno y la vía (**$X$**), evaluando sus patrones de comportamiento.
""")

CSV_PATH = "data/processed/datos_colisiones_procesados.csv"

@st.cache_data
def cargar_datos_analisis(ruta):
    df = pd.read_csv(ruta)
    df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce')
    df['collision_year'] = df['collision_year'].astype(int)
    return df

df = cargar_datos_analisis(CSV_PATH)

st.sidebar.header("Filtros de Exploracion")
entorno_sel = st.sidebar.multiselect(
    "Filtrar por Entorno Geografico:",
    options=['Urbano', 'Rural'],
    default=['Urbano', 'Rural']
)

df_filtrado = df[df['entorno'].isin(entorno_sel)]

st.subheader("1. Distribución de la Variable Objetivo ($Y$: Gravedad de la Colision)")

col_metric1, col_metric2, col_metric3 = st.columns(3)
prop_leve = (df_filtrado['severidad'] == 'Leve').mean() * 100
prop_grave = (df_filtrado['severidad'] == 'Grave').mean() * 100
prop_fatal = (df_filtrado['severidad'] == 'Fatal').mean() * 100

col_metric1.metric("Proporcion Leve", f"{prop_leve:.1f}%")
col_metric2.metric("Proporcion Grave", f"{prop_grave:.1f}%")
col_metric3.metric("Proporcion Fatal", f"{prop_fatal:.2f}%")

fig_y = px.histogram(
    df_filtrado,
    x='severidad',
    color='severidad',
    category_orders={'severidad': ['Leve', 'Grave', 'Fatal']},
    color_discrete_map={'Fatal': '#e63946', 'Grave': '#f4a261', 'Leve': '#2a9d8f'},
    labels={'severidad': 'Nivel de Gravedad', 'count': 'Total de Colisiones'},
    title="Frecuencia por Gravedad de Colisiones (Variable Y)"
)
st.plotly_chart(fig_y, use_container_width=True)

st.markdown("""
> **Observacion e Interpretacion:**  
> Se evidencia un fuerte desbalance de clases: las colisiones leves agrupan más del 70% del universo analizado, 
> mientras que los desenlaces fatales representan menos del 2%. Este desbalance es critico para el proyecto, 
> ya que el analisis requiere evaluar tasas y proporciones relativas para no invisibilizar los eventos de mayor letalidad.
""")

st.markdown("---")

col_izq, col_der = st.columns(2)

with col_izq:
    st.subheader("2. Distribución de Limites de Velocidad")
    fig_speed = px.histogram(
        df_filtrado,
        x='speed_limit',
        nbins=12,
        color_discrete_sequence=['#457b9d'],
        labels={'speed_limit': 'Limite de Velocidad (mph)', 'count': 'Frecuencia'},
        title="Frecuencia por Limite de Velocidad Reglamentario"
    )
    st.plotly_chart(fig_speed, use_container_width=True)
    st.markdown("""
    > **Interpretacion:** La gran mayoría de los siniestros ocurre en zonas con límite de 30 mph, 
    > correspondiente a la velocidad estándar en zonas urbanas de Gran Bretaña.
    """)

with col_der:
    st.subheader("3. Tipo de Via")
    top_vias = df_filtrado['tipo_via'].value_counts().reset_index()
    top_vias.columns = ['tipo_via', 'Cantidad']
    
    fig_vias = px.bar(
        top_vias,
        x='Cantidad',
        y='tipo_via',
        orientation='h',
        color_discrete_sequence=['#1d3557'],
        title="Colisiones segun configuracion de la Via"
    )
    fig_vias.update_layout(yaxis={'categoryorder': 'total ascending'})
    st.plotly_chart(fig_vias, use_container_width=True)
    st.markdown("""
    > **Interpretacion:** La calzada simple (*Single carriageway*) concentra la gran mayoría de las colisiones, 
    > superando con amplitud a vias dobles o rotondas.
    """)

st.markdown("---")

col_clima, col_tiempo = st.columns(2)

with col_clima:
    st.subheader("4. Condiciones Ambientales (Clima y Luz)")
    fig_clima = px.histogram(
        df_filtrado,
        x='clima',
        color='iluminacion',
        title="Distribucin de Colisiones segun Clima e Iluminación",
        labels={'clima': 'Condicion Meteorológica', 'iluminacion': 'Iluminación', 'count': 'Colisiones'}
    )
    st.plotly_chart(fig_clima, use_container_width=True)
    st.markdown("""
    > **Interpretacion:** La mayor cantidad de siniestros ocurre bajo tiempo despejado y en luz diurna; 
    > no obstante, la presencia de oscuridad y precipitaciones introduce una mayor dispersión de riesgo.
    """)

with col_tiempo:
    st.subheader("5. Patron Horario de Siniestros")
    fig_hora = px.histogram(
        df_filtrado.dropna(subset=['hora']),
        x='hora',
        nbins=24,
        color_discrete_sequence=['#2a9d8f'],
        title="Distribucion de Colisiones por Hora del Día",
        labels={'hora': 'Hora del Día (0-23)', 'count': 'Frecuencia'}
    )
    st.plotly_chart(fig_hora, use_container_width=True)
    st.markdown("""
    > **Interpretacion:** Se aprecian claramente dos picos de concentración horaria en torno a las 08:00 y las 17:00-18:00 hrs, 
    > coincidiendo con los horarios de mayor flujo vehicular laboral.
    """)