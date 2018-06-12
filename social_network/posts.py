from datetime import datetime


class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        self.timestamp = timestamp or datetime.utcnow()
        self.user = None

    def set_user(self, user):
        self.user = user


class TextPost(Post):
    def __init__(self, text, timestamp=None):
        super(TextPost, self).__init__(text, timestamp)

    def __str__(self):
        return '@{first} {last}: "{text}"\n\t{dt}'.format(
            first=self.user.first_name,
            last=self.user.last_name,
            text=self.text,
            dt=self.timestamp.strftime('%A, %b %d, %Y'))


class PicturePost(Post):
    def __init__(self, text, image_url, timestamp=None):
        super(PicturePost, self).__init__(text, timestamp)
        self.image_url = image_url

    def __str__(self):
        return '@{first} {last}: "{text}"\n\t{url}\n\t{dt}'.format(
            first=self.user.first_name,
            last=self.user.last_name,
            text=self.text,
            dt=self.timestamp.strftime('%A, %b %d, %Y'),
            url=self.image_url)


class CheckInPost(Post):
    def __init__(self, text, latitude, longitude, timestamp=None):
        super(CheckInPost, self).__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return '@{first} Checked In: "{text}"\n\t{lat}, {lon}\n\t{dt}'.format(
            first=self.user.first_name,
            text=self.text,
            lat=self.latitude,
            lon=self.longitude,
            dt=self.timestamp.strftime('%A, %b %d, %Y'))
