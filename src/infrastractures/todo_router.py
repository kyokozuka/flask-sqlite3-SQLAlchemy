from flask import Blueprint
from flask import url_for
from flask import redirect
from flask import request


todo = Blueprint('todo', __name__)

@todo.route('/todo/add', methods=['POST'])
def add():
    name = request.form['name']
    description = request.form['description']
    return {"name": name}