from source.socials.post import Post
from source.users.user import User

class Feeds:
    def __init__(self):
        self.posts: dict[str, dict[str, Post]] = {
            "Forum": {},
            "Success Story": {},
            "Educational": {},
            "comments": {}
        }

    def post(self, author: User, type: str,
             title: str, content: str) -> Post | None:
        if type in author.allowedPosts:
            p = Post(author, type, title, content)
            self.posts[type][title] = p
            author.posts[type][title] = p
            return p
        else:
            return None
