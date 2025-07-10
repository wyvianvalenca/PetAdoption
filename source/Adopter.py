class Adopter(User):
    def __init__(self, username: str, id: int)__:
        super().__init(username, id)
        self.age: int | None = None
        self.descripion: str | None = None
        self.applications: List = []
        self.successStories: List = []
        self.forumPosts: List = []

    def updateProfile(age: int):
        self.age = age

    def updateProfile(description: str):
        self.description = description

    def searchPets():
        pass

    def searchShelters():
        pass

    def searchEvents():
        pass

    def viewFeed():
        pass

    def viewApplications(self):
        for application in self.applications:
            print(f"")

