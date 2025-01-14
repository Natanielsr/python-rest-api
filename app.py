from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados de exemplo
tasks = [
    {'id': 1, 'title': 'Estudar Python', 'done': False},
    {'id': 2, 'title': 'Criar aplicação REST', 'done': False}
]

# Rota para listar todas as tarefas
@app.route('/')
def home():
    return "Application Running"

# Rota para listar todas as tarefas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# Rota para pegar uma tarefa específica
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Tarefa não encontrada'}), 404
    return jsonify({'task': task})

# Rota para criar uma nova tarefa
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = {
        'id': len(tasks) + 1,
        'title': data['title'],
        'done': data.get('done', False)
    }
    tasks.append(new_task)
    return jsonify({'task': new_task}), 201

# Rota para atualizar uma tarefa
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Tarefa não encontrada'}), 404
    
    data = request.get_json()
    task['title'] = data.get('title', task['title'])
    task['done'] = data.get('done', task['done'])
    
    return jsonify({'task': task})

# Rota para deletar uma tarefa
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'message': 'Tarefa deletada'})

if __name__ == '__main__':
    app.run(debug=True)
