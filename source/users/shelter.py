from source.socials.event import Event
from source.users.user import User
from source.users.pet import Pet, STATUS_LIST

class Shelter(User):
    def __init__(self, id: int, username: str, name: str):
        super().__init__(username, id, name)

        self.user_profile.update({
            'address': None,
            'donation type': None,
            'donation code': None
        })

        self._pet_types: dict[str, list[str]] = {}
        self._pets: list[Pet] = []
        self._events: list[Event] = []
        self.allowed_posts.extend(["Forum", "Educational"])

    @property
    def pet_types(self) -> dict[str, list[str]]:
        return self._pet_types

    def add_pet_type(self, petType: str) -> None:
        self.pet_types[petType] = []

    @property
    def pets(self) -> list[Pet]:
        return self._pets

    def add_pet(self, pet: Pet) -> str:
        if pet.animalGroup in self.pet_types:
            self.pets.append(pet)
            self.pet_types[pet.animalGroup].append(pet.breed)
            return f"[OK] {pet.name} added to {self.name}"
        else:
            return f"[FAIL] {self.name} does not shelters {pet.animalGroup} yet."

    def print_pets(self):
        for pet in self.pets:
            print(f"[{pet.name}] - {pet.animalGroup}, {pet.breed}")

    def add_events(self, name: str, date: str, location: str) -> None:
        new_event = Event(name, date, location, self)
        self._events.append(new_event)

    def print_events(self):
        for event in self._events:
            event.print_event()

    def print_allowed_pets(self) -> None:
        print(f"\n{self.name} shelters the following species: ", end=' ')
        for pet_type in self.pet_types:
            print(pet_type, end=' ')

    def print_user_profile(self) -> None:
        super().print_user_profile()
        self.print_allowed_pets()
