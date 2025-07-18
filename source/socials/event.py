
class Event():
    def __init__(self, name: str, date: str, location: str, shelter: 'Shelter'):
        self.name: str = name
        self.date: str = date
        self.location: str = location
        self.shelter: 'Shelter' = shelter

    def print_event(self):
        print(f"{self.name.upper()} by {self.shelter.name.title()}")
        print("Date: ", self.date)
        print("Location: ", self.location)
