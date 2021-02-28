from flask import Flask
from flask import render_template

from src.interfaces.todo_controller import TodoController
from src.infrastractures.todo_router import todo


todo_controller = TodoController()
app = Flask(__name__, static_folder='../statics', template_folder='../templates')
app.secret_key = 'jdkajfewjfofl'
app.register_blueprint(todo)

@app.route('/')
def index():
    data = todo_controller.find()
    return render_template('index.html', data=data)

@app.route('/add_page', methods=["GET"])
def add_page():
    return render_template('/todo/addPage.html')

@app.route('/description_page', methods=["GET"])
def description_page():
    return render_template('/todo/descriptionPage.html')
