from types import FunctionType
from source.users.adopter import Adopter
from source.users.shelter import Shelter
from source.users.pet import Pet

def isType(types: list[str], pet: Pet) -> bool:
    return pet.pet_type in types

def isBreed(breeds: list[str], pet: Pet) -> bool:
    return pet.breed in breeds

def isFurColor(colors: list[str], pet: Pet) -> bool:
    return pet.fur_color in colors

def inAgeRange(targets: list[int], pet: Pet) -> bool:
    if pet.age is not None:
        return pet.age in targets
    else:
        return False

def search_pets(users: dict[str, dict[str, Shelter | Adopter]],
                shelters: list[str] | None, 
                filters: dict[str, list[str] | list[int] | None]
                ) -> set[Pet]:

    functions: dict[str, FunctionType] = {
        "types": isType,
        "breeds": isBreed,
        "colors": isFurColor,
        "ageRange": inAgeRange
    }

    filtered: dict[str, list[Pet]] = {
        "types": [],
        "breeds": [],
        "colors": [],
        "ageRange": []
    }

    pets_shelters: list[Pet] = []

    # selects pets from filtered shelters
    if shelters is not None:
        for shelter in shelters:
            pets_shelters.extend(users["Shelter"][shelter].pets)
    # or all shelters
    else:
        for shelter in users["Shelter"].values():
            pets_shelters.extend(shelter.pets)

    # filters pets based on informed criterias
    for criteria, items in filters.items():
        if items is not None:
            filtered[criteria] = [
                pet for pet in pets_shelters if functions[criteria](items, pet)
            ]

    # transforms lists to sets to facilitade intersection between criterias
    intersection: set[Pet] = set(pets_shelters)
    for criteria, pet_list in filtered.items():
        if filters[criteria] is not None:
            intersection = intersection.intersection(set(pet_list))

    return intersection
