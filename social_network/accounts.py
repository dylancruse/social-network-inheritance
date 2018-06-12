
class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.posts = []
        self.following = []

    def add_post(self, post):
        post.user = self
        self.posts.append(post)

    def get_timeline(self):
        all_posts = []
        for user in self.following:
            for post in user.posts:
                all_posts.append(post)
        return sorted(all_posts, key=lambda post: post.timestamp)

    def follow(self, other):
        self.following.append(other)
