from User import User

class Adopter(User):
    def __init__(self, username: str, id: int):
        super().__init__(username, id)
        self.age: int | None = None
        self.descripion: str | None = None
        self._applications: List = []
        self._successStories: List = []
        self._forumPosts: List = []

    @property
    def applications(self):
        return self._applications

    def searchPets():
        pass

    def searchShelters():
        pass

    def searchEvents():
        pass

    def viewApplications(self):
        for application in self.applications:
            print(f"")
