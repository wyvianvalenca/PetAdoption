from source.socials.event import Event
from source.queries.search_pet import search_pets
from source.socials.feed import Feed
from source.users.accounts import Accounts
from source.users.adopter import Adopter
from source.users.pet import Pet
from source.users.shelter import Shelter
from source.users.user import User

accounts = Accounts()
feed = Feed()

ad1 = accounts.create_user("Adopter", "wyvianvalenca", "Wyvian Valença")
ad2 = accounts.create_user("Adopter", "ycarosales", "ycaro SALES")

sh1 = accounts.create_user("Shelter", "neafa", "NEAFA")
sh2 = accounts.create_user("Shelter", "reptile_house", "Reptile's House")

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

def shelter_menu(user: Shelter):
    print(f"\nWelcome, {user.name}!")
    print("[1] - Update Profile")
    print("[2] - Create Events")
    print("[3] - Add Pet Type")
    print("[4] - Register New Pet")
    print("[4a] - Update Pet")
    print("[5] - View Adoption Applications")
    print("[6] - Create Post")
    print("[7] - View Social Feed")
    print("[b] - Return to main menu")

    while True:
        response = input("\nChoose an option: ")
        if response == "b":
            return 0;

        elif response == "1":
            update_user_profile(user)

        elif response == "2":
            print("\nLet's create an event!")
            name = input("Name: ")
            date = input("Date: ")
            location = input("Location: ")

            event = Event(name, date, location, user)
            user.add_events(event)
            print("[OK] Event created!")

        elif response == "3":
            petType = input("\nPet Type: ")
            user.add_pet_type(petType)

        elif response == "4":
            print("\n Let's register a new pet!")
            pet_name = input("Name: ")
            pet_type = input("Type (species): ")
            pet_breed = input("Breed: ")
            pet_furColor = input("Fur Color: ")
            pet = Pet(pet_name, pet_type, pet_breed, pet_furColor)
            print(user.add_pet(pet))

        elif response == "4a":
            print("\nLet's update a pet!")
            name = input("Pet Name: ")
            
            choosen = False
            for pet in users.pets:
                if name == pet.name:
                    choosen = pet
                    choosen.showPet()
                    break

            if choosen == False:
                print("Pet not found.")
                continue
            
            print("If you don't want to update something, just leave it blank")

            name = input("Name: ")
            if name:
                choosen.name = name

            description = input("Description: ")
            if description:
                choosen.description = description

            print(f"\nGreat! Here's {choosen.name}'s new profile!")
            choosen.showShelter()

        elif response == "5":
            pass

        elif response == "6":

            print("\nLet's add a post! First, choose the type.")
            for i in range(1, len(user.allowed_posts)):
                print(f"[{i}] - {user.allowed_posts[i]}")
            post_type = user.allowed_posts[int(input("Choose an option: "))]
            title = input("Title: ")
            content = input("Content: ")

            if feed.create_post(user, post_type, title, content):
                print("[OK] Post created")
            else:
                print("[FAIL] You can't post that.")

        elif response == "7":
            feed.view_feed()

        else:
            print("\nInvalid Option.\n")

def adopter_menu(user: Adopter):
    print(f"\nWelcome, {user.name}!")
    print("[1] - Update Profile")
    print("[2] - View Events")
    print("[3] - View Shelters")
    print("[4] - View Pets")
    print("[5] - View Adoption Applications")
    print("[6] - Create Post")
    print("[7] - View Social Feed")
    print("[b] - Return to main menu")

    while True:
        response = input("\nChoose an option: ")
        if response == "b":
            return 0;

        elif response == "1":
            update_user_profile(user)

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

        elif response == "6":

            print("\nLet's add a post! First, choose the type.")
            for i in range(1, len(user.allowed_posts)):
                print(f"[{i}] - {user.allowed_posts[i]}")
            post_type = user.allowed_posts[int(input("Choose an option: "))]
            title = input("Title: ")
            content = input("Content: ")

            if feed.create_post(user, post_type, title, content):
                print("[OK] Post created")
            else:
                print("[FAIL] You can't post that.")

        elif response == "7":
            feed.view_feed()

        else:
            print("\nInvalid Option.\n")



def access(type: str) -> User | None:

    print("\nCome on in!")
    print("[1] - Login")
    print("[2] - Create Account")
    print("[b] - Return to main menu")
    response = input("Choose an option: ")
    while True:
        if response == "b":
            return None

        elif response == "1":
            username = input("Username: ")
            user = accounts.login(type, username)
            return user

        elif response == "2":
            username = input("Username: ")
            name = input("Name: ")
            user = accounts.create_user(type, username, name)
            return user

        else:
            print("Invalid option.")



def welcome():
    while True:
        print("\nWelcome! How do you want to access the system?")
        print("[1] - Adopter")
        print("[2] - Shelter")
        print("[q] - Quit")
        response = input("Choose an option: ")

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
