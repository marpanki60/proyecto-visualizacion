1. Identificación y Tiempo
collision_index: Identificador único global del siniestro. Combina el año y el número de referencia para relacionar esta tabla con las de vehículos y víctimas.

collision_year: Año en que ocurrió la colisión (entero, ej. 2021 a 2025).

collision_ref_no: Número de referencia local asignado internamente por la fuerza policial interviniente.

date: Fecha del accidente (formato DD/MM/AAAA).

day_of_week: Día de la semana en que ocurrió el siniestro:

1: Domingo (Sunday)

2: Lunes (Monday)

3: Martes (Tuesday)

4: Miércoles (Wednesday)

5: Jueves (Thursday)

6: Viernes (Friday)

7: Sábado (Saturday)

time: Hora estimada del siniestro en formato HH:MM.

2. Ubicación y Georreferenciación
location_easting_osgr: Coordenada Este en la cuadrícula cartográfica oficial de Gran Bretaña (British National Grid).

location_northing_osgr: Coordenada Norte en la cuadrícula británica.

longitude: Longitud geográfica (coordenada decimal WGS84).

latitude: Latitud geográfica (coordenada decimal WGS84).

local_authority_district: Código numérico de la autoridad o distrito municipal local (ej. 1 = Westminster, 2 = Camden, etc.).

local_authority_ons_district: Código alfanumérico territorial asignado por la Oficina Nacional de Estadísticas británica (ONS) (ej. E06000002).

local_authority_highway: Código ONS de la autoridad responsable del mantenimiento de la carretera al momento del hecho.

local_authority_highway_current: Código de autoridad vial actualizado a los límites geográficos vigentes más recientes.

lsoa_of_accident_location: Código censal de área mínima (Lower Layer Super Output Area), utilizado para vincular estadísticas socioeconómicas y demográficas.

urban_or_rural_area: Clasificación del entorno del área:

1: Urbano (Urban)

2: Rural (Rural)

3: No asignado (Unallocated)

-1: Dato faltante o fuera de rango

trunk_road_flag: Indica si la vía forma parte de la red de carreteras troncales/estatales principales:

1: Carretera troncal gestionada por la agencia nacional (Trunk / National Highways)

2: Carretera no troncal / red local (Non-trunk)

-1: Desconocido o fuera de rango

3. Gravedad y Víctimas
collision_severity: Gravedad máxima del siniestro:

1: Fatal (Fatal, hubo al menos un fallecido dentro de los 30 días posteriores al hecho).

2: Grave (Serious, hospitalización o lesiones severas).

3: Leve (Slight, contusiones, cortes menores, sin hospitalización prolongada).

enhanced_severity_collision: Clasificación detallada incorporada a partir de 2023:

1: Fatal (Fatal)

5: Muy grave (Very Serious)

6: Moderadamente grave (Moderately Serious)

7: Menos grave (Less Serious)

3: Leve (Slight)

-1: Dato faltante

number_of_vehicles: Cantidad total de vehículos involucrados.

number_of_casualties: Cantidad total de personas que resultaron heridas o fallecidas.

collision_injury_based: Método de clasificación de gravedad:

0: Basado en el reporte tradicional de severidad policial.

1: Basado en el registro detallado de lesiones médicas (sistema CRASH / COPA).

collision_adjusted_severity_serious: Valor de probabilidad ajustada para colisiones graves (ajuste estadístico del DfT para corregir inconsistencias históricas entre fuerzas policiales).

collision_adjusted_severity_slight: Valor de probabilidad ajustada para colisiones leves.

4. Características de la Vía y Cruces
first_road_class: Tipo o jerarquía de la carretera principal:

1: Autopista (Motorway, designadas como M)

2: Autovía tipo A (A(M))

3: Carretera principal clase A (A)

4: Carretera secundaria clase B (B)

5: Carretera menor clase C (C)

6: Vía sin clasificar / calle local (Unclassified)

-1: Dato faltante

first_road_number: Número oficial de la ruta principal (ej. carretera 139). Es 0 en vías C o sin clasificar porque no tienen número oficial.

road_type: Tipo de calzada:

1: Rotonda (Roundabout)

2: Calle de sentido único (One way street)

3: Calzada doble / con mediana separadora (Dual carriageway)

6: Calzada simple de doble sentido (Single carriageway)

7: Rampa o carril de incorporación/salida (Slip road)

12: Calle de sentido único / rampa de acceso

9 / -1: Desconocido o fuera de rango

speed_limit: Límite de velocidad legal de la vía en millas por hora (20, 30, 40, 50, 60, 70). Si es -1 o 99, el dato es desconocido o no reportado.

second_road_class: Jerarquía de la vía secundaria si el choque ocurrió en un cruce:

0: No ocurrió en un cruce o estuvo a más de 20 metros de uno.

1 a 6: Misma clasificación que first_road_class.

second_road_number: Número de la vía secundaria en una intersección (0 si no aplica o es vía no numerada).

junction_detail: Configuración de la intersección (especificación STATS19 vigente):

