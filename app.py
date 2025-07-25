from source.queries.search_pet import search_pets
from source.socials import post
from source.socials.feed import Feed
from source.users.accounts import Accounts
from source.users.adopter import Adopter
from source.users.pet import Pet
from source.users.pet import STATUS_SEQUENCE
from source.users.shelter import Shelter
from source.users.user import User

""" GLOBAL VARIABLES """

accounts = Accounts()
feed = Feed()

""" OPTIONS AND FORMATTER """

DIVIDER = "\n" + ("=" * 80) + "\n"

SMALL_DIVIDER = ("-" * 60)

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
    "[4a] - Update Pet's Profile",
    "[4b] - Add question to Pet's Application",
    "[5] - View Adoption Application",
    "[6] - Create Post",
    "[7] - ViewSocial Feed",
    "[b] - Return to Welcome Page"
]

ADOPTER_OPTIONS = [
    "[1] - Update Profile",
    "[2] - View Events",
    "[3] - View Shelters",
    "[4] - View Pets",
    "[5] - View Adoption Applications",
    "[6] - Create Post",
    "[7] - View Social Feed",
    "[b] - Return to Welcome Page"
]

def boxed_list(menu_name: str, menu_options: list[str]) -> str:
    left_padding: int  = 2
    right_padding: int = 5

    margin_left = "  "

    left_up_corner: str    = "╭"
    left_down_corner: str  = "╰"
    right_up_corner: str   = "╮"
    right_down_corner: str = "╯"
    horizontal_line: str   = "─"
    vertical_line: str     = "│"

    biggest_string = 0

    for option in menu_options:
        if len(option) > biggest_string:
            biggest_string = len(option)

    box_width = 1 + left_padding + biggest_string + right_padding + 1

    # header
    header:str = left_up_corner + ((2 + left_padding) * horizontal_line) + " " + menu_name.upper() + " "
    current_header_width = len(header)
    header = header + ((box_width - current_header_width - 1) * horizontal_line) + right_up_corner + "\n"
    header = margin_left + header

    if len(header) - 3 > box_width:
        box_width = len(header) - 3

    # empty line for spacing
    empty_line = margin_left + vertical_line + ((box_width - 2) * " ") + vertical_line + "\n"

    # body
    body = ""
    for opt in menu_options:
        line = vertical_line + (left_padding * " ") + opt
        current_width = len(line)
        line = line + ((box_width - current_width - 1) * " ") + vertical_line + "\n"
        line = margin_left + line

        body = body + line

    # footer
    footer = margin_left + left_down_corner + ((box_width - 2) * horizontal_line) + right_down_corner

    return "\n" + header + empty_line + body + empty_line + footer + "\n"

"""INITIAL DATA"""

ad1 = accounts.create_user("Adopter", "wyvianvalenca", "Wyvian Valença")
ad2 = accounts.create_user("Adopter", "ycarosales", "ycaro SALES")

sh1 = accounts.create_user("Shelter", "csf", "Casa São Francisco")
sh2 = accounts.create_user("Shelter", "reptile_house", "Reptile's House")

print(sh1.update_profile({
    "description": "Veterinária Popular",
    "address": "R. dos Bandeirantes, 504 - Farol, Maceió - AL, 57051-120",
    "donation type": "PIX CNPJ",
    "donation code": "12.234.456/0001-01"
}))

print(sh2.update_profile({
    "description": "Amamos repteis!!!!",
    "address": "R. dos Repteis, 111 - Fatol, Maceió"
}))

pet1 = Pet("Becky", "Dog", "Chow Chow", "Orange")
pet1.update_status()
pet1.update_status()
_ = pet1.add_question("How many walks can you take her on everyday?", 
                  ["0", "1", "2 or more"],
                  "2 or more")
_ = pet1.add_question("Can you train her?",
                       ["I don't know how, but will learn",
                        "I don't have time",
                        "Yes"],
                       "Yes")

_ = pet1.apply_to_adopt(ad1, {
    "How many walks can you take her on everyday?":"2 or more",
    "Can you train her?":"Yes"
})

_ = pet1.apply_to_adopt(ad2, {
    "How many walks can you take her on everyday?":"2 or more",
    "Can you train her?":"I don't know how, but will learn"
})

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
    print(boxed_list("post type", user.allowed_posts[1:]))

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

def view_applications(header: str, apps: list[str]) -> None:
    print(DIVIDER)

    print(boxed_list(header, apps))

    _ = input("Press any key to return to menu.")
    return None


# SHELTER'S TEXT UI FUNCTIONS

def create_event(user: Shelter) -> None:
    print(DIVIDER)
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
    print(DIVIDER)
    print("\n Let's register a new pet! Type it's info: \n")
    pet_name = input("Name: ")
    pet_type = input("Type (species): ")
    pet_breed = input("Breed: ")
    pet_furColor = input("Fur Color: ")

    pet = Pet(pet_name, pet_type, pet_breed, pet_furColor)

    print(user.add_pet(pet))

    return None

def find_pet(shelters_pets: list[Pet]) -> Pet | None:
    while True:
        name = input("\n> Pet Name: ")

        if name == "q":
            return None

        for pet in shelters_pets:
            if name.lower() == pet.name.lower():
                return pet

        print("Pet Not Found! Try again or type q to quit.")

def update_pet(shelter: Shelter) -> None:
    print(DIVIDER)
    print("\nLet's update a pet!",
          "First, let's find the pet you want to update.\n")

    pet = find_pet(shelter.pets)

    if pet == None:
        return

    print(f"\nHere's {pet.name}'s current profile:")
    print(boxed_list("current info", pet.pet_list()))

    print("If you don't want to update something, just leave it blank.\n")

    new_name = input("> New Name: ")
    if new_name:
        pet.name = new_name

    new_description = input("> New Description: ")
    if new_description:
        pet.description = new_description

    new_age = input("> New Age: ")
    if new_age:
        pet.age = int(new_age)

    new_breed = input("> New Breed: ")
    if new_breed:
        pet.breed = new_breed

    new_fur = input("> New Fur Color: ")
    if new_fur:
        pet.fur_color = new_fur

    while True:
        new_status = input(f"> Do you want to update status from {pet.status} to {STATUS_SEQUENCE[pet.status.lower()].upper()}? [y/n] ")

        if new_status == "y":
            pet.update_status()
            continue

        break

    print(f"\nGreat! Here's {pet.name}'s new profile!")
    print(boxed_list("new profile", pet.pet_list()))

    _ = input("Press any key to return to shelter's menu.")

    return

def add_question(shelter: Shelter) -> None:
    print(DIVIDER)
    print("Let's add a new question to a pet's application form template!")

    pet = find_pet(shelter.pets)

    if pet == None:
        return None

    print("Here's the current form (it may be empty):")
    print(boxed_list(f"{pet.name}'s Adoption Application Template", 
                     pet.form_template_list()))

    while True:
        question: str = input("\n> Type a question or q to quit: ")

        if question == "q":
            break

        print("\nNow let's add possible answers to this question.")

        options: list[str] = []
        while True:
            option = input(">>> Type an anser or <s> to stop: ")

            if option == "s":
                break

            options.append(option)

        print("\nFinally, let's choose 'right' answer.")
        expected: str = input("> Type the preferred option: ")

        print(f"\nQuestion: {question}",
              f"\nOptions: {options}",
              f"\nExpected answer: {expected}\n")

        confirm: str = input("Do you confirm adding this question to the form template? [y/n] ")
        if confirm == "y":
            print("")
            print(pet.add_question(question, options, expected))

    print("Here's the new form:")
    print(boxed_list(f"{pet.name}'s Adoption Application Template", 
                     pet.form_template_list()))

    _ = input("Press any key to return to shelter's menu.")
    return None

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
        print(boxed_list("Shelter's menu", SHELTER_OPTIONS))

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
            update_pet(user)

        elif response == "4b":
            add_question(user)

        elif response == "5":
            view_applications(f"Adoption applications for pets at {user.name}",
                              user.applications_list())

        elif response == "6":
            create_post(user)

        elif response == "7":
            feed.view_feed()

        else:
            print("\nInvalid Option.")

        print(DIVIDER)

# ADOPTER'S TEXT UI FUNCTIONS

def print_all_events() -> None:
    all_events: list[str] = []
    for shelter in accounts.users["Shelter"].values():
        shelter_events = []
        for event in shelter.events:
            shelter_events.append(f"> {event.name.upper()} by {event.shelter.name.title()}")
            shelter_events.append(f"    - Location: {event.location}")
            shelter_events.append(f"    - Date: {event.date}")
            shelter_events.append("")

        all_events.extend(shelter_events)

    print(boxed_list("events", all_events))

    _ = input("Press any key to return to adopter's menu.")

    return None

def print_all_shelters() -> None:
    all_shelters: list[str] = []
    for shelter in accounts.users["Shelter"].values():
        shelter_info = []

        shelter_info.append(f"> {shelter.name.upper()}")

        for field, info in shelter.user_profile.items():
            if info:
                shelter_info.append(f"    - {field.title()}: {info}")

        shelter_info.append("")

        all_shelters.extend(shelter_info)

    print(boxed_list("shelters", all_shelters))

    _ = input("Press any key to return to adopter's menu.")

    return None

def choose_shelters(shelters: dict[str, Shelter]) -> list[str] | None:
    all_shelters: list[str] = []
    for username, shelter in shelters.items():
        all_shelters.append(f"{username} - {shelter.name}")

    print(DIVIDER)
    print(f"\nFiltering shelters!".upper())

    print(boxed_list("shelters", all_shelters))

    choosen_shelters: list[str] = []
    while True:
        response = input("\n> Add shelter to filter (username) or q to stop: ")

        if response in shelters.keys():
            print(f"- {response} added as filter to shelters.")
            choosen_shelters.append(response)
            continue

        if response == "q":
            break

        print("Shelter not found. Try again.\n")

    if len(choosen_shelters) > 0:
        return choosen_shelters
    else:
        return None

