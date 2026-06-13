from model.model import Model

class Project(Model):
    
    def __init__(self, title, description,due_date, user):
        super().__init__()
        self. title = title
        self.description = description
        self.due_date = due_date
        self.user = user
        self._tasks = []

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not value.strip():
            raise ValueError("Title cannot be empty")
        self._title = value
    
    
    @property
    def tasks(self):
        return self._tasks

    def add_task(self, task):
        self._tasks.append(task)