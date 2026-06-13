class Model:
    _id_counter = 1

    def __init__(self):
        cls = self.__class__
        self._id = cls._id_counter
        cls._id_counter += 1

    @property
    def id(self):
        return self._id
    
    def __repr__(self):
        return f"{self.__class__.name__}(id={self.id})"