def all_pets(shelters: dict[str, Shelter]) -> list[Pet]:
    pets: list[Pet] = []
    for shelter in shelters.values():
        for pet in shelter.pets:
            pets.append(pet)

    return pets

def print_pets_list(pets: list[Pet]) -> None:
    """formatted print of all pets in a given Pet's list"""

    pets_info: list[str] = []
    for pet in pets:
        pets_info.extend(pet.pet_list())

    print(boxed_list("pets", pets_info))

def choose_filters(pets: list[Pet]
                   ) -> dict[str, list[str] | list[int] | None]:
    filters: dict[str, list[str] | None] = {
        "types": [],
        "breeds": [],
        "colors": []
    }

    options = {
        "types": [pet.pet_type for pet in pets],
        "breeds": [pet.breed for pet in pets if pet.breed],
        "colors": [pet.fur_color for pet in pets if pet.fur_color]
    }

    for filter, opts in options.items():
        print(DIVIDER)
        print(f"\nFiltering {filter}!".upper())

        print(boxed_list(filter, opts))

        while True:
            response = input("\n> Type a option to filter or q to quit: ")
            if response in opts:
                filters[filter].append(response)
                print(f"- {response} added as filter to {filter}.")
                continue

            if response == "q":
                if len(filters[filter]) == 0:
                    filters[filter] = None
                break

            print("Invalid option. Try again.")

    return filters

def answer_question(number: int, question: str, options: list[str]) -> str:
    formatted_question: list[str] = [f"> {question}"]

    for opt in options:
        formatted_question.append("   - " + opt)

    while True:
        print(boxed_list(f"Question No. {number}", formatted_question))

        answer = input("> Type your answer: ")

        if answer in options:
            return answer

        print(f"\n{answer} is not a valid option. Try again.")


def apply_adoption(user: Adopter, shelters: dict[str, Shelter]) -> None:
    print(DIVIDER)
    print("Great! Let's adopt a pet!")

    pets = all_pets(shelters)

    pet = find_pet(pets)

    if pet == None:
        return None

    if not pet.is_available():
        print(f"\n[FAIL] {pet.name.title()} is not available for adoption.")
        return None

    if not pet.can_adopter_apply(user.username):
        print(f"\n[FAIL] You already applied to adopt {pet.name.title()}.")
        return None

    print(boxed_list(f"{pet.name}'s adoption form", 
                     [f"We're very glad that you want to adopt {pet.name.title()}",
                      "Please answer the questions below.",
                      "Always type your answer, and make sure it's exactly like one of the given options."])
          )

    answers: dict[str, str] = {}
    count: int = 1

    for question, options, _ in pet.form_template:
        answers[question] = answer_question(count, question, options)
        count += 1

    print("\n" + pet.apply_to_adopt(user, answers))
    return None

def print_all_pets(user: Adopter, shelters: dict[str, Shelter]) -> None:
    print(DIVIDER)

    pets = all_pets(shelters)

    print_pets_list(pets)

    while True:
        response = input("> Do you want to filter pets? [y/n] ")

        if response == "y":
            filtered_shelters = choose_shelters(shelters)
            filters = choose_filters(pets)
            filtered_pets = list(
                search_pets(accounts.users, filtered_shelters, filters)
            )

            print(DIVIDER)
            print("Search results:")

            if len(filtered_pets) == 0:
                print(boxed_list("pets", ["No pet matches filters."]))
            else:
                print_pets_list(filtered_pets)

            break

        elif response == "n":
            break


    while True:
        response = input("\n> Do you want to apply to adopt a pet? [y/n] ")

        if response == "n":
            break

        apply_adoption(user, shelters)




ADOPTER_MENU_FUNCTIONS = [
    ("1", "Update Profile", update_user_profile)
]

def adopter_menu(user: Adopter) -> None:
    print(DIVIDER)
    print(f"\nYou're logged in, {user.name}!\n")

    while True:
        print(boxed_list("Adopter's menu", ADOPTER_OPTIONS))

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
            print_all_pets(user, accounts.users["Shelter"])

        elif response == "5":
            view_applications(f"{user.name}'s adoption applications",
                              user.applications_list())

        elif response == "6":
            create_post(user)

        elif response == "7":
            feed.view_feed()

        else:
            print("\nInvalid Option.\n")

        print(DIVIDER)



def access(type: str) -> User | None:
    print(DIVIDER)
    print(f"\nYou chose {type.title()}! That's so cool!\n")

    while True:
        print(boxed_list("Access Menu", ACCESS_OPTIONS))

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
        print(boxed_list("Pet App", WELCOME_OPTIONS))

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

        print(DIVIDER)

    print("Goodbye!")


if __name__ == "__main__":
    welcome()
