from source.queries.search_pet import search_pets
from source.socials import post
from source.socials.feed import Feed
from source.users.accounts import Accounts
from source.users.adopter import Adopter
from source.users.pet import Pet
from source.users.shelter import Shelter
from source.users.user import User

""" GLOBAL VARIABLES """

accounts = Accounts()
feed = Feed()

""" MENU'S OPTIONS AND FORMATTER """

DIVIDER = "\n" + ("=" * 80) + "\n"

INPUT_MESSAGE = "> Choose an Option: "

WELCOME_OPTIONS = [
    "[1] - Access as Adopter",
    "[2] - Access as Shelter",
    "[q] - Quit"
]

ACCESS_OPTIONS = [
    "[1] - Login",
    "[2] - Create Account",
    "[b] - Return to Welcome Page"
]

SHELTER_OPTIONS = [
    "[1] - Update Profile",
    "[2] - Create Events",
    "[3] - Add Pet Type",
    "[4] - Register New Pet",
    "[4a] - Update Pet",
    "[5] - View Adoption Application (WIP)",
    "[6] - Create Post",
    "[7] - View Social Feed",
    "[b] - Return to Welcome Page"
]

ADOPTER_OPTIONS = [
    "[1] - Update Profile",
    "[2] - View Events",
    "[3] - View Shelters",
    "[4] - View Pets (WIP)",
    "[5] - View Adoption Applications (WIP)",
    "[6] - Create Post",
    "[7] - View Social Feed",
    "[b] - Return to main menu"
]

def formatted_menu(menu_name: str, menu_options: list[str]) -> str:
    left_padding: int  = 2
    right_padding: int = 5

    left_up_corner: str    = "┌"
    left_down_corner: str  = "└"
    right_up_corner: str   = "┐"
    right_down_corner: str = "┘"
    horizontal_line: str   = "─"
    vertical_line: str     = "│"

    biggest_string = 0

    for option in menu_options:
        if len(option) > biggest_string:
            biggest_string = len(option)

    box_width = 1 + left_padding + biggest_string + right_padding + 1

    empty_line = vertical_line + ((box_width - 2) * " ") + vertical_line + "\n"

    # header
    header:str = left_up_corner + ((2 + left_padding) * horizontal_line) + " " + menu_name.upper() + " "
    current_header_width = len(header)
    header = header + ((box_width - current_header_width - 1) * horizontal_line) + right_up_corner + "\n"

    # body
    body = ""
    for opt in menu_options:
        line = vertical_line + (left_padding * " ") + opt
        current_width = len(line)
        line = line + ((box_width - current_width - 1) * " ") + vertical_line + "\n"

        body = body + line

    # footer
    footer = left_down_corner + ((box_width - 2) * horizontal_line) + right_down_corner + "\n"

    return "\n" + header + empty_line + body + empty_line + footer

"""INITIAL DATA"""

ad1 = accounts.create_user("Adopter", "wyvianvalenca", "Wyvian Valença")
ad2 = accounts.create_user("Adopter", "ycarosales", "ycaro SALES")

sh1 = accounts.create_user("Shelter", "csf", "Casa São Francisco")
sh2 = accounts.create_user("Shelter", "reptile_house", "Reptile's House")

print(sh1.update_profile({
    "description": "🏥 Veterinária Popular",
    "address": "R. dos Bandeirantes, 504 - Farol, Maceió - AL, 57051-120",
    "donation type": "PIX CNPJ",
    "donation code": "12.234.456/0001-01"
}))

print(sh2.update_profile({
    "description": "Amamos repteis!!!!",
    "address": "R. dos Repteis, 111 - Fatol, Maceió"
}))

pet1 = Pet("Becky", "Dog", "Chow Chow", "Orange")
pet2 = Pet("Tomas", "Cat", None, "Black")
pet3 = Pet("Thor", "Dog", "Golden Retriever", "White")
pet4 = Pet("Shiro", "Dog", None, "White")
pet5 = Pet("Jack", "Turtle", None, None)

sh1.add_pet_type("Cat")
sh1.add_pet_type("Dog")
sh1.add_pet(pet1)
sh1.add_pet(pet2)
sh1.add_pet(pet3)
sh1.add_pet(pet4)

sh2.add_pet_type("Turtle")
sh2.add_pet(pet5)


sh1.add_events("Fundraising!", "12/08/2025", "Praça Centenário - Farol, Maceió")
sh1.add_events("Adoption Fair", "10/10/2025", "UFAL, Praça da Paz - Cidade Universitária, Maceió")

sh2.add_events("Turle Festival", "01/02/2026", "Praça Dois Leões - Jaraguá, Maceió")

""" TEXT UI FUNCTION """

# USER'S TEXT UI FUNCTIONS

def wip() -> None:
    print("We're still working on this option!")
    return None

def update_user_profile(user: User) -> None:
    print("\nLet's Update your profile!", 
          "Here's your current information:")

    user.print_user_profile()

    print("If you don't want to update something, just leave it blank.\n")

    new_profile: dict[str, str] = {}
    for field in user.user_profile.keys():
        new_data = input(f"New {field.title()}: ")
        if new_data:
            new_profile[field] = new_data

    print(user.update_profile(new_profile))

    print("\nGreat! Here's your new profile!\n")

    user.print_user_profile()

def create_post(user: User) -> None:
    print("\nLet's add a post! First, choose the type.")
    print(formatted_menu("post type", user.allowed_posts[1:]))

    post_type = input("> Choose a type: ")
    while post_type not in user.allowed_posts:
        print("\nInvalid Option. Try Again.")
        post_type = input("> Choose a type: ")


    print(f"\nLet's write a {post_type}! Please type your post's info\n")
    title = input("Title: ")
    content = input("Content: ")

    if feed.create_post(user, post_type, title, content):
        print("[OK] Post created")
    else:
        print("[FAIL] You can't post that.")


# SHELTER'S TEXT UI FUNCTIONS

def create_event(user: Shelter) -> None:
    print("\nLet's create an event!")
    name = input("Name: ")
    date = input("Date: ")
    location = input("Location: ")

    user.add_events(name, date, location)
    print("[OK] Event created!")

    return None

def add_pet_type(user: Shelter) -> None:
    petType = input("\nPet Type: ")
    user.add_pet_type(petType)

    return None

def register_new_pet(user: Shelter) -> None:
    print("\n Let's register a new pet! Type it's info: \n")
    pet_name = input("Name: ")
    pet_type = input("Type (species): ")
    pet_breed = input("Breed: ")
    pet_furColor = input("Fur Color: ")

    pet = Pet(pet_name, pet_type, pet_breed, pet_furColor)

    print(user.add_pet(pet))

    return None

def find_pet(name: str, shelters_pets: list[Pet]) -> Pet | None:
    for pet in shelters_pets:
        if name == pet.name:
            return pet

    return None

def update_pet(pets: list[Pet]) -> None:
    print("\nLet's update a pet!",
          "First, let's find the pet you want to update.")
    name = input("Pet Name: ")
    pet = find_pet(name, pets)

    while pet is None:
        print("Pet Not Found! Try again or type q to quit.")
        name = input("Pet Name: ")

        if name == "q":
            return

        pet = find_pet(name, pets)

    print("If you don't want to update something, just leave it blank")

    new_name = input("New Name: ")
    if new_name:
        pet.name = new_name

    new_description = input("New Description: ")
    if new_description:
        pet.description = new_description

    new_age = input("New Age: ")
    if new_age:
        pet.age = int(new_age)

    new_breed = input("New Breed: ")
    if new_breed:
        pet.breed = new_breed

    new_fur = input("New Fur Color: ")
    if new_fur:
        pet.fur_color = new_fur

    print(f"\nGreat! Here's {pet.name}'s new profile!")
    pet.print_pet()

    return

SHELTER_MENU_FUNCTIONS = [
    ("1", "Update Profile", update_user_profile),
    ("2", "Create Events", create_event),
    ("3", "Add Pet Type", add_pet_type),
    ("4", "Register New Pet", register_new_pet),
    ("4a", "Update Pet Profile", update_pet),
    ("5", "[WIP] View Adoption Applications", wip),
    ("6", "Create Post", create_post),
    ("7", "Open Social Feed", feed.view_feed)
]

