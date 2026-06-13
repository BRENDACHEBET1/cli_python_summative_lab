from model import Model

class Project(Model):
    
    def __init__(self, title, description,due_date):
        super().__init__()
        self. title = title
        self.description = description
        self.due_date = due_date


    @property
    def title(self):
        return self.title
    
    @title.setter
    def title(self, value):
        if not value.strip():
            raise ValueError("Title cannot be empty")
        self.title = value
    