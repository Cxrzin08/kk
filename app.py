from flask import Flask, render_template, jsonify
import time

app = Flask(__name__)

images = [
    "agradecimento1.jpg",
    "agradecimento2.jpg",
    "agradecimento3.jpg",
    "agradecimento4.jpg",
    "agradecimento5.jpg"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/next_image')
def next_image():
    return jsonify(image=images[int(time.time()) % len(images)])

if __name__ == '__main__':
    app.run(debug=True)