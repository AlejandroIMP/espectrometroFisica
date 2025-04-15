# Detalle del Algoritmo Propuesto
La implementación se realiza en cinco pasos:

## 1. Entrada: Cargar Imagen del Espectro
Objetivo: Permitir que el usuario seleccione una imagen (JPEG/PNG) de su smartphone capturando el patrón de difracción (generado por el CD).

Técnicas y Librerías:

Flask para la carga de archivos (flask.request.files).

OpenCV o PIL para convertir el archivo a una matriz de píxeles para su procesamiento.

## 2. Preprocesamiento: Ajustar Imagen y Detectar ROI
Ajuste de Brillo/Contraste:

Aplicar técnicas de ecualización y CLAHE para mejorar la visibilidad y la uniformidad de la imagen.

Detección del ROI:

Convertir la imagen a una forma en blanco/negro mediante umbralización.

Utilizar el algoritmo de Canny para extraer los bordes y delimitar la región donde se observa el espectro.

## 3. Análisis: Extraer Intensidad y Calcular Longitudes de Onda
Extracción de Intensidad:

Seleccionar una línea (horizontal o vertical, según la dispersión) dentro del ROI.

Recorrer los píxeles a lo largo de esa línea para obtener los valores de intensidad.

Cálculo de Longitudes de Onda:

Emplear la ecuación de difracción (d ⋅ sin(θ) = m ⋅ λ).

Realizar una calibración inicial con una fuente de luz conocida para determinar la relación entre píxel y ángulo.

Convertir cada posición de píxel a su correspondiente longitud de onda.

## 4. Visualización: Gráficos y Resaltado de Picos
Generación de Gráficos:

Utilizar Matplotlib para trazar la gráfica de intensidad vs. longitud de onda.

Añadir etiquetas y leyendas para claridad.

Resaltado de Picos:

Emplear algoritmos (como find_peaks de SciPy) para detectar longitudes de onda dominantes.

Visualizar estos puntos sobre la gráfica para facilitar la interpretación.

## 5. Exportación: Guardar Resultados
Opciones de Exportación:

Exportar los datos en formato CSV utilizando Pandas, permitiendo el análisis en hojas de cálculo u otros entornos.

Guardar la imagen del gráfico (PNG o JPEG) con las funciones de Matplotlib o bien integrarlas al reporte final.

Generar reportes en PDF/HTML que incluyan tanto gráficos como tablas de resultados para presentación profesional.
