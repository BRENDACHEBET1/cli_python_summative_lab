from model import Model

class Task(Model):
    
    def __init__(self, title, status, assigned_to, project):
        super().__init__()
        self.title = title
        self.status = status
        self.assigned_to = assigned_to
        self.project = project

    @property 
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not value.strip():
            raise ValueError("Title cannot be empty")
        self._title =value

    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value):
        allowed = ["Pending", "In Progress", "Completed"]
        if value not in allowed:
            raise ValueError(f"Status must be one of {allowed}")
        self._status = value

        