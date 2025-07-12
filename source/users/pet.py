from source.users.user import User

STATUS_LIST: list[str] = [
    "Rescued",
    "In treatment",
    "Available for adoption",
    "Adopted"
]

class Pet:
    def __init__(self, name: str, animalGroup: str,
                 breed: str | None, furColor: str | None):
        self.name: str = name
        self.description: str | None = None
        self.age: int | None = None

        self._animalGroup: str = animalGroup
        self.breed: str | None = breed
        self.furColor: str | None = furColor
        self.age: int | None = None

        self._status: str = 'Rescued'

        self.houseType: str | None = None
        self.coexistsOtherPets: bool = False

        self.applications: dict[User, int] = {}
        self._tutor: User | None = None

    @property
    def animalGroup(self) -> str:
        return self._animalGroup

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def setter(self, value: str) -> None:
        if value in STATUS_LIST:
            self._status = value
