class User:
    def __init__(self, username: str, id: int, name: str):
        self._username: str = username
        self._id: int = id
        self._name: str = name
        self._user_profile: dict[str, str | int | None] = {
            'description': None
        }

        self.posts: dict[str, 'Post'] = {}

        self.allowed_posts: list[str] = ["comments"]

    @property
    def username(self) -> str:
        return self._username

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self.name = name.title()

    @property
    def user_profile(self) -> dict[str, str | int | None]:
        return self._user_profile

    def update_profile(self, new_data: dict[str, str]) -> str:
        log = "The following fields were updated:"
        for field, data in new_data.items():
            if data:
                self.user_profile[field] = data
                log += f"\n {field}"
        return log

    def print_user_profile(self) -> None:
        print(f"{self.name.upper()}")
        for field, data in self.user_profile.items():
            print(f"> {field.title()}: {data}")
