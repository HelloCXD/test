from app.exts import db


class Banners(db.Model):
    bannerid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image= db.Column(db.String(256))


class Goods(db.Model):
    postid= db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(256))
    image = db.Column(db.String(256))
    duration=db.Column(db.String(100))


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.Integer,unique=True)
    mail = db.Column(db.String(256))
    password = db.Column(db.String(100))
    token = db.Column(db.String(100))
