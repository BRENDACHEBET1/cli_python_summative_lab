

class Task():
    #class atribute
    _id_counter = 1

    def __init__(self, title, status, assigned_to,project):
         # Assign unique ID
        self.id = Task._id_counter
        Task._id_counter += 1

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

    #status property
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

    #json storage
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "project_id": self.project.id if self.project else None,
            "assigned_email": self.assigned_to 
        }

    #distionary to task object
    @classmethod
    def from_dict(cls, data):
        task = cls(
            data["title"],
            data["status"],
            data.get("assigned_email"),
            None
        )
        task.id = data.get("id", task.id)
        if task.id >= cls._id_counter:
            cls._id_counter = task.id + 1

        return task

    # object collection
    @classmethod
    def load_all(cls, data_list):
        return [cls.from_dict(item) for item in data_list]

        
    def __repr__(self):
        return f"Task(id={self.id}, title={self.title}, status={self.status})"



        