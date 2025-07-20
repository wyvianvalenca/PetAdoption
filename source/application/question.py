class Question:
    def __init__(self, name: str, options: list[str], expected: str):
        self._name: str = name
        self._options: list[str] = options
        self._expected_answer: str = expected

        self.user_answer: str
        self.is_expected: bool

    @property
    def name(self) -> str:
        return self._name

    @property
    def options(self) -> list[str]:
        return self._options

    @property
    def expected_answer(self) -> str:
        return self._expected_answer

    def answer(self, user_option: str) -> bool:
        if user_option in self.options:
            self.user_answer = user_option

            self.is_expected = (self.expected_answer == self.user_answer)
            return True

        return False

    def question_list(self) -> list[str]:
        question_info: list[str] = [self.name]

        for option in self.options:
            if option == self.expected_answer:
                question_info.append("   -" + option + " **")
                continue

            question_info.append("   -" + option)
            question_info.append("")

        return question_info

