from model import Model

class Task(Model):
    super().__init__()
    def __init__(self, title, status, assigned_to):
        self.title = title
        self.status = status
        self.assigned_to = assigned_to

    @property 
    def title(self):
        return self.title
    
    @title.setter
    def title(self, value):
        if not value.strip():
            raise ValueError("Title cannot be empty")
        self.title =value

    def status(self):
        return self.status
    
    def assigned_to(self):
        return self.assigned_to

        