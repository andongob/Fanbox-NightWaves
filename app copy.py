import streamlit as st
from pathlib import Path

# Configuración inicial de la página
st.set_page_config(
    page_title="Reproductor de Video",
    layout="wide"
)

# Título
st.title("Reproductor de Video Local")


# Ruta del video local
video_path = Path("static/nightwaves.mp4")

# Verificar si el archivo existe
if video_path.exists():
    with open(video_path, "rb") as video_file:
        video_bytes = video_file.read()
        st.video(video_bytes, format="video/mp4")
else:
    st.error("El archivo de video no se encontró. Por favor, verifica la ruta.")
