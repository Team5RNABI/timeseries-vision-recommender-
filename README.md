# Sistema Inteligente Integrado para Transporte

Aplicación web desarrollada en **Streamlit** para demostrar un ecosistema de inteligencia artificial aplicado al sector transporte. El proyecto reúne tres capacidades complementarias:

1. Predicción de demanda de transporte.
2. Clasificación de conducción distractiva a partir de imágenes.
3. Recomendación personalizada de destinos turísticos.

La solución está pensada como una demo funcional y educativa, con modelos ya entrenados y artefactos incluidos en el repositorio para facilitar su ejecución local.

## Descripción General

El objetivo del sistema es apoyar decisiones operativas y de experiencia de usuario en una empresa de transporte:

- estimar cuántos asientos podrían venderse en un viaje,
- identificar comportamientos de riesgo del conductor,
- y sugerir destinos relevantes según el historial del usuario.

La interfaz principal centraliza la navegación entre módulos y permite usar cada uno de forma independiente o como parte de una misma experiencia.

## Módulos Disponibles

### Módulo 1: Predicción de Demanda de Transporte

Predice el número estimado de asientos vendidos para un viaje a partir de variables operativas como:

- cupo máximo del vehículo,
- día de la semana,
- mes,
- hora del viaje,
- origen,
- destino,
- tipo de carro,
- método de pago principal.

Este módulo usa una red neuronal implementada en **PyTorch** junto con un preprocesador serializado en `joblib`.

### Módulo 2: Clasificación de Conducción Distractiva

Clasifica imágenes del conductor en cinco categorías:

- `other_activities`
- `safe_driving`
- `talking_phone`
- `texting_phone`
- `turning`

El módulo utiliza un modelo entrenado con **TensorFlow / Keras** y muestra tanto la clase predicha como la distribución de probabilidades.

### Módulo 3: Sistema de Recomendación de Destinos

Genera recomendaciones personalizadas de destinos turísticos basadas en:

- perfil del usuario,
- historial de interacciones,
- preferencias previas,
- y puntuaciones estimadas por el modelo.

El artefacto principal se carga desde un archivo `joblib` que incluye el modelo y las estructuras necesarias para inferencia.

## Tecnologías Utilizadas

- [Streamlit](https://streamlit.io/)
- [PyTorch](https://pytorch.org/)
- [TensorFlow](https://www.tensorflow.org/)
- [NumPy](https://numpy.org/)
- [Pandas](https://pandas.pydata.org/)
- [scikit-learn](https://scikit-learn.org/)
- [Pillow](https://python-pillow.org/)
- [Joblib](https://joblib.readthedocs.io/)

## Estructura del Repositorio

```text
.
├── Home.py
├── app.py
├── pages/
│   ├── Modulo_1_PrediccionDemanda.py
│   ├── Modulo_2_ClasificacionDeImagenes.py
│   └── Modulo_3_SistemasDeRecomendacion.py
├── models/
│   ├── modelo_pytorch1.pth
│   ├── preprocesador1.pkl
│   ├── model_module_2.keras
│   ├── model_module_2.h5
│   └── model_module_3.pkl
├── imagenes_prueba/
├── modelo_pytorch123.pth
├── preprocesador123.pkl
└── requirements.txt
```

## Requisitos

- Python instalado
- Entorno virtual recomendado
- Dependencias listadas en `requirements.txt`

## Instalación

### 1. Crear y activar un entorno virtual

En Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

En macOS / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

## Ejecución

### Opción recomendada: abrir la experiencia completa

```bash
streamlit run Home.py
```

Esto abre la página principal del sistema, desde donde puedes navegar entre los módulos disponibles.

### Ejecución directa por módulo

Si prefieres abrir una funcionalidad específica:

```bash
streamlit run pages/Modulo_1_PrediccionDemanda.py
streamlit run pages/Modulo_2_ClasificacionDeImagenes.py
streamlit run pages/Modulo_3_SistemasDeRecomendacion.py
```

También existe una versión independiente de predicción de demanda en:

```bash
streamlit run app.py
```

## Artefactos Incluidos

El proyecto ya incluye los modelos y preprocesadores necesarios para inferencia:

- `models/modelo_pytorch1.pth`
- `models/preprocesador1.pkl`
- `models/model_module_2.keras`
- `models/model_module_2.h5`
- `models/model_module_3.pkl`
- `modelo_pytorch123.pth`
- `preprocesador123.pkl`

No es necesario reentrenar los modelos para probar la aplicación.

## Notas de Uso

- El Módulo 1 valida que el origen y el destino no sean iguales.
- El Módulo 2 acepta imágenes en formato `jpg`, `jpeg` y `png`.
- El Módulo 3 requiere un `UserID` existente en los datos serializados dentro del modelo.

## Solución de Problemas

- Si la aplicación indica que no encuentra un modelo, verifica que los archivos de `models/` y los artefactos de la raíz estén presentes.
- Si Streamlit no abre automáticamente el navegador, copia la URL local que aparece en consola.
- Si tienes errores de compatibilidad, revisa que la versión de Python sea consistente con las dependencias del entorno.

## Créditos

Proyecto académico orientado a la construcción de una solución integral de IA para transporte, combinando predicción, visión por computador y recomendación.

