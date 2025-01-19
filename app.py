from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    video_url = request.args.get('url', None)
    return render_template('index.html', video_url=video_url)

if __name__ == '__main__':
    app.run(debug=True)
