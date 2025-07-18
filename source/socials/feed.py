from source.socials.post import Post
from source.users.user import User

class Feed:
    def __init__(self):
        self.posts: dict[str, Post] = {}

    def create_post(self, author: User, type: str, title: str, content: str
             ) -> bool:
        if type in author.allowed_posts:
            p = Post(author, type, title, content)
            self.posts[title] = p
            author.posts[title] = p
            return True
        else:
            return False

    def view_feed(self):
        id = 0
        for post in self.posts.values():
            print(f"[{id}] - ", end=" ")
            post.showPost()
