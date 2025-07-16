from source.users.pet import Pet
from source.users.accounts import Accounts
from source.queries.search_pet import search_pets


if __name__ == "__main__":
    acc = Accounts()

    user = acc.create_user("Adopter", "wyvian", None, None, None)
    if user:
        pass

    sh = acc.create_user("Shelter", "casa_pet", "Casa PET", "aaa", "bbbb")
    if sh:
        sh.addPetTypes("Dog")
        sh.addPet(Pet("Becky", "Dog", "Chow Chow", "Orange"))
        sh.addPet(Pet("Frieren", "Dog", "Chow Chow", "White"))

    sh2 = acc.create_user("Shelter", "amorpet", "AmorPET", "cccc", "dddddd")
    if sh2:
        sh2.addPetTypes("Cat")
        sh2.addPet(Pet("Tomas", "Cat", None, "Black"))
        sh2.addPet(Pet("Flow", "Cat", None, "Black"))

    sh3 = acc.create_user("Shelter", "NEAFA", "NEAFA", "eeeee", "ffffff")
    if sh3:
        sh3.addPetTypes("Dog")
        sh3.addPet(Pet("Thor", "Dog", "Golden Retriever", "White"))


    results = search_pets(acc.users, ["casa_pet"], {
            "types": None, 
            "breeds": ["Chow Chow"], 
            "colors": None, 
            "ageRange": None
    })
