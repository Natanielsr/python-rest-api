#!/usr/bin/env python3
import os

from flask import Flask
from routes.tasks import tasks_bp  # Importando o Blueprint de tarefas
from routes.search import search_bp  # Importando o Blueprint de busca
from routes.tester import tester_bp  # Importando o Blueprint de testes
from routes.lyric import lyric_bp  # Importando o Blueprint de letras
from routes.slides import slides_bp  # Importando o Blueprint de slides

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Registrando os Blueprints
app.register_blueprint(tasks_bp)
app.register_blueprint(search_bp)
app.register_blueprint(lyric_bp)
app.register_blueprint(tester_bp)
app.register_blueprint(slides_bp)

@app.route('/')
def home():
    return "Application Running"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
