from model.person import Person

#Inherits person
class User(Person):
    # Class attribute for auto-incrementing IDs
    _id_counter = 1

    def __init__(self, name, email):
        super().__init__(name, email)

        self.id = User._id_counter
        User._id_counter += 1

        #user can have mulitple projects
        self._projects = [] # relationship- user has projects 

    #getter for projects
    @property
    def projects(self):
        return self._projects

    #Add project to user and check if it exists to prevent duplicates
    def add_project(self, project):
        if project not in self._projects:
            self._projects.append(project)
            
        else:
            print(f"Project '{project.title}' already exists for user {self.name}")

    #Convert object to dictionary for json storage
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "projects": [p.to_dict() for p in self.projects]
        }


    #convert dictionary to user object
    @classmethod
    def from_dict(cls, data):
        user = cls(data["name"], data["email"])
        user.id = data.get("id", user.id)

        if user.id >= cls._id_counter:
            cls._id_counter = user.id + 1

        return user
    
    # Load multiple users from JSON list
    @classmethod
    def load_all(cls, data_list):
        return [cls.from_dict(item) for item in data_list]