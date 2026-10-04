import streamlit as st

st.set_page_config(
    page_title= "Factores de gravedad en accidentes de Gran Bretaña",
    layout="wide"
)

st.title("Factores de gravedad en accidentes de transito en Gran Bretaña")

st.markdown("""### **Integrantes**
* Lucciano Morchio
* Benjamin Diaz
* Marcelo Belmar

### Continuidad del proyecto (Avance 2)
* **Problematica:** Las colisiones de transito representan un problema
prioritario de seguridad publica en 2024 se reportaron 128.272 victimas y 1.602 fallecidos en Gran Bretaña.
El estudio de los factores asociados a la gravedad permite avanzar en politicas publicas focalizadas para prevenir los siniestros.
* **Pregunta de investigacion:** ¿Como varia la gravedad de las colisiones de transito segun las condiciones temporales, ambientales 
y las caracteristicas de la via en Gran Bretaña entre 2021 y 2025?.
* **Alcance:** Registros policiales de siniestros con lesiones entre 2021 y 2025 en Gran Bretaña
### Estructura Analitica:
*    **Variables Objetivo (Y):** Gravedad de la colision ('collision_severity': Fatal,Grave,Leve).
*    **Variables Explicativas (X):** Limite de velocidad ('speed_limit'), entorno ('urban_or_rural_area'), iluminacion ('light_conditions'),
 clima('weather_conditions'), tipo de pista('road_type'), Condicion de la superficie de la pista ('road_surface_coditions').
*    **Temporal (T):** Año, mes, dia de la semana y franja horaria ('collision_year','date','time','day_of_week').
### Utiliza el panel lateral para explorar las paginas del estudio:
*   **Contexto u Datos:** Calidad, Volumen, tipos de variables y decisiones de limpieza.
*   **Analisis Exploratorio (EDA):** Distribuciones univariadas, frecuencias y correlaciones.
*   **Analisis de la pregunta:** Relacion entre factores de riesgo (X) y severidad (Y), evolucion temporal (T) y mapa interactivo.
""")