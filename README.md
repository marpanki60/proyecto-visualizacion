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

proyecto-visualizacion/
|
|-- data/
| |-- raw/
| |-- processed/
|
|-- notebooks/
|  |-- 01_exploracion.ipynb
|
|-- src/
|
|-- figures/
|
|-- app/
|
|-- README.md
|
|-- .gitignore
