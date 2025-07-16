class User:
    def __init__(self, username: str, id: int):
        self._username: str = username
        self._id: int = id
        self.posts: dict[str, 'Post'] = {}
        self.allowedPosts: list[str] = ["comments"]

    @property
    def username(self) -> str:
        return self._username

    @property
    def id(self) -> int:
        return self._id

    def viewPosts(self) -> None:
        pass
