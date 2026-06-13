from model.model import Model

class User(Model):
    def __init__(self, name, email):
        super().__init__()
        self.name = name
        self.email = email
        self._projects = [] # relationship- user has projects 


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value


    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Invalid email")
        self._email = value


    @property
    def projects(self):
        return self._projects

    def add_project(self, project):
        self._projects.append(project)