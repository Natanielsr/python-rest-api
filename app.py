from flask import Flask, jsonify, request
from routes.tasks import tasks_bp  # Importando o Blueprint de tarefas
from routes.search import search_bp  # Importando o Blueprint de busca

app = Flask(__name__)

# Registrando os Blueprints
app.register_blueprint(tasks_bp)
app.register_blueprint(search_bp)

@app.route('/')
def home():
    return "Application Running"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
