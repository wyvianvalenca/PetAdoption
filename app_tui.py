from textual import on
from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.screen import Screen, ModalScreen
from textual.containers import Container, HorizontalGroup, Center
from textual.widgets import (
        Markdown, 
        Static, 
        Label, 
        Button,
        Input,
        Footer, 
        Header
)

from source.users.user import User
from source.users.adopter import Adopter
from source.users.accounts import Accounts

class AdopterMenu(Screen):
    def __init__(self, user: Adopter):
        super().__init__()
        self.user = user


class Login(Screen[User]):
    def __init__(self, user_type: str, accounts: Accounts, **kwargs) -> None:
        super().__init__(**kwargs)
        self.user_type: str = user_type
        self.accounts: Accounts = accounts

    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="login-container"):
            with Center():
                yield Label(f"Login as {self.user_type}")
            with Center():
                yield Input(placeholder="Enter your username", id="username")
            with HorizontalGroup():
                yield Button("Login", variant="primary", id="login")
                yield Button("Cancel", variant="error", id="close")
        yield Footer()

    @on(Button.Pressed, "#login")
    def handle_login(self, event:Button.Pressed) -> None:
        _ = event.stop()
        username_input = self.query_one("#username", Input)
        username = username_input.value

        if not username:
            self.notify("Username can't be empty")
            return

        # Roda a função de login do arquivo accounts.py
        logged_user = self.accounts.login(self.user_type, username)

        if logged_user:
            # Retorna o usuário logado com sucesso
            self.dismiss(logged_user)
        else:
            # Mostra erro se o usuário não for encontrado
            self.notify("User not found")

    @on(Button.Pressed, "#close")
    def handle_close(self, event: Button.Pressed) -> None:
        event.stop()
        self.dismiss(None)

class ChooseRole(ModalScreen[str]):
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Label("How do you wanto to access the system?"),
            Button("As an adopter", id="adopter", variant="primary"),
            Button("As a shelter", id="shelter", variant="primary",
                   classes="secondary"),
            id="role-container"
        )

    @on(Button.Pressed, "#adopter")
    def handle_adopter(self, event: Button.Pressed) -> None:
        event.stop()
        self.dismiss("Adopter")

    @on(Button.Pressed, "#shelter")
    def handle_shelter(self, event: Button.Pressed) -> None:
        event.stop()
        self.dismiss("Shelter")


WELCOME_MD = """\
# Welcome to PetAdoption!

Your journey to finding a new best friend starts here. Our platform connects loving homes with pets in need, making the adoption process seamless and joyful.

Explore detailed pet profiles, discover local shelters and events, and connect with a community of fellow pet lovers.

***

_Let's find a forever home for every pet._
"""

class PetApp(App):

    CSS_PATH = "tcss/app.tcss"
    BINDINGS = [
        ("d", "toggle_dark", "Toggle Dark Mode"),
    ]
    SCREENS = {
        "role": ChooseRole,
        "login": Login
    }

    user: User | reactive[None] = reactive(None)

    def __init__(self):
        super().__init__()
        self.accounts: Accounts = Accounts()
        # Para teste: cria um usuário "adopter" com username "wyvian"
        _ = self.accounts.create_user("Adopter", "wyvian", None, None, None)

    def compose(self) -> ComposeResult:
        yield Footer()
        yield Header()
        with Container():
            md = Markdown(WELCOME_MD, id="welcome")
            md.border_title = "PetApp"
            yield md
            with HorizontalGroup(classes="two-options"):
                yield Button("Login", id="login", variant="primary")
                yield Button("Sign Up", id="signup", variant="primary",
                         classes="secondary")

    def on_mount(self) -> None:
        self.theme = "tokyo-night"

    def on_button_pressed(self, event: Button.Pressed) -> None:
        def check_role(role: str) -> None:
            if event.button.id == "login":
                def check_login(user: User | None) -> None:
                    self.user = user

                self.push_screen(Login(role, self.accounts), check_login)

        self.push_screen(ChooseRole(), check_role)


    def action_toggle_dark(self) -> None:
        self.theme = (
            "tokyo-night" if self.theme == "textual-light" else "textual-light"
        )


if __name__ == "__main__":
    app = PetApp()
    _ = app.run()
