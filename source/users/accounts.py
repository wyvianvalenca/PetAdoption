from source.users.user import User
from source.users.adopter import Adopter
from source.users.shelter import Shelter

class Accounts:
    def __init__(self):
        self.adopters_available_id: int = 0
        self.shelters_available_id: int = 0

        self.users: dict[str, dict[str, Shelter | Adopter]] = {
            "Adopter": {},
            "Shelter": {}
        }

    # LOGIN / SIGNUP

    def create_user(self, type: str, username: str, name: str, 
                    address: str | None, description: str | None
                    ) -> User | None:
        if username in self.users[type]:
            return None

        user: User

        if type == "Adopter":
            user = Adopter(self.adopters_available_id, username, name)
            self.adopters_available_id += 1

        elif type == "Shelter":
            user = Shelter(self.shelters_available_id, username, name,
                           address, description)
            self.shelters_available_id += 1

        self.users[type][user.username] = user
        return user

    def login(self, type: str, username: str) -> User | None:
        if username in self.users[type]:
            return self.users[type][username]
        else:
            return None
