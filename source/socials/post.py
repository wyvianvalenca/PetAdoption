import textwrap
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

    def like_post(self) -> None:
        self._likes += 1

    @property
    def comments(self) -> list['Post']:
        return self._comments

    def add_comment(self, comment: 'Post'):
        comment.parent = self
        self.comments.append(comment)

    def post_list(self) -> list[str]:
        """Posts info formatted into a list of strings"""

        post_info: list[str] = []

        post_info.append(f"{self.type} post by {self.author.name.title()} (@{self.author.username})")
        post_info.append(f"ᯓ➤ {self.title.upper()}")
        post_info.append("")
        post_info.extend(textwrap.wrap(self.content, 
                                       initial_indent="  ╰┈➤ ", 
                                       subsequent_indent="      "))

        post_info.append("")
        post_info.append(f"  🗨 {len(self.comments)} comments  " + 
                         f"❤︎ {self.likes} likes")

        # post_info.append("⋆ > " + ("━" * 50) + " < ⋆")
        # post_info.append("")

        return post_info

    def showComments(self):
        pass