0: Fuera de una intersección (o a más de 20 metros de ella)

13: Cruce en T o en Y escalonado

16: Cruce de cuatro vías / encrucijada (Crossroads)

17: Cruce múltiple con más de 4 ramales (sin ser rotonda)

18: Entrada o salida de camino/acceso privado

19: Otro tipo de intersección

99 / -1: Desconocido o sin información

junction_detail_historic: Codificación previa de la intersección (formato anterior a 2024):

0: Sin cruce; 1: Rotonda; 2: Mini-rotonda; 3: Cruce en T/Y; 5: Rampa; 6: Cuatro vías; 7: Más de 4 ramales; 8: Camino privado; 9: Otro.

junction_control: Sistema de control o prioridad de tránsito en la intersección:

0: Fuera de cruce (a más de 20 m)

1: Agente de tránsito o persona autorizada

2: Semáforo automático

3: Señal de Alto / STOP

4: Señal de Ceda el paso o intersección sin control prioritario

9 / -1: Desconocido o sin registro

5. Pasos Peatonales
pedestrian_crossing: Cruces peatonales en un radio de 50 metros (especificación 2024):

0: Ningún cruce físico a menos de 50 metros

11: Control manual por patrulla escolar

12: Control manual por otra persona autorizada

13: Paso de cebra (Zebra crossing)

14: Cruce semaforizado peatonal (Pelican, puffin o toucan)

15: Fase peatonal integrada en un semáforo de intersección vehicular

16: Pasarela aérea o túnel peatonal subterráneo

17: Refugio o isleta central divisoria (sin otros controles)

99 / -1: Desconocido o sin registro

pedestrian_crossing_human_control_historic: Campo histórico para control humano (0: Ninguno, 1: Patrulla escolar, 2: Otra persona).

pedestrian_crossing_physical_facilities_historic: Campo histórico para infraestructura peatonal (0: Ninguna, 1: Cebra, 4: Semáforo peatonal, 5: Fase peatonal en cruce, 7: Pasarela/túnel, 8: Isleta central).

6. Condiciones Ambientales y del Entorno
light_conditions: Iluminación del lugar:

1: Luz diurna (Daylight)

4: Oscuridad con alumbrado público encendido (Lights lit)

5: Oscuridad con alumbrado público apagado o defectuoso (Lights unlit)

6: Oscuridad sin red de alumbrado público (No lighting)

7 / -1: Oscuridad con estado de alumbrado desconocido / dato faltante

weather_conditions: Condiciones climáticas:

1: Despejado / buen tiempo sin vientos fuertes

2: Lloviendo sin vientos fuertes

3: Nevando sin vientos fuertes

4: Despejado con vientos fuertes

5: Lloviendo con vientos fuertes

6: Nevando con vientos fuertes

7: Niebla o neblina (Fog or mist)

8: Otras condiciones climáticas

9 / -1: Desconocido o dato faltante

road_surface_conditions: Estado de la superficie de la calzada:

1: Seco (Dry)

2: Mojado o húmedo (Wet or damp)

3: Nieve (Snow)

4: Escarcha o hielo (Frost or ice)

5: Inundación / charco con profundidad superior a 3 cm

6: Presencia de aceite o combustible derramado

7: Barro o lodo

9 / -1: Desconocido o dato no reportado

special_conditions_at_site: Alteraciones o anomalías físicas en el lugar:

0: Ninguna anomalía

1: Semáforo automático apagado por completo

2: Semáforo con fallas parciales

3: Señalización vial defectuosa, dañada o poco visible

4: Obras viales en construcción o mantenimiento (Roadworks)

5: Defecto o deterioro en la superficie del pavimento

6: Aceite o combustible

7: Barro

9 / -1: Desconocido o no informado

carriageway_hazards: Obstáculos o peligros en la calzada (especificación vigente):

0: Ningún peligro presente

11: Semáforos averiados

12: Señalización vial permanente tapada o inadecuada

13: Obras en la vía

14: Aceite o diésel

15: Barro

16: Carga caída o desprendida de un vehículo

17: Otro objeto sobre la vía

18: Relacionado con un siniestro previo en el mismo punto

19: Peatón en la calzada (que no resultó herido)

-1 / 9: Desconocido o dato faltante

carriageway_hazards_historic: Codificación anterior de peligros (1: Carga desprendida, 2: Otro objeto, 3: Accidente previo, 4: Perro en la calzada, 5/7: Otros animales, 6: Peatón no lesionado).

7. Intervención Policial
police_force: Código de la fuerza policial actuante (ej. 1 = Metropolitan Police de Londres, 3 = Cumbria, 4 = Lancashire, 6 = Greater Manchester, etc.).

did_police_officer_attend_scene_of_accident: Indica si un oficial de policía concurrió a la escena del siniestro:

1: Sí concurrió (Yes)

2: No concurrió (No)

3: No concurrió; siniestro reportado por autodeclaración ciudadana mediante formulario web/papel (Self completion form)

-1: Desconocido o dato ausente