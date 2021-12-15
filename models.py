import mongoengine as db


class Post(db.Document):
    post_id = db.IntField(Required=True)
    author = db.StringField(Required=True)
    datetime = db.StringField(Required=True)
    content = db.StringField(Required=True)
    likes = db.IntField(Required=True)
    ad = db.BooleanField(Required=True)

    def to_dict(self):
        result = {}
        result['id'] = self.post_id
        result['author'] = self.author
        result['datetime'] = self.datetime,
        result['content'] = self.content
        result['likes'] = self.likes
        result['ad'] = self.ad
        result['liked'] = False
        return result


class Like(db.Document):
    like_id = db.IntField(Required=True)
    user_id = db.IntField(Required=True)
    post_id = db.IntField(Required=True)

    def to_dict(self):
        result = {}
        result['id'] = self.like_id
        result['user_id'] = self.user_id
        result['post_id'] = self.post_id
        return result


class User(db.Document):
    user_id = db.IntField(Required=True)
    email = db.StringField(Required=True)
    password = db.StringField(Required=True)

    def to_dict(self):
        result = {}
        result['id'] = self.user_id
        result['email'] = self.email
        result['password'] = self.password
        return result
