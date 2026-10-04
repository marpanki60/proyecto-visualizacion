#PROYECTO DE VISUALIZACION

#NOMBRE DEL PROYECTO
Factores de Gravedad en Accidentes Gran Bretaña

#INTEGRANTES
Benjamin Diaz
Lucciano Morchio
Marcelo Belmar

#DESCRIPCION DEL PROBLEMA
Las colisiones de transito continuan siendo un problema relevante de seguridad vial
y diversos factores pueden alterar la gravedad de las coliciones

#MOTIVACION
El analisis de los factores asociados a la gravedad permite diseñar mejores politicas 
de prevencion y control de accidentes de transito en Gran Bretaña.

#PREGUNTA INICIAL
¿Como varía la gravedad de las colisiones de transito segun las condiciones 
temporales, ambientales y las caracteristicas de la via en Gran Bretaña entre 2021 y 2025?.

#ALCANCE

¿Como las condiciones temporales, ambientales y las caracteristicas de la via en gran bretaña afectan a la gravedad de las colisiones de transito?

Lugar de estudio: gran bretaña.
Periodo: 2021-2025.
Solo colisiones con lesiones registradas.
No se realizaran encuestas.

#FUENTE DEL DATASET

https://www.gov.uk/government/statistical-data-sets/road-safety-open-data#about-this-data

#DESCRIPCION DE LOS DATOS

Dimensiones generales:
    Total de columnas= 44 Variables
    Periodo temporal cubierto= 2021 a 2025

Categorias de las variables:
    Identificacion de colicion y temporalidad
    Ubicacion geografica y autoridades viales locales
    Gravedad e impacto del siniestro
    Caracteristicas de la via
    Condiciones del entorno
    Intervencion policial

#ESTRUCTURA GENERAL DEL REPOSITORIO

proyecto-visualizacion/<br>
|<br>
|-- data/<br>
| |-- raw/<br>
| |-- processed/<br>
|<br>
|-- notebooks/<br>
|  |-- 01_exploracion.ipynb<br>
|<br>
|-- src/<br>
|<br>
|-- figures/<br>
|<br>
|-- app/<br>
|<br>
|-- README.md<br>
|<br>
|-- .gitignore<br>

#Avance 2

#Análisis de Severidad en Siniestros Viales en Gran Bretaña (2021–2025)

#roblema y Pregunta de Investigación

Los siniestros viales constituyen un problema crítico de salud pública y seguridad vial a nivel global. En Gran Bretaña, aunque existe una red vial altamente regulada, la distribución de la gravedad de los impactos varía de forma sustancial dependiendo de la cinemática de la vía y el contexto operacional. 

 **Pregunta de Investigación:**  
 **¿En qué medida los factores de infraestructura vial (límite de velocidad, tipo de calzada) y las condiciones ambientales (iluminación, meteorología) inciden en la severidad de las colisiones viales en Gran Bretaña, y cómo ha evolucionado este riesgo relativo a lo largo del período 2021–2025?**

* **Variable Objetivo ($Y$):** Gravedad de la colisión (`collision_severity` decodificada en `severidad`: Leve, Grave, Fatal).
* **Variables Explicativas ($X$):** Límite de velocidad (`speed_limit`), entorno geográfico (`entorno`), tipo de calzada (`tipo_via`), condiciones meteorológicas (`clima`) e iluminación (`iluminacion`).
* **Dimensión Temporal ($T$):** Año del evento (`collision_year`, 2021–2025), fecha completa y franja horaria intradía.

---

#Descripción del Dataset

El proyecto utiliza los registros oficiales del sistema **STATS19** del Departamento de Transporte del Reino Unido (*Department for Transport - DfT*):
* **Período temporal:** Quinquenio 2021 a 2025.
* **Volumen:** Más de 513.000 colisiones viales registradas formalmente por las fuerzas policiales británicas.
* **Dimensiones clave analizadas:** 12 variables principales que abarcan la severidad del impacto, límites de velocidad reglamentarios, configuración de calzada, estado del asfalto, condiciones meteorológicas, iluminación, y marcas temporales detalladas.

---

#Instrucciones para Obtener los Datos

1. Los microdatos públicos provienen del portal oficial británico de seguridad vial ([data.gov.uk - Road Safety Data / STATS19](https://www.data.gov.uk/dataset/cb7ae6f0-4be6-4935-9277-47e5ce24a11f/road-accidents-safety-data)).
2. Para reproducir el entorno:
   * Colocar el archivo bruto CSV original en la ruta:  
     `data/raw/datos_colisiones_granbretaña_2021-2025.csv`
   * Ejecutar el pipeline de limpieza y filtrado ejecutando el notebook `notebooks/01_exploracion.ipynb` (o el script de preprocesamiento), el cual generará automáticamente la versión optimizada en:  
     `data/processed/datos_colisiones_procesados.csv`

---

#Instrucciones para Ejecutar la Aplicación

Para desplegar y visualizar la plataforma interactiva localmente:

1. **Clonar el repositorio:**
   ```bash
   git clone <URL_DE_TU_REPOSITORIO>
   cd proyecto-visualizacion
