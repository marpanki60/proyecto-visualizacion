import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Analisis y Respuesta a la Pregunta", layout="wide")

st.title("Analisis y Respuesta a la Pregunta de Investigación")
st.markdown("""
Esta seccion articula la relación entre los factores del entorno y de la vía (**$X$**) 
con la gravedad de las colisiones (**$Y$**), integrando la evolución temporal (**$T$**) 
para evaluar qué condiciones maximizan el riesgo de siniestros graves o fatales.
""")

CSV_PATH = "data/processed/datos_colisiones_procesados.csv"

@st.cache_data
def cargar_datos_analisis(ruta):
    df = pd.read_csv(ruta)
    df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce')
    df['collision_year'] = df['collision_year'].astype(int)
    return df

df = cargar_datos_analisis(CSV_PATH)

st.sidebar.header("Controles de Analisis")
anios_disponibles = sorted(df['collision_year'].dropna().unique().tolist())
anios_sel = st.sidebar.multiselect(
    "Filtrar por Años (Dimension T):",
    options=anios_disponibles,
    default=anios_disponibles
)

df_filtrado = df[df['collision_year'].isin(anios_sel)]

st.subheader("1. Evolucion Temporal de la Tasa de Gravedad (2021 - 2025)")

tendencia_anual = df_filtrado.groupby('collision_year').agg(
    total=('collision_index', 'count'),
    tasa_grave_fatal=('es_grave_fatal', lambda x: x.mean() * 100),
    tasa_fatal=('es_fatal', lambda x: x.mean() * 100)
).reset_index()

fig_temp = px.line(
    tendencia_anual,
    x='collision_year',
    y=['tasa_grave_fatal', 'tasa_fatal'],
    markers=True,
    title="Evolución Multianual de la Proporción de Siniestros Graves y Fatales (%)",
    labels={'value': 'Porcentaje sobre el Total (%)', 'collision_year': 'Año del Siniestro', 'variable': 'Métrica'},
    color_discrete_map={'tasa_grave_fatal': '#e63946', 'tasa_fatal': '#457b9d'}
)

fig_temp.update_layout(
    xaxis=dict(
        tickmode='linear',
        tick0=2021,
        dtick=1
    )
)

fig_temp.for_each_trace(lambda t: t.update(name={
    'tasa_grave_fatal': '% Severidad Alta (Grave + Fatal)',
    'tasa_fatal': '% Desenlace Fatal'
}[t.name]))

st.plotly_chart(fig_temp, use_container_width=True)

st.markdown("""
> **Interpretación Temporal:**  
> Al aislar el efecto del volumen bruto, la tasa relativa de colisiones con consecuencias graves o fatales muestra una tendencia persistente entre el 25% y el 28%, evidenciando que las mejoras en infraestructura o regulaciones vehiculares tienen un impacto gradual sobre la letalidad general.
""")

st.markdown("---")

st.subheader("2. Impacto de la Velocidad y el Entorno en la Letalidad")

col_izq, col_der = st.columns(2)

with col_izq:
    riesgo_velocidad = df_filtrado.groupby('speed_limit').agg(
        tasa_letalidad=('es_grave_fatal', lambda x: x.mean() * 100),
        total_casos=('collision_index', 'count')
    ).reset_index()
    riesgo_velocidad = riesgo_velocidad[riesgo_velocidad['total_casos'] > 200]

    fig_vel = px.bar(
        riesgo_velocidad,
        x='speed_limit',
        y='tasa_letalidad',
        color='tasa_letalidad',
        color_continuous_scale='Reds',
        title="Tasa de Gravedad Alta por Límite de Velocidad (mph)",
        labels={'speed_limit': 'Límite de Velocidad (mph)', 'tasa_letalidad': '% Choques Graves o Fatales'}
    )
    st.plotly_chart(fig_vel, use_container_width=True)
    st.markdown("""
    > **Hallazgo Clave:** A mayor velocidad reglamentaria, el porcentaje de colisiones que resultan en gravedad o muerte se incrementa significativamente, pasando de aproximadamente 20% en zonas de 20-30 mph a más del 35% en vías de 60-70 mph.
    """)

