from src.entities.todo_domain import TodoDomain


class TodoInteractor:
    
    def __init__(self):
        pass
    
    def add(self):
        return "todo add"
    
    def find(self):
        return TodoDomain(name="Sample1", description="初めての投稿")
        