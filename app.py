from audioop import add
from multiprocessing import Event
from source.queries.search_pet import search_pets
from source.socials.feed import Feed
from source.users.accounts import Accounts
from source.users.adopter import Adopter
from source.users.pet import Pet
from source.users.shelter import Shelter
from source.users.user import User

accounts = Accounts()
feed = Feed()

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
            print("\nLet's Update your profile!")
            user.showShelter()
            print("If you don't want to update something, just leave it blank")

            name = input("New Name: ")
            if name:
                user.name = name

            description = input("New Description: ")
            if description:
                user.description = description

            address = input("New Address: ")
            if address:
                user.address = address

            pix_type = input("New Pix Type: ")
            if pix_type:
                user._pixKeyType = pix_type

            pix_value = input("New Pix Value: ")
            if pix_value:
                user._pixKeyValue = pix_value

            print("\nGreat! Here's your new profile!")
            user.showShelter()

        elif response == "2":
            print("\nLet's create an event!")
            name = input("Name: ")
            date = input("Date: ")
            location = input("Location: ")

            event = Event(name, date, location)
            user.addEvent(event)
            print("[OK] Event created!")

        elif response == "3":
            petType = input("\nPet Type: ")
            user.addPetTypes(petType)

        elif response == "4":
            print("\n Let's register a new pet!")
            pet_name = input("Name: ")
            pet_type = input("Type (species): ")
            pet_breed = input("Breed: ")
            pet_furColor = input("Fur Color: ")
            pet = Pet(pet_name, pet_type, pet_breed, pet_furColor)
            print(user.addPet(pet))

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
            for i in range(1, len(user.allowedPosts)):
                print(f"[{i}] - {user.allowedPosts[i]}")
            post_type = user.allowedPosts[int(input("Choose an option: "))]
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

            print("\nLet's Update your profile!")
            print("If you don't want to update something, just leave it blank")

            name = input("New Name: ")
            if name:
                user.name = name
            
            description = input("New Description: ")
            if description:
                user.description = description

            age = int(input("Age: "))
            if age:
                user.age = age

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
                pet.showPet()

        elif response == "6":

            print("\nLet's add a post! First, choose the type.")
            for i in range(1, len(user.allowedPosts)):
                print(f"[{i}] - {user.allowedPosts[i]}")
            post_type = user.allowedPosts[int(input("Choose an option: "))]
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

            if type == "Adopter":
                user = accounts.create_user(type, username, name, None, None)
            else:
                address = input("Address: ")
                description = input("Description: ")
                user = accounts.create_user(type, username, name, address, description)

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
