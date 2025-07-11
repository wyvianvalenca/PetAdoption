class User:
    def __init__(self, username: str, id: int):
        self._username: str = username
        self._id: int = id

    @property username(self):
        return self._username

    @property id(self):
        return self._id
