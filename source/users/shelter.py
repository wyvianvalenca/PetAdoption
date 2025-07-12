from source.users.user import User
from source.users.pet import Pet, STATUS_LIST

class Shelter(User):
    def __init__(self, id: int, username: str, name: str, address: str,
                 description: str | None):
        super().__init__(username, id)

        self.name: str = name
        self.address: str = address
        self.description: str | None = description

        self._pixKeyType: str | None = None
        self._pixKeyValue: str | None = None

        self._petTypes: dict[str, list[str]] = {}

        self._pets: list[Pet] = []
        self._events: list = []

        self.allowedPosts.extend(["Forum", "Educational"])

    @property
    def petTypes(self) -> dict[str, list[str]]:
        return self._petTypes

    def addPetTypes(self, petType: str) -> None:
        self.petTypes[petType] = []

    @property
    def pets(self) -> list[Pet]:
        return self._pets

    def addPet(self, pet: Pet) -> str:
        if pet.animalGroup in self.petTypes:
            self.pets.append(pet)
            self.petTypes[pet.animalGroup].append(pet.breed)
            return f"[OK] {pet.name} added to {self.name}"
        else:
            return f"[FAIL] {self.name} does not shelters {pet.animalGroup} yet."

    def showPets(self):
        for pet in self.pets:
            print(f"[{pet.name}] - {pet.animalGroup}, {pet.breed}")

    # events methods

    def showShelter(self):
        pass
