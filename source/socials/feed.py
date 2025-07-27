from source.socials.post import Post
from source.users.user import User

class Feed:
    def __init__(self):
        self.posts: dict[str, Post] = {}

    def create_post(self, author: User, post_type: str, title: str, content: str
             ) -> bool:
        if post_type in author.allowed_posts:
            p = Post(author, post_type, title, content)
            self.posts[title] = p
            author.posts[title] = p
            return True
        else:
            return False

