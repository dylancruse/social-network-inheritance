
class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.posts = []

    def add_post(self, post):
        post.user = self
        self.posts.append(post)

    def get_timeline(self):
        pass

    def follow(self, other):
        pass
