from typing import List

from User import User
from Pet import Pet

class Shelter(User):
    def __init__(self, username: str, id: int, name: str, address: str,
                 description: str | None):
        super().__init__(username, id)
        
        self.name: str = name
        self.address: str = address
        self.description: str | None = description

        self._pixKeyType: str | None = None
        self._pixKeyValue: str | None = None

        self._petTypes: dict[str:List[str]] = {}
        
        self._pets: List[Pet] = []
        self._events: List = []

    @property
    def petTypes(self) -> dict[str:List[str]]:
        return self._petTypes

    def addPetTypes(self, petType: str) -> None:
        self.petTypes[petType] = []

    @property
    def pets(self) -> List[Pet]:
        return self._pets

    def addPet(self, pet: Pet) -> str:
        if pet.animalGroup in self.petTypes:
            self.pets.append(pet)
            self.petTypes[pet.animalGroup].append(pet.breed)
            return f"[OK] {pet.name} added to {self.name}"
        else:
            return f"[FAIL] {self.name} does not accept {pet.animalGroup} yet."

    def showPets(self):
        for pet in self.pets:
            print(f"[{pet.id}] - {pet.name}, {pet.animalGroup}, {pet.breed}")
    
    # events methods

    def showShelter(self):
        pass
