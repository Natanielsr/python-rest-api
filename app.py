#!/usr/bin/env python3


from flask import Flask, jsonify, request
from routes.tasks import tasks_bp  # Importando o Blueprint de tarefas
from routes.search import search_bp  # Importando o Blueprint de busca
from routes.lyric import lyric_bp  # Importando o Blueprint de busca

app = Flask(__name__)

# Registrando os Blueprints
app.register_blueprint(tasks_bp)
app.register_blueprint(search_bp)
app.register_blueprint(lyric_bp)

@app.route('/')
def home():
    return "Application Running"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
