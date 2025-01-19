from flask import Flask, render_template, request
import os

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
