from source.users.user import User

class Adopter(User):
    def __init__(self, id: int, username: str):
        super().__init__(username, id)
        self.age: int | None = None
        self.descripion: str | None = None
        # self.applications: dict[Pet, Application] = {}
        self.allowedPosts.extend(["Forum", "Success Story"])

    def viewApplications(self) -> None:
        pass

