from twitter import db

class Tweets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tweet = db.Column(db.String(500))
    username = db.Column(db.String(80))
    retweet = db.Column(db.Integer)
    likes = db.Column(db.Integer)
    email = db.Column(db.String(80))
    profile_photo = db.Column(db.String(80))
    date = db.Column(db.String(30))

    def __init__(self, tweet, username, email, profile_photo, date, retweet=0, likes=0):
        self.tweet = tweet
        self.username = username
        self.email = email
        self.profile_photo = profile_photo
        self.retweet = retweet
        self.likes = likes
        self.date = date

class Followers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    followers = db.Column(db.String(80))

    def __init__(self, username=username, followers=followers):
        self.username = username
        self.followers = followers

class Following(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    following = db.Column(db.String(80))

    def __init__(self, username=username, following=following):
        self.username = username
        self.following = following




