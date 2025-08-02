from source.users.adopter import Adopter
from source.application.form import Form

STATUS_SEQUENCE: dict[str, str] = {
    "rescued": "in treatment",
    "in treatment": "available for adoption",
    "available for adoption": "adopted",
    "adopted": "adopted"
}

class Pet:
    def __init__(self, 
                 name: str, 
                 pet_type: str,
                 breed: str | None, 
                 fur_color: str | None):
        self.name: str = name.lower()
        self._pet_type: str = pet_type
        self.breed: str | None = breed
        self.fur_color: str | None = fur_color

        self.age: int | None = None
        self.description: str | None = None

        self._status: str = 'Rescued'
        self.form_template: list[tuple[str, list[str], str]] = [
            (f"Are you sure you want to adopt {self.name.title()}?", ["Yes", "No"], "Yes")
        ]
        self.applications: list[Form] = []
        self.tutor: Adopter

    @property
    def pet_type(self) -> str:
        return self._pet_type

    @property
    def status(self) -> str:
        return self._status.upper()

    @status.setter
    def status(self, value: str) -> None:
        if value.lower() in STATUS_SEQUENCE:
            self._status = value.lower()

    def update_status(self) -> None:
        self.status = STATUS_SEQUENCE[self.status.lower()]

        return None

    def add_question(self, name: str, options: list[str], 
                     expected_answer: str) -> str:
        if expected_answer not in options:
            return f"[FAIL] Expected answer '{expected_answer}' is not a valid option."

        question: tuple[str, list[str], str] = (name, options, expected_answer)
        self.form_template.append(question)
        return "[OK] Question added to form template."

    def form_template_list(self) -> list[str]:
        template_info: list[str] = []

        for question, options, expected in self.form_template:
            template_info.append(f"  > {question}")
            for opt in options:
                template_info.append(f"     - {opt}")
            template_info.append(f"    Expected: {expected}")

        return template_info

    def can_adopter_apply(self, username: str) -> bool:
        applicants: list[str] = [app.applicant for app in self.applications]
        return not username in applicants

    def is_available(self) -> bool:
        return self.status.lower() == "available for adoption"

    def apply_to_adopt(self, user: Adopter, answers: dict[str, str]) -> str:
        application = Form(user.username, self.name, self.form_template)
        for question in application.questions:
            if question.answer(answers[question.name]) == False:
                return f"[FAIL] {answers[question.name]} is not an option for '{question.name}'."

        self.applications.append(application)
        user.applications.append(application)

        print()
        return (f"[OK] Application submitted.\nYou are a {application.compute_score() * 100:.2f}% match for {self.name.title()}")

    def pet_list(self) -> list[str]:
        pet_info: list[str] = []

        pet_info.append(f"> {self.name.upper()}")
        pet_info.append(f"   - Pet Type: {self.pet_type}")

        if self.breed:
            pet_info.append(f"   - Breed: {self.breed}")

        if self.description:
            pet_info.append(f"   - Desc: {self.description}")

        if self.fur_color:
            pet_info.append(f"   - Fur Color: {self.fur_color}")

        if self.age:
            pet_info.append(f"   - Age: {self.age}")

        pet_info.append(f"   - Status: {self.status}")

        if self.status.lower() == "adopted":
            pet_info.append(f"   - Tutor: {self.tutor.name}")
        else:
            pet_info.append(f"   - Applications: {len(self.applications)}")

        pet_info.append("")

        return pet_info
