from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from tracker.models import User, Car


class RegistrationForm(FlaskForm):
    username = StringField('Login', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    confirm_password = PasswordField('Potwierdź Hasło', validators=[DataRequired(), EqualTo('password')])
    sumbit = SubmitField('Zarejestruj')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Login Zajęty')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email zajęty')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    remember = BooleanField('Zapamiętaj Logowanie')
    submit = SubmitField('Zaloguj')


class AddACarForm(FlaskForm):
    id = StringField('Id Pojazdu', validators=[DataRequired()])
    plate = StringField('Numer Rejestracyjny', validators=[DataRequired()])
    brand = StringField('Marka Pojazdu')
    sumbit = SubmitField('Dodaj')

    def validate_id(self, id):
        car = Car.query.filter_by(id=id.data).first()
        if car:
            raise ValidationError('Pjazd Dodany')
