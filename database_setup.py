import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
from flask_migrate import Migrate

# ---------------------------> App Config <---------------------#

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# --------------------------> Model <-----------------------------#
class Restaurant(db.Model):
    __tablename__ = 'restaurant'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    menuItem = db.relationship('MenuItem', backref='restaurants')

    def __repr__(self):
        return f'<Restaurant {self.id}, {self.name}>'

class MenuItem(db.Model):
    __tablename__ = 'menu_item'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(250))
    price = db.Column(db.String(8))
    course = db.Column(db.String(250))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))

    def __repr__(self):
        return f'<MenuItem {self.name} {self.description} {self.price}>'
