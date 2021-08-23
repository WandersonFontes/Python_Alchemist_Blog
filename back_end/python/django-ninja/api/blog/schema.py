from ninja.schema import Schema

class ProfileBody(Schema):
    id: int = None
    user_id: int = None
    website: str
    bio: str

class PostBody(Schema):
    id: int = None
    title: str
    subtitle: str
    slug: str = None
    body: str
    meta_description: str
    publish_date: str
    published: str
    author: int
    tag: int = None