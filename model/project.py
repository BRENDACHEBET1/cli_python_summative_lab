

class Project():
    _id_counter = 1

    def __init__(self, title, description,due_date):
        #Unique id
        self.id = Project._id_counter
        Project._id_counter += 1

        self.title = title
        self.description = description
        self.due_date = due_date
        #Each project has multiple tasks
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
        if task not in self._tasks:
            self._tasks.append(task)
           
        else:
            print(f"Task '{task.title}' already exists in project '{self.title}'")

    # Convert Project → dictionary for saving JSON
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "tasks": [t.to_dict() for t in self.tasks]
            
        }

     # Convert dictionary → Project object
    @classmethod
    def from_dict(cls, data):
        project = cls(
            data["title"],
            data["description"],
            data["due_date"],
           
        )
        project.id = data.get("id", project.id)
        if project.id >= cls._id_counter:
            cls._id_counter = project.id + 1

        return project

    # collection
    @classmethod
    def load_all(cls, data_list):
        return [cls.from_dict(item) for item in data_list]