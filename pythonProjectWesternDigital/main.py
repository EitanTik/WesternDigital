from flask import Blueprint, request, redirect
from .models import Person
from .__init__ import db
import requests

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return 'Home route.'



@main.route('/get_person', methods=['GET'])
def get_person():
    name = request.args.get("name", type=str)
    person = Person.query.filter_by(name=name).first()

    # ask for the name and get the age of the person
    if person:
        return "I found this person, he/she is " + str(person.age) + " years old."
    else:
        return "Who is that???"


@main.route('/post_person', methods=['GET','POST'])
def post_person():
    # get the persons name from the user
    name = request.args.get("name",type=str)
    age = request.args.get("age",type=int)
    person = Person.query.filter_by(name=name).first()
    if person:
        return "This person's name already exists, and he/she is "+str(person.age) +" years old."

    new_person = Person(name=name, age=age)
    db.session.add(new_person)
    db.session.commit()
    return "Added a new person to our system."

@main.route('/put_person', methods=['GET','PUT','DELETE'])
def put_person():
    # get the persons name from the user
    name = request.args.get("name",type=str)
    age = request.args.get("age",type=int)

    person = Person.query.filter_by(name=name).first()
    if not person:
        new_person = Person(name=name, age=age)
        db.session.add(new_person)
        db.session.commit()
        return "Added a new person to our system."
    else:
        new_person = Person(name=name, age=age)
        db.session.delete(person)
        db.session.commit()
        db.session.add(new_person)
        db.session.commit()
        return "This person existed, I updated what needed updating if needed."

@main.route('/delete_person', methods=['GET','DELETE'])
def delete_person():
    # get the persons name from the user
    name = request.args.get("name", type=str)
    person = Person.query.filter_by(name=name).first()
    if not person:
        return "Delete? This person does not exist in our system to begin with."
    else:
        db.session.delete(person)
        db.session.commit()
        return name + ", has been deleted from our system."








