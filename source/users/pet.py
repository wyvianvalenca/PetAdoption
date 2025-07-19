from source.users.user import User

STATUS_LIST: list[str] = [
    "Rescued",
    "In treatment",
    "Available for adoption",
    "Adopted"
]

class Pet:
    def __init__(self, 
                 name: str, 
                 pet_type: str,
                 breed: str | None, 
                 fur_color: str | None):
        self.name: str = name
        self.description: str | None = None
        self.age: int | None = None

        self._pet_type: str = pet_type
        self.breed: str | None = breed
        self.fur_color: str | None = fur_color

        self._status: str = 'Rescued'

        self.application_form: dict[str, str | int] = {}

        self.applications: dict[User, int] = {}
        self._tutor: User | None = None

    @property
    def pet_type(self) -> str:
        return self._pet_type

    @property
    def status(self) -> str:
        return self._status.upper()

    @status.setter
    def status(self, value: str) -> None:
        if value in STATUS_LIST:
            self._status = value

    def pet_strings(self) -> list[str]:
        pet_info: list[str] = []

        pet_info.append(f"{self.name.upper()}")
        pet_info.append(f"    > Pet Type: {self.pet_type}")

        if self.breed:
            pet_info.append(f"    > Breed: {self.breed}")

        if self.description:
            pet_info.append(f"    > Desc: {self.description}")

        if self.fur_color:
            pet_info.append(f"    > Fur Color: {self.fur_color}")

        if self.age:
            pet_info.append(f"    > Age: {self.age}")

        pet_info.append(f"    > Status: {self.status}")
        pet_info.append("")

        return pet_info

    def print_pet(self):
        print(f"{self.name.upper()}" + 20*"-",
              f"\n > Desc: {self.description}",
              f"\n > Type: {self.pet_type}",
              f"\n > Breed: {self.breed}",
              f"\n > Fur Color: {self.fur_color}",
              f"\n > Age: {self.age}",
              f"\n > Status: {self.status}"
        )
