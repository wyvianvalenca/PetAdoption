from copy import deepcopy
from .question import Question

class Form:
    def __init__(self, applicant: str, pet: str, 
                 questions_template: list[Question]):
        self._applicant: str = applicant
        self._pet: str = pet

        self._questions: list[Question]
        for question in questions_template:
            self._questions.append(deepcopy(question))

        self.score: float = 0
        self.status: str = "submitted"

    @property
    def applicant(self) -> str:
        return self._applicant

    @property
    def pet(self) -> str:
        return self._pet

    @property
    def questions(self) -> list[Question]:
        return self._questions

    def compute_score(self) -> float:
        count: int = 0

        for question in self.questions:
            if question.is_expected:
                count += 1

        self.score = count / len(self.questions)
        return self.score

    def approve(self) -> bool:
        if self.status == "submitted":
            self.status = "approved"
            return True

        return False

    def form_list(self) -> list[str]:
        form_info: list[str] = [f"> {self.applicant}'s application to adopt {self.pet}"]

        for question in self.questions:
            form_info.append(f"  - {question.name}")
            form_info.append(f"     + Expected Answer: {question.expected_answer}")
            form_info.append(f"     + {self.applicant}'s Answer: {question.user_answer}")

        form_info.append(f"  - Score: {self.score}")
        form_info.append(f"  - Status: {self.status.title()}")

        return form_info
