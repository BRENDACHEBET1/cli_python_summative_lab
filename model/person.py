#user inherits this
class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    #Email getter(encapuslation)
    @property
    def email(self):
        return self._email

    # Email setter with validation
    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Invalid email")
        self._email = value

    def __repr__(self):
        return f"Person(name={self.name}, email={self.email})"