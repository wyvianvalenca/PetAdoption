from source.users.user import User

class Post:
    def __init__(self, author: User, type: str, title: str, content: str):
        self._author: User = author
        self._type: str = type
        self._title: str = title.upper()
        self._content: str = content
        self._likes: int = 0
        self._comments: list['Post'] = []
        self.parent: 'Post' | None = None

    @property
    def author(self) -> User:
        return self._author

    @property
    def type(self) -> str:
        return self._type

    @property 
    def title(self) -> str:
        return self._title

    @property
    def content(self) -> str:
        return self._content

    def updateContent(self, user: User, content: str) -> None:
        if user == self.author:
            self._content = content

    @property
    def likes(self) -> int:
        return self._likes

    def likePost(self) -> None:
        self._likes += 1

    @property
    def comments(self) -> list['Post']:
        return self._comments

    def addComment(self, comment: 'Post'):
        comment.parent = self
        self.comments.append(comment)

    def showPost(self):
            # Define uma borda para reutilização
            border = "─" * 50

            print(f"\n {border}\n",
                  f"TÍTULO: {self.title}\n",
                  f"por: @{self.author.username}\n",
                  "-" * 30, "\n", 
                  self.content, "\n\n", 
                  f"💬 {len(self.comments)} comentários   ",
                  f"❤️  {self.likes} curtidas\n",
                  f"{border}\n")

    def showComments(self):
        pass
