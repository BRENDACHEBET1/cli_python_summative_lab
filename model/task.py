from model.model import Model

class Task(Model):
    
    def __init__(self, title, status, assigned_to,project):
        super().__init__()
        self.title = title
        self.status = status
        self.assigned_to = assigned_to
        self.project = project

    #title property
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
        allowed = ["Pending", "In progress", "Completed"]
        if value not in allowed:
            raise ValueError(f"Status must be one of {allowed}")
        self._status =  value

    
    @property
    def assigned_to(self):
        return self._assigned_to
    
    @assigned_to.setter
    def assigned_to(self, value):
        self._assigned_to = value

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "project_id": self.project.id if self.project else None,
            "assigned_email": self.assigned_to.email if self.assigned_to else None
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(
            data["title"],
            data["status"],
            None,
            None
        )
        task._id = data.get("id", task.id)
        return task

    # object collection
    @classmethod
    def load_all(cls, data_list):
        return [cls.from_dict(item) for item in data_list]

        