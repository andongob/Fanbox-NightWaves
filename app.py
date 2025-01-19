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


'''import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    video_url = request.args.get('url', None)
    return render_template('index.html', video_url=video_url)

if __name__ == '__main__':
    # Usa el puerto especificado por Hugging Face o el puerto 5000 por defecto
    port = int(os.environ.get('PORT', 7860))
    app.run(debug=True, host='0.0.0.0', port=port)
'''

'''
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    video_url = request.args.get('url', None)
    return render_template('index.html', video_url=video_url)

if __name__ == '__main__':
    app.run(debug=True)

'''
