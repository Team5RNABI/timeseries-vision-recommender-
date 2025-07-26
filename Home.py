import streamlit as st

st.set_page_config(
    page_title="Sistema Inteligente de Transporte",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Sistema Inteligente Integrado para Transporte")

st.markdown("""
Bienvenido al sistema inteligente de transporte, una herramienta desarrollada con aprendizaje profundo para mejorar **la eficiencia operativa**, **la seguridad vial** y **la experiencia del usuario** en una empresa de transporte.
""")

st.markdown("""
Este sistema se compone de tres módulos principales:
- 📈 **Predicción de Demanda de Transporte**
- 📷 **Clasificación de Conducción Distractiva**
- 🎯 **Sistema de Recomendación de Destinos de Viaje**
""")

st.markdown("---")

# Explicación de cada módulo
with st.expander("📈 Módulo 1: Predicción de Demanda de Transporte"):
    st.markdown("""
Este módulo utiliza modelos de series de tiempo para anticipar la demanda de transporte en rutas específicas durante los próximos 30 días. Esto permite planificar mejor los recursos, como personal y vehículos.
- Analiza patrones históricos.
- Identifica estacionalidades y tendencias.
- Optimiza la planeación operativa.
""")

with st.expander("📷 Módulo 2: Clasificación de Conducción Distractiva"):
    st.markdown("""
Este módulo utiliza imágenes para identificar comportamientos distractores en conductores, como el uso del celular o la somnolencia. Así se mejora la seguridad vial en la operación de transporte.
- Clasifica imágenes en cinco categorías.
- Detecta riesgos como uso del teléfono.
- Genera alertas de conducción insegura.
""")

with st.expander("🎯 Módulo 3: Sistema de Recomendación de Destinos de Viaje"):
    st.markdown("""
Este módulo recomienda destinos de viaje personalizados a los usuarios, utilizando su historial de viajes y preferencias pasadas. Aumenta la satisfacción del cliente y la fidelización.
- Basado en interacciones previas.
- Aprende de los hábitos de cada usuario.
- Sugiere rutas relevantes y atractivas.
""")

st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    st.link_button("🎥 ¿Cómo usar?", "https://www.youtube.com/watch?v=tu_video_de_ejemplo")
with col2:
    st.link_button("📄 Reporte Técnico", "https://medium.com/@dcastrot/aplicaciones-en-sistemas-de-recomendación-e-imágenes-c79df14e1d83")
st.markdown("---")

# Navegación entre módulos
st.markdown("## 🔍 Ir a un módulo")
col1, col2, col3 = st.columns(3)

with col1:
    st.link_button("🚌 Módulo 1", "https://appdemandatransporte-txpxeoaqe7t6elvabs9lpp.streamlit.app")

with col2:
    st.page_link("pages/Modulo_2_ClasificacionDeImagenes.py", label="🚦 Módulo 2", icon="📷")

with col3:
    st.page_link("pages/Modulo_3_SistemasDeRecomendacion.py", label="🧭 Módulo 3", icon="🎯")

st.markdown("---")

# Footer o mensaje de cierre
st.info("Este sistema ha sido desarrollado como una solución integral de inteligencia artificial para empresas del sector transporte. ¡Explora cada módulo y mejora tu operación!")
