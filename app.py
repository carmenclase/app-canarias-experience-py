from flask import Flask, render_template
from config import get_config

app = Flask(__name__)

# Obtener configuración según el entorno
config = get_config()

@app.route('/')
def index():
    return render_template('index.html', version=config.VERSION)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