with col_der:
    riesgo_entorno = df_filtrado.groupby(['entorno', 'tipo_via']).agg(
        tasa_grave=('es_grave_fatal', lambda x: x.mean() * 100),
        casos=('collision_index', 'count')
    ).reset_index()
    riesgo_entorno = riesgo_entorno[riesgo_entorno['casos'] > 300]

    fig_entorno = px.bar(
        riesgo_entorno,
        x='tipo_via',
        y='tasa_grave',
        color='entorno',
        barmode='group',
        color_discrete_map={'Urbano': '#457b9d', 'Rural': '#e63946'},
        title="Tasa de Severidad Alta por Tipo de Vía y Entorno",
        labels={'tasa_grave': '% Severidad Alta', 'tipo_via': 'Configuración de la Calzada', 'entorno': 'Entorno'}
    )
    st.plotly_chart(fig_entorno, use_container_width=True)
    st.markdown("""
    > **Hallazgo Clave:** En todos los tipos de vía, el **entorno rural** exhibe una tasa de severidad sistemáticamente superior al entorno urbano, impulsado por mayores velocidades de circulación y mayores distancias hacia centros de asistencia.
    """)

st.markdown("---")

st.subheader("3. Riesgo Combinado: Iluminacion y Condiciones Climaticas")

matriz_riesgo = df_filtrado[
    (df_filtrado['iluminacion'] != 'Otro / Desconocido') & 
    (df_filtrado['clima'].isin(['Despejado', 'Lluvia', 'Nieve', 'Niebla']))
].groupby(['iluminacion', 'clima']).agg(
    tasa_letalidad=('es_grave_fatal', lambda x: x.mean() * 100),
    volumen=('collision_index', 'count')
).reset_index()

matriz_riesgo = matriz_riesgo[matriz_riesgo['volumen'] > 100]

fig_matriz = px.density_heatmap(
    matriz_riesgo,
    x='clima',
    y='iluminacion',
    z='tasa_letalidad',
    color_continuous_scale='OrRd',
    title="Mapa Termico de Riesgo: Tasa de Siniestros Graves/Fatales(%)",
    labels={'tasa_letalidad': '% Severidad Alta', 'iluminacion': 'Condición de Luz', 'clima': 'Clima'}
)
st.plotly_chart(fig_matriz, use_container_width=True)

st.markdown("""
> **Observacion:**  
> La mayor concentracion de riesgo se produce en condiciones de **Noche sin alumbrado** combinadas con visibilidad comprometida (**Niebla o Lluvia**). La falta de iluminación artificial agrava de forma no lineal las probabilidades de fatalidad.
""")

st.markdown("---")

# --- SÍNTESIS DE RESPUESTA A LA PREGUNTA ---
st.subheader("Conclusiones y Respuesta a la Pregunta de Investigación")
st.success("""
**¿Qué factores influyen en la gravedad de las colisiones en Gran Bretaña (2021-2025)?**

1. **Velocidad y Entorno Geográfico (Factores Dominantes):** El límite de velocidad de la vía y la naturaleza rural son los dos predictores de mayor correlacion con la letalidad. Mientras que la ciudad concentra el volumen de choques leves, las vías interurbanas rurales de 60 mph concentran el mayor porcentaje de fallecimientos.
2. **Visibilidad e Iluminación:** La ausencia total de iluminación artificial durante la noche multiplica el riesgo de severidad alta frente a la luz diurna, superando incluso el impacto aislado de la lluvia.
3. **Estabilidad Temporal:** El patrón de severidad no presenta caídas drásticas año a año, confirmando que el riesgo está fuertemente anclado a la infraestructura vial y la cinemática del impacto más que a variaciones estacionales menores.
""")