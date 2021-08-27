from flask import render_template, url_for, flash, redirect, request, jsonify
from bancoin import app, db, bcrypt
from bancoin.models import User
from bancoin.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required
from flask_cors import cross_origin


@app.route('/')
@app.route('/home')
def home():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    else:
        return jsonify({"msg": "Hello world!"}), 201

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.name.data}!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
@cross_origin()
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data): 
            login_user(user, remember=form.remember.data)
            flash(f'Welcome!', 'success')
            next_page = request.args.get('next')
            return redirect(url_for(next_page.strip('/'))) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check credentials.', 'danger')

    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')