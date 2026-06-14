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

    def add_task(self, task):
        self._tasks.append(task)

    # ---------------- JSON ----------------
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "user_email": self.user.email if self.user else None
        }

    @classmethod
    def from_dict(cls, data):
        project = cls(
            data["title"],
            data["description"],
            data["due_date"],
            None  # user assigned in main.py
        )
        project._id = data.get("id", project.id)
        return project

    # collection
    @classmethod
    def load_all(cls, data_list):
        return [cls.from_dict(item) for item in data_list]