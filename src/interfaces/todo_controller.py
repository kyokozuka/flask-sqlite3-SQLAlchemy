from src.usecases.todo_interactor import TodoInteractor

class TodoController:
    def __init__(self):
        self.todo = TodoInteractor()
    
    def add(self):
        result = self.todo.add()
        return result
    
    def find(self):
        result = self.todo.find()
        return result