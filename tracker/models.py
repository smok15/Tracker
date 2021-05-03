from tracker import db,login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    #cars = db.relationship('Cars', backref='właściciele', lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.id}','{self.password}')"


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    map = db.Column(db.String(20), unique=True)
    #user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f"Car(''{self.id}','{self.map}')"