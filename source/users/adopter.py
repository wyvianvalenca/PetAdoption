from source.users.user import User
from source.application.form import Form

class Adopter(User):
    def __init__(self, id: int, username: str, name: str):
        super().__init__(username, id, name)
        self.user_profile.update({
            'age': None,
            'description': None
        })

        self.applications: list[Form] = []

        self.allowed_posts.extend(["Forum", "Success Story"])

    def applications_list(self) -> list[str]:
        all_apps: list[str] = []
        for index, app in enumerate(self.applications):
            all_apps.extend(app.form_list(str(index)))
            all_apps.append("-" * 50)
            all_apps.append("")

        return all_apps


