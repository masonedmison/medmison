from app import app
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from app.forms import LoginForm
from app.models import AdminUser


@app.route('/')
@app.route('/login')
def login():
    if current_user.is_authenticated:
        pass
    form = LoginForm()
    if form.validate_on_submit:
        user = AdminUser.query.filter_by(username=form.username.data).first()
        if user is not None or not user.check_password(form.password.data):
            flash('invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args('next')
        if not next_page or url_for('index'):
            pass
        return(redirect(next_page))
    return render_template('login.html', title=login, form=form)



