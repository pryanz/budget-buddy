import os
import secrets
from PIL import Image
from flask import render_template , url_for , flash , redirect , request
from app import app , db , bcrypt
from app.models import User, Transaction
from app.forms import RegistrationForm , LoginForm , TransactionForm
from flask_login import login_user , current_user, logout_user, login_required

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
            hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(username=form.username.data , email = form.email.data, password= hashed_pw)
            db.session.add(user)
            db.session.commit()
            flash('Your Account has been created! You are now able to login', 'success')
            return redirect(url_for('login'))
    return render_template('register.html', title='Register', form = form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember = form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form = form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/dashboard", methods=['GET', 'POST'])
@login_required
def dashboard():
    transactions = (
        Transaction.query
        .filter_by(user_id=current_user.id)
        .order_by(Transaction.date_time.desc())
        .all()
    )

    form = TransactionForm()
    
    if form.validate_on_submit():
        if form.amount.data <= 0:
            flash("Amount must be greater than zero", "danger")
            return redirect(url_for("dashboard"))
        amount = int(form.amount.data *100)
        if form.income.data:
            curr_tran = Transaction(amount=amount,category=form.category.data , user_id=current_user.id)
            current_user.balance += amount
            db.session.add(curr_tran)
            db.session.commit()
            flash(f"Your Income Transaction has been recorded and {form.amount.data} credited successfully",'success')
            return redirect(url_for('dashboard'))
        elif current_user.balance>=amount:
            curr_tran = Transaction(amount=-amount ,category=form.category.data , user_id=current_user.id)
            current_user.balance -= amount
            db.session.add(curr_tran)
            db.session.commit()
            flash(f"Your Expense Transaction has been recorded and {form.amount.data} debited successfully",'success')
            return redirect(url_for('dashboard'))
        else:
            flash("Balance is not sufficient to debit the said amount",'danger')
    return render_template("dashboard.html", transactions = transactions, form=form)