def shelter_menu(user: Shelter) -> None:
    print(DIVIDER)
    print(f"\nYou're logged in, {user.name}!\n")

    while True:
        print(formatted_menu("Adopter's menu", ADOPTER_OPTIONS))

        response = input(INPUT_MESSAGE)
        print()

        if response == "b":
            return

        elif response == "1":
            update_user_profile(user)

        elif response == "2":
            create_event(user)

        elif response == "3":
            add_pet_type(user)

        elif response == "4":
            register_new_pet(user)

        elif response == "4a":
            update_pet(user.pets)

        elif response == "5":
            wip()

        elif response == "6":
            create_post(user)

        elif response == "7":
            feed.view_feed()

        else:
            print("\nInvalid Option.")

# ADOPTER'S TEXT UI FUNCTIONS

def print_all_events() -> None:
    all_events: list[str] = []
    for shelter in accounts.users["Shelter"].values():
        shelter_events = []
        for event in shelter.events:
            shelter_events.append(f"> {event.name.upper()} by {event.shelter.name.title()}")
            shelter_events.append(f"     - Location: {event.location}")
            shelter_events.append(f"     - Date: {event.date}")
            shelter_events.append("")

        all_events.extend(shelter_events)

    print(formatted_menu("events", all_events))

    _ = input("Press any key to return to adopter's menu.")

    return None

def print_all_shelters() -> None:
    all_shelters: list[str] = []
    for shelter in accounts.users["Shelter"].values():
        shelter_info = []

        shelter_info.append(f"> {shelter.name.upper()}")

        for field, info in shelter.user_profile.items():
            if info:
                shelter_info.append(f"     - {field.title()}: {info}")

        shelter_info.append("")

        all_shelters.extend(shelter_info)

    print(formatted_menu("shelter", all_shelters))

    return None


ADOPTER_MENU_FUNCTIONS = [
    ("1", "Update Profile", update_user_profile)
]

def adopter_menu(user: Adopter) -> None:
    print(DIVIDER)
    print(f"\nYou're logged in, {user.name}!\n")

    while True:
        print(formatted_menu("Adopter's menu", ADOPTER_OPTIONS))

        response = input(INPUT_MESSAGE)
        print()

        if response == "b":
            return None

        elif response == "1":
            update_user_profile(user)

        elif response == "2":
            print_all_events()

        elif response == "3":
            print_all_shelters()

        elif response == "4":
            print("Let's find a pet! First, choose your filter!")
            print("If you don't want to filter, leave it blank")

            shelter = input("Type a Shelter: ")
            animal_group = input("Type a Animal Group: ")
            breed = input("Type a breed: ")
            color = input("Type a Fur Color: ")
            age_min = int(input("Type a minimal age: "))
            age_max = int(input("Type a maximal age: "))

            filters = { }
            filters['types'] = [animal_group]
            filters['breeds'] = [breed]
            filters['colors'] = [color]
            filters['ageRange'] = [age_max]

            pets = search_pets(users, [shelter], filters)

            for pet in pets:
                pet.print_pet()

        elif response == "5":
            wip()

        elif response == "6":
            create_post(user)

        elif response == "7":
            feed.view_feed()

        else:
            print("\nInvalid Option.\n")



def access(type: str) -> User | None:
    print(DIVIDER)
    print(f"\nYou chose {type.title()}! That's so cool!\n")

    while True:
        print(formatted_menu("Access Menu", ACCESS_OPTIONS))

        response = input(INPUT_MESSAGE)
        print()

        if response == "b":
            return None

        elif response == "1": #login
            username = input("Username: ")
            user = accounts.login(type, username)
            return user

        elif response == "2": #creat account
            username = input("Username: ")
            name = input("Name: ")
            user = accounts.create_user(type, username, name)
            return user

        else:
            print("Invalid option for access.\n")


def welcome():
    print(DIVIDER)
    print("\nWelcome!\n")
    
    while True:
        print(formatted_menu("Pet App", WELCOME_OPTIONS))

        response = input(INPUT_MESSAGE)
        print()

        if response == '1':
            adopter = access("Adopter")

            if adopter:
                adopter_menu(adopter)
            else: 
                print("Access Failed! Try Again")

        elif response == '2':
            shelter = access("Shelter")

            if shelter:
                shelter_menu(shelter)
            else: 
                print("Access Failed! Try Again")

        elif response == "q":
            break

        else:
            print("Invalid option.")

    print("Goodbye!")


if __name__ == "__main__":
    welcome()
