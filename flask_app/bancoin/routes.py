from flask import render_template, url_for, flash, redirect, request, jsonify
from bancoin import app, db, bcrypt
from bancoin.models import Transaction, User, Product
from bancoin.forms import RegistrationForm, LoginForm, TransactionForm
from flask_login import login_user, current_user, logout_user, login_required
from flask_cors import cross_origin


@app.route('/')
@app.route('/home')
def home():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    else:
        return render_template('home.html', title='Login')

@app.route('/transactions')
def transactions():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    else:
        return render_template('transactions.html', title='Transactions')


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

@app.route("/new-transaction", methods=['GET', 'POST'])
def new_transaction():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    form = TransactionForm()
    form.product_id.choices = [(p.id, p.name) for p in Product.query.order_by('name')]
    if form.validate_on_submit():
        transaction = Transaction(
            quantity=form.quantity.data, 
            intention=form.intention.data,
            product_id=form.product_id.data,
            user_id=current_user.id
            )
        db.session.add(transaction)
        db.session.commit()
        flash(f'Transaction Created Successfully!', 'success')
        return redirect(url_for('transactions'))
    return render_template('new_transaction.html', title='New Transaction', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')