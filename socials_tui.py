from textual import on
from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup, Vertical
from textual.reactive import reactive
from textual.widgets import Collapsible, Button, Header, Markdown, Footer

from source.users.user import User
from source.socials.post import Post
from source.socials.feed import Feed

class ViewPost(Vertical):
    def __init__(self, post: Post, **kwargs):
        super().__init__(**kwargs)
        self.post: Post = post
        self.likes = reactive(self.post.likes)

    def compose(self) -> ComposeResult:
        title: str = f"{self.post.title} - @{self.post.author.username} | 💬 {len(self.post.comments)} ❤️ {self.post.likes}"
        with Collapsible(title=title):
            yield Markdown(self.post.content)
            with HorizontalGroup():
                yield Button("Like", variant="error", id="like")
                yield Button("Comment", id="comment")


    @on(Button.Pressed, "#like")
    def handle_like(self, event: Button.Pressed) -> None:
        _ = event.stop()
        self.post.like_post()

class ViewFeed(App):
    def __init__(self, feed: Feed, **kwargs):
        super().__init__(**kwargs)
        self.feed: Feed = feed

    def compose(self) -> ComposeResult:
        yield Header()
        with Vertical():
            for post in self.feed.posts.values():
                yield ViewPost(post)
        yield Footer()

TEST_MD = """\
# Tuaque magna Tirynthia ferrum

## Amaris volucris dominis praesensque proxima inritata creatus

Lorem markdownum, Assyrii. Montes melior non dederat [Ethemon in
dant](http://animiredire.com/oculis) albentia *tenues*: et dabat umbrae, ut
oscula tuta, inter. Ab urbis; mea deus quid, pervenientia Musa reparabat litus,
latrator harundine Laurens! Genitor corpus recordor praecipue [aliturque umbras
nescio](http://flore-ignibus.org/tradideratagitur.php) Cicones sagittis lyram
agitantem, lacerto remos. *Neque* anum loca crescitque dolores potest Aurora,
*sub quam*, sed lupis egi ponunt insolida.

> Pontifici bacchantum trementes erat est artificem desit alti formam: illo non
> patriorum cetera pugnat inmissos purpureae tanta. Damno effigiem et mater
> saetaeque de ambo litore ut sibi fuit corpore. Pedibus a mortalia gaudia
> alitibus species sacerdos praemiaque Venus; atque quod iubas inpetus removete
> corpore nulloque Aeneas sis manentem? Moraque quem omnes animas illa cum qui
> fidemque, os exiguam Turnus, riguerunt. Aetas parte aequore quaecumque serpit
> plures paterque fremitu, in multifidasque flumine restet!
"""

if __name__ == "__main__":
    u = User("wyvian", 1)
    u.allowed_posts.extend(["Success Stories"])
    f: Feed = Feed()
    print(u.allowed_posts)
    print(f.create_post(u, "Success Stories", "Testando o post", TEST_MD))
    print(f.create_post(u, "Success Stories", "Testando o post", TEST_MD))
    print(f.create_post(u, "Success Stories", "Testando o post", TEST_MD))
    print(f.create_post(u, "Success Stories", "Testando o post", TEST_MD))
    print(f.create_post(u, "Success Stories", "Testando o post", TEST_MD))
    print(f.create_post(u, "Success Stories", "Testando o post", TEST_MD))
    print(f.create_post(u, "Success Stories", "Testando o post dnv", TEST_MD))
    app = ViewFeed(f)
    _ = app.run()

