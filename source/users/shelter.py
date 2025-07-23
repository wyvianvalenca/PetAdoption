from source.socials.event import Event
from source.users.user import User
from source.users.pet import Pet, STATUS_SEQUENCE

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
        if pet.pet_type in self.pet_types:
            if pet.name not in [pet.name for pet in self.pets]:
                self.pets.append(pet)
                self.pet_types[pet.pet_type].append(pet.breed)
                return f"[OK] {pet.name} added to {self.name}"
            else:
                return f"[FAIL] '{pet.name}' already registered."
        else:
            return f"[FAIL] {self.name} does not shelters {pet.pet_type} yet."

    def print_pets(self):
        for pet in self.pets:
            print(f"[{pet.name}] - {pet.pet_type}, {pet.breed}")

    @property
    def events(self) -> list[Event]:
        return self._events

    def add_events(self, name: str, date: str, location: str) -> None:
        new_event = Event(name, date, location, self)
        self.events.append(new_event)

    def print_events(self):
        for event in self._events:
            event.print_event()

    def print_allowed_pets(self) -> None:
        print(f"\n{self.name} shelters the following species: ", end=' ')
        for pet_type in self.pet_types:
            print(pet_type, end=', ')
        print(".")

    def applications_list(self) -> list[str]:
        all_apps: list[str] = []
        for pet in self.pets:
            for application in pet.applications:
                all_apps.extend(application.form_list())
                all_apps.append("-" * 50)
                all_apps.append("")

        return all_apps

    def print_user_profile(self) -> None:
        super().print_user_profile()
        self.print_allowed_pets()
