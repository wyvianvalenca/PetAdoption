from .question import Question

class Form:
    def __init__(self, applicant: str, pet: str, 
                 questions_template: list[tuple[str, list[str], str]]):
        self._applicant: str = applicant
        self._pet: str = pet

        self._questions: list[Question] = []
        for question, options, expected in questions_template:
            q = Question(question, options, expected)
            self._questions.append(q)

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
        """Formats all the forms info into a list, with each string being a line."""
        form_info: list[str] = [
            f"> {self.applicant}'s application to adopt {self.pet.title()}",
            f"  - Questions:"
        ]

        for question in self.questions:
            form_info.append(f"    + {question.name}")
            form_info.append(f"       * Preferred Answer: {question.expected_answer}")
            form_info.append(f"       * {self.applicant}'s Answer: {question.user_answer}")

        form_info.append(f"  - Compatibility: {self.compute_score() * 100:.2f}%")
        form_info.append(f"  - Status: {self.status.title()}")
        form_info.append("")

        return form_info
