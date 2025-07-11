class User:
    def __init__(self, username: str, id: int):
        self._username: str = username
        self._id: int = id

    @property
    def username(self) -> str:
        return self._username

    @property
    def id(self) -> int:
        return self._id
