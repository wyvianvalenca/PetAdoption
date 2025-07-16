
class Event():
    def __init__(self, name: str, date: str, location: str, shelter: 'Shelter'):
        self.name = name
        self.date = date
        self.location = location

    def showEvent(self):
        print(f"{self.name.upper()} by {self.shelter.name.title()}")
        print("Date: ", self.date)
        print("Location: ", self.location)
