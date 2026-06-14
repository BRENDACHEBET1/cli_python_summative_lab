from model.model import Model

class Project(Model):
    
    def __init__(self, title, description,due_date):
        super().__init__()
        self. title = title
        self.description = description
        self.due_date = due_date
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

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "tasks": [t.to_dict() for t in self.tasks]
            
        }

    @classmethod
    def from_dict(cls, data):
        project = cls(
            data["title"],
            data["description"],
            data["due_date"],
           
        )
        project._id = data.get("id", project.id)
        return project

    # collection
    @classmethod
    def load_all(cls, data_list):
        return [cls.from_dict(item) for item in data_list]