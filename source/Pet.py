# import config
from User import User

class Pet:
    def __init__(self, id: int, name: str, animalGroup: str,
                 breed: str | None, furColor: str | None):
        self._id: int = id

        self.name: str = name
        self.description: str | None = None
        self.age: int | None = None

        self._animalGroup: str = animalGroup
        self.breed: str | None = breed
        self.furColor: str | None = furColor

        self._status: str = 'Rescued'

        self.houseType: str | None = None
        self.coexistsOtherPets: bool = False

        self.applications: List = []
        self._tutor: User | None = None

    @property
    def id(self) -> int:
        return self._id

    @property
    def animalGroup(self) -> str:
        return self._animalGroup

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def setter(self, value) -> None:
        if value in config.STATUS_LIST:
            self.status = value
