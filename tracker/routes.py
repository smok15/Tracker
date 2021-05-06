from flask import render_template, url_for, flash, redirect, request
from tracker import app, db, bcrypt
from tracker.form import RegistrationForm, LoginForm, AddACarForm
from flask_login import login_user, current_user, logout_user, login_required
from tracker.models import User, Car
import folium, os

map = folium.Map(location=[51.7470283, 19.4145344], zoom_start=13)
routeData = os.path.join("tracker/data1.geojson")
folium.GeoJson(routeData, name='trasa').add_to(map)
map.save('tracker/templates/map.html')


@app.route("/")
def home():
    return render_template('home.html',)


@app.route("/trasa")
def trasa():
    return render_template('trasa.html', title='Trasa')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Konto zostało utworzone', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Logowanie nie powiodło się, spóbuj ponownie', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/addacar", methods=['GET', 'POST'])
def addacar():
    form = AddACarForm()
    if form.validate_on_submit():
        car = Car(id=form.id.data, plate=form.plate.data, brand=form.brand.data)
        db.session.add(car)
        db.session.commit()
        flash(f'Pojazd został dodany!', 'success')
        return redirect(url_for('account'))
    return render_template('addacar.html', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html',query=Car.query.all())

