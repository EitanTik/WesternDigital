from .__init__ import db


class Person(db.Model):

    name = db.Column(db.String(50),primary_key=True, unique=True, nullable=False)

    age = db.Column(db.Integer,primary_key=True, nullable=False)


