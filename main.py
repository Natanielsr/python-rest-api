#!/usr/bin/env python3
import os
import sys
from dotenv import load_dotenv
from flask import Flask, send_from_directory
from routes.tasks import tasks_bp  # Importando o Blueprint de tarefas
from routes.search import search_bp  # Importando o Blueprint de busca
from routes.tester import tester_bp  # Importando o Blueprint de testes
from routes.lyric import lyric_bp  # Importando o Blueprint de letras
from routes.slides import slides_bp  # Importando o Blueprint de slides
from utils import resource_path

import threading, webbrowser

from flask_cors import CORS

static_folder_path = resource_path("web-build")

app = Flask(
    __name__,
    static_folder=static_folder_path,
    static_url_path=""
    )

CORS(app)

# Registrando os Blueprints
app.register_blueprint(tasks_bp)
app.register_blueprint(search_bp)
app.register_blueprint(lyric_bp)
app.register_blueprint(tester_bp)
app.register_blueprint(slides_bp)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(app.static_folder, path)


def open_browser():
    webbrowser.open("http://127.0.0.1:9170")



load_dotenv(resource_path(".env"))

if __name__ == '__main__':
    print(f"Current execution directory: {os.getcwd()}")
    print(f"Icon path: {resource_path('images/icon.png')}")
    print(f"Icon found? {os.path.exists(resource_path('images/icon.png'))}")

    threading.Timer(1, open_browser).start()
    port = int(os.environ.get("PORT", 9170))
    app.run(host="127.0.0.1", port=9170)
