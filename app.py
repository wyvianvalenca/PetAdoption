from source.application.form import Form
from source.queries.search_pet import search_pets
from source.socials.post import Post
from source.socials.feed import Feed
from source.users.accounts import Accounts
from source.users.adopter import Adopter
from source.users.pet import Pet
from source.users.pet import STATUS_SEQUENCE
from source.users.shelter import Shelter
from source.users.user import User

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
    "[7] - View Social Feed",
    "[8] - View Donations",
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

""" GLOBAL VARIABLES """

accounts = Accounts()
feed = Feed()

""" INITIAL DATA """

ad1 = accounts.create_user("Adopter", "wyvianvalenca", "Wyvian Valença")
ad2 = accounts.create_user("Adopter", "ycarosales", "ycaro SALES")

sh1 = accounts.create_user("Shelter", "csf", "Casa São Francisco")
sh2 = accounts.create_user("Shelter", "reptile_house", "Reptile's House")

_ = sh1.update_profile({
    "description": "Veterinária Popular",
    "address": "R. dos Bandeirantes, 504 - Farol, Maceió - AL, 57051-120",
    "donation type": "PIX CNPJ",
    "donation code": "12.234.456/0001-01"
})

_ = sh2.update_profile({
    "description": "Amamos repteis!!!!",
    "address": "R. dos Repteis, 111 - Fatol, Maceió"
})

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
    "Are you sure you want to adopt Becky?": "Yes",
    "How many walks can you take her on everyday?":"2 or more",
    "Can you train her?":"Yes"
})

_ = pet1.apply_to_adopt(ad2, {
    "Are you sure you want to adopt Becky?": "Yes",
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

_ = feed.create_post(sh1, "Educational", 
                     "The Decompression Period: Giving Your New Pet Time to Adjust", 
                     "Bringing a new pet home is an exciting time, but it's crucial to remember the '3-3-3 Rule' for rescue animals: 3 days to decompress, 3 weeks to learn your routine, and 3 months to feel truly at home. During the initial period, your new companion may be scared, shy, or unsure of their new surroundings. Avoid overwhelming them with visitors or new experiences, and instead focus on establishing a predictable routine with feeding, walks, and quiet time. This patience will build a strong foundation of trust and help your pet transition smoothly into a loving member of your family.")

_ = (feed.create_post(sh2, "Educational", 
                     "Understanding Dog Body Language: What is Your Pet Trying to Tell You?", 
                     "A wagging tail doesn't always mean a happy dog. Understanding the subtle cues of canine body language is essential for preventing misunderstandings and building a strong bond. Pay attention to their ears, mouth, and overall posture. For example, a relaxed dog might have a loose body and a gently wagging tail, while a fearful dog might tuck its tail, flatten its ears, and lick its lips. Learning to read these signals will not only keep you and your pet safe but will also deepen your understanding of their needs and emotions."))

_ = (feed.create_post(sh2, "Forum", 
                     "Volunteers Needed for Our Upcoming 'Clear the Kennels' Adoption Drive!", 
                     "Hello, pet-loving community! Sunny Paws Shelter is hosting our annual 'Clear the Kennels' adoption event in two weeks, and we're looking for enthusiastic volunteers to help make the day a success. We need help with tasks like walking dogs, managing the kitten playpen, and talking to potential adopters about our amazing animals. If you're available to lend a hand and want to help our residents find their forever homes, please let us know in the comments or send us a direct message for more information."))

_ = (feed.create_post(ad1, "Forum", 
                     "Advice Needed: Introducing My New Rescue Dog to My Resident Cat!", 
                     "Hi everyone, we just brought home a wonderful 2-year-old beagle mix named Cooper, and we're so excited! We already have a 5-year-old cat, Whiskers, who is very calm but has never lived with a dog before. We are keeping them in separate rooms for now, but I was hoping to get some tips and hear about your experiences on how to make the first few weeks as smooth and stress-free as possible for both of them. Any advice would be greatly appreciated!"))

_ = (feed.create_post(ad2, "Success Story", 
                     "Our Shy Little Luna is Finally Blossoming!", 
                     "When we first adopted Luna from the shelter three months ago, she would spend all day hiding under the bed and was too scared to even let us pet her. It broke our hearts to see how timid she was, but we decided to give her all the time and space she needed. Today, I'm overjoyed to share that Luna is a completely different cat! She now sleeps on our bed, greets us at the door with happy meows, and has even started playing with toys. Adopting a shy pet requires patience, but seeing her personality shine through has been the most rewarding experience of our lives."))

""" TEXT UI FUNCTION """

# USER'S TEXT UI FUNCTIONS

def user_pause() -> None:
    _ = input("Press <enter> to return.")

def wip() -> None:
    print("We're still working on this option!")
    return None

def update_user_profile(user: User) -> None:
    print("\nLet's Update your profile!", 
          "Here's your current information:")

    print(boxed_list("current profile", user.profile_list()))

    print("If you don't want to update something, just leave it blank.\n")

    new_profile: dict[str, str] = {}
    for field in user.user_profile.keys():
        new_data = input(f"New {field.title()}: ")
        if new_data:
            new_profile[field] = new_data

    print()
    print(user.update_profile(new_profile))

    print("\nGreat! Here's your new profile!")
    print(boxed_list("new profile", user.profile_list()))

    user_pause()

    return None

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

    return None

def view_feed(message: str, posts: list[Post], user: User) -> None:
    print(DIVIDER)
    print(f"\n{message.upper()}:\n")

    for id, post in enumerate(posts):
        print(boxed_list(f"post id: {id}", post.post_list()))

        while True:
            action: str = input("\n> Type " + 
                                "<q> to quit, " +
                                "<n> to see next post, " +
                                "<v> to view comments, " +
                                "<c> to comment or " +
                                "<l> to like: ")

            if action == "q":
                return None

            elif action == "n":
                break

            elif action == "v":
                view_feed(f"Comments for post '{post.title}'", 
                          post.comments, user)

            elif action == "c":
                print()
                title: str = input("Title: ")
                content: str = input("Content: ")
                c: Post = Post(user, "comment", title, content)
                post.add_comment(c)
                print("\n[OK] Comment added.")

            elif action == "l":
                post.like_post()
                print("\n[OK] Post liked.")

            else:
                print("\nInvalid option. Try Again")

    print(f"\n{message.title()} ended.\n")
    
    print(DIVIDER)

    user_pause()

def deny_other_applications(apps: list[Form], accepted: int) -> None:
    for index, app in enumerate(apps):
        if index != accepted:
            if app.status == "submitted":
                feedback: str = input(f"\n> Give {app.applicant} a feedback as to why their application was denied: ")

                print()
                _ = app.deny(feedback)

                print("[OK] Application denied.\n")
            else:
                print(f"\n[FAIL] Application already processed.\n")

    return None

def respond_application(adopters: dict[str, Adopter], shelter: Shelter) -> bool:
    """Handles application processing. Return True if everything's OK and False if the user's input was wrong and we need to call the function again."""
    app_id: str = input("> Type an application's code (like 0-0, 1-2) to process it or <q> to quit: ")

    if app_id == "q":
        return True

    try:
        pet_index, app_index = [int(x) for x in app_id.split("-")]
    except ValueError:
        return False

    try:
        pet: Pet = shelter.pets[pet_index]
        pets_apps: list[Form] = pet.applications
    except IndexError:
        return False

    try:
        form: Form = pets_apps[app_index]
        applicant: User = adopters[form.applicant]
    except IndexError:
        return False

    print(f"\nYou choose {form.applicant}'s applicatiion for {form.pet.title()}")

    profile = input(f"\n> Do you wish to see {form.applicant}'s profile? [y/n] ")
    if profile == "y":
        print(boxed_list("applicant's profile", applicant.profile_list()))

    while True:
        result = input(f"\n> Do you approve {form.applicant}'s application? [y/n/q] ")
        if result == "y":
            if form.approve():
                pet.update_status()
                pet.tutor = applicant
                print(f"\n[OK] Application approved! {form.applicant} is {form.pet.title()}'s new tutor.")

                deny_other_applications(pets_apps, app_index)

            else:
                print("\n[FAIL] Application already processed.\n")

            break

        elif result == "n":
            deny_other_applications([form], -1)
            break

        elif result == "q":
            break

        print("\nInvalid option. Try again.\n")

    user_pause()

    return True

def view_applications(header: str, apps: list[str]) -> None:
    print(DIVIDER)

    print(boxed_list(header, apps))

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

    user_pause()

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

    user_pause()

    return None

def show_donations(shelter: Shelter) -> None:
    print(boxed_list("donations", shelter.donations_list()))

    user_pause()

    return None

# SHELTER_MENU_FUNCTIONS = [
#     ("1", "Update Profile", update_user_profile),
#     ("2", "Create Events", create_event),
#     ("3", "Add Pet Type", add_pet_type),
#     ("4", "Register New Pet", register_new_pet),
#     ("4a", "Update Pet Profile", update_pet),
#     ("5", "[WIP] View Adoption Applications", wip),
#     ("6", "Create Post", create_post),
#     ("7", "Open Social Feed", view_feed)
# ]

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

            while not respond_application(accounts.users["Adopter"], user):
                print("\nInvalid code. Try again.\n")

        elif response == "6":
            create_post(user)

        elif response == "7":
            view_feed("social feed", 
                      [post for post in feed.posts.values()], 
                      user)
        
        elif response == "8":
            show_donations(user)

        else:
            print("\nInvalid option.")

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

    user_pause()

    return None

def print_all_shelters(user: User, shelters: list[Shelter]) -> None:
    username: str = user.username

    all_shelters: list[str] = []

    for id, shelter in enumerate(shelters):
        shelter_info: list[str] = [f"> [{id}] {shelter.name.upper()}"]

        for field, info in shelter.user_profile.items():
            if info:
                shelter_info.append(f"    - {field.title()}: {info}")

        shelter_info.append("")

        all_shelters.extend(shelter_info)

    print(boxed_list("shelters", all_shelters))

    while True:
        donate = input("> Do you wish to make a donation to a shelter? [y/n] ")

        if donate == "y":

            try:
                shelter_index: int = int(input("\n> Type a shelter's code: "))
            except ValueError:
                print("\nInvalid code. Try again\n")
                continue

            while True:
                try:
                    donation_receiver: Shelter = shelters[shelter_index]
                    break
                except IndexError:
                    print("\nInvalid code. Try again\n")
                    continue

            while True:
                try:
                    ammount: float = float(
                        input(
                            f"\n> How much do you wish to donate to {donation_receiver.name}? "))
                    print("\n" 
                          + donation_receiver.donate(username, ammount) 
                          + "\n\n")
                    break
                except ValueError:
                    print("\nInvalid answer. Type a number\n")
                    continue

        elif donate == "n":
            return None

        else:
            print("\nInvalid code. Try again\n")

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
            print_all_shelters(user, 
                               [s for s in accounts.users["Shelter"].values()])

        elif response == "4":
            print_all_pets(user, accounts.users["Shelter"])

        elif response == "5":
            view_applications(f"{user.name}'s adoption applications",
                              user.applications_list())

            user_pause()

        elif response == "6":
            create_post(user)

        elif response == "7":
            view_feed("social feed", 
                      [post for post in feed.posts.values()], 
                      user)

        else:
            print("\nInvalid option.\n")

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
            print("Invalid option. Try again.")

        print(DIVIDER)

    print("Goodbye!")


if __name__ == "__main__":
    welcome()
