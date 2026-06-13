from model import Model

class User(Model):
    def __init__(self, name, email):
        super().__init__()
        self.name = name
        self.email = name

    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value