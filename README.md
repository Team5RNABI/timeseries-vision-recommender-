# Timeseries Vision Recommender

Repositorio academico orientado al desarrollo de soluciones de machine learning para el sector transporte y turismo. El proyecto integra tres frentes principales:

1. Prediccion de demanda mediante analisis de series de tiempo.
2. Clasificacion de actividades distractivas del conductor a partir de imagenes.
3. Recomendacion personalizada de destinos turisticos.

El repositorio esta estructurado para documentar el trabajo de investigacion, conservar los artefactos del modelo y permitir la reproduccion local de los notebooks.

## Resumen Ejecutivo

La propuesta combina analitica descriptiva, aprendizaje automatico y vision por computador para apoyar decisiones operativas y de experiencia de usuario:

- estimar la demanda futura de un servicio para mejorar la planificacion,
- identificar comportamientos de riesgo en la conduccion,
- y sugerir destinos de viaje segun el perfil y la historia del usuario.

La solucion esta organizada por modulos independientes, lo que facilita el mantenimiento, la evaluacion y la reutilizacion de cada componente.

## Alcance Del Proyecto

Este repositorio contiene el material base del proyecto, incluyendo notebooks de exploracion, entrenamiento y evaluacion, ademas de datasets y modelos serializados.

No es una aplicacion desplegada con una unica entrada ejecutable; el flujo de trabajo principal es el analisis desde notebooks y la carga de artefactos guardados.

## Modulos Del Sistema

### Modulo 1: Prediccion De Demanda

Notebook de serie temporal para modelar la demanda de transporte o turismo y apoyar la planificacion operativa.

Proposito:

- analizar tendencia y comportamiento temporal,
- estimar valores futuros de demanda,
- y servir como base para decisiones de capacidad y operacion.

Salida esperada:

- predicciones a futuro a partir de historicos y variables temporales.

### Modulo 2: Clasificacion De Imagenes

Notebook de vision por computador basado en una red neuronal convolucional para clasificar imagenes del conductor.

Categorias incluidas en el clasificador:

- `safe_driving`
- `other_activities`
- `talking_phone`
- `texting_phone`
- `turning`

Proposito:

- detectar distracciones o estados relevantes de conduccion,
- y apoyar analisis de seguridad vial.

Artefactos asociados:

- `Module2/modelos/modelo_final.keras`
- `Module2/modelos/modelo_final_cnn.h5`

### Modulo 3: Sistema De Recomendacion

Notebook y artefactos para recomendar destinos turisticos de forma personalizada.

Proposito:

- explorar preferencias e historial de usuarios,
- generar recomendaciones relevantes,
- y evaluar enfoques de filtrado colaborativo y contenido, segun el planteamiento del proyecto.

Artefacto principal:

- `Module3/model_production/model_module_3.pkl`

## Tecnologias Y Dependencias

El archivo `requirements.txt` incluye la base cientifica del proyecto:

- `numpy`
- `scipy`
- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `Cython`
- `jupyter`

Dependiendo del notebook que ejecutes, puede ser necesario instalar dependencias adicionales usadas en celdas especificas o en el entorno de entrenamiento original.

## Estructura Del Repositorio

```text
.
|-- Module 1/
|   \-- Pred_Demanda_Transporte.ipynb
|-- Module2/
|   |-- Module2_CNN_Classifier.ipynb
|   \-- modelos/
|       |-- modelo_final.keras
|       \-- modelo_final_cnn.h5
|-- Module3/
|   |-- DATA/
|   |   |-- Expanded_Destinations.csv
|   |   |-- Final_Updated_Expanded_Reviews.csv
|   |   |-- Final_Updated_Expanded_UserHistory.csv
|   |   \-- Final_Updated_Expanded_Users.csv
|   |-- NOTEBOOK/
|   |   |-- EDA.ipynb
|   |   \-- modelo_Recomendacioes.ipynb
|   \-- model_production/
|       \-- model_module_3.pkl
|-- README.md
|-- LICENSE
|-- requirements.txt
\-- reinstalar_dependencias.py
```

## Instalacion

### 1. Crear un entorno virtual

En Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

En macOS o Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Iniciar Jupyter

```bash
jupyter notebook
```

Tambien puedes usar:

```bash
jupyter lab
```

## Uso Recomendado

### Para analisis y reproduccion

1. Abre primero `Module3/NOTEBOOK/EDA.ipynb` para revisar el contexto de datos.
2. Continua con `Module3/NOTEBOOK/modelo_Recomendacioes.ipynb` para el entrenamiento o carga del sistema de recomendacion.
3. Revisa `Module2/Module2_CNN_Classifier.ipynb` para la parte de vision por computador.
4. Ejecuta `Module 1/Pred_Demanda_Transporte.ipynb` para la prediccion temporal de demanda.

### Para usar artefactos serializados

- `Module2/modelos/modelo_final.keras`
- `Module2/modelos/modelo_final_cnn.h5`
- `Module3/model_production/model_module_3.pkl`

Los notebooks y scripts asociados deben ejecutarse desde la raiz del repositorio para que las rutas relativas funcionen correctamente.

## Datasets Incluidos

El proyecto conserva los datos necesarios para reproducir el modulo de recomendacion:

- `Module3/DATA/Expanded_Destinations.csv`
- `Module3/DATA/Final_Updated_Expanded_Reviews.csv`
- `Module3/DATA/Final_Updated_Expanded_UserHistory.csv`
- `Module3/DATA/Final_Updated_Expanded_Users.csv`

Si planeas modificar el flujo, procura mantener la misma estructura de carpetas o actualizar las rutas en los notebooks.

## Notas Tecnicas

- Los notebooks fueron pensados para ejecucion secuencial y exploratoria.
- Las rutas relativas dependen de que el directorio de trabajo sea la raiz del proyecto.
- Los artefactos binarios estan versionados para facilitar pruebas y reproduccion.
- Si regeneras un modelo, conviene conservar el mismo nombre de archivo o actualizar las referencias en los notebooks.

## Solucion De Problemas

- Si un notebook no encuentra archivos, verifica que estes ejecutandolo desde la raiz del repositorio.
- Si Jupyter no detecta el entorno, reinstala el kernel o activa el entorno virtual antes de abrirlo.
- Si falla la carga de un modelo serializado, revisa la compatibilidad de versiones de la libreria usada para guardarlo.
- Si aparece un error de dependencias, instala manualmente la libreria faltante dentro del mismo entorno virtual.

## Licencia

Este proyecto se distribuye bajo licencia MIT. Revisa el archivo [LICENSE](LICENSE) para ver los terminos completos.

## Creditos

Proyecto desarrollado por Team5RNABI como parte de un trabajo academico enfocado en analitica de datos, aprendizaje automatico y sistemas de recomendacion para transporte y turismo.
