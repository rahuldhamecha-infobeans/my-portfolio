from flask import Blueprint, render_template,redirect,request,url_for,flash,abort
from ecommerce import app
from ecommerce.auth.admin.forms import LoginForm,RegistrationForm
from ecommerce.database.models.User import User
from flask_login import login_user,logout_user,login_required
from ecommerce.database import db

auth_admin_blueprint = Blueprint('auth',__name__)

@auth_admin_blueprint.route('/login',methods=['GET','POST'])
def admin_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            flash('Logged in Successfully!')
            next = request.args.get('next')

            if next == None or not next[0] == '/':
                next = url_for('dashboard.index')

            return redirect(next)
        else:
            flash('Email Or Password Not Matched.')

    return render_template('auth/admin/login.html',form=form)

@auth_admin_blueprint.route('/register',methods=['GET','POST'])
def admin_register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for registration!')
        return redirect(url_for('auth.admin_login'))

    return render_template('auth/admin/register.html',form=form)


@auth_admin_blueprint.route('/forgot-password.html')
def admin_forgot_password():
    return render_template('auth/admin/forgot-password.html')

@auth_admin_blueprint.route('/logout')
def admin_logout():
    logout_user()
    return redirect(url_for('auth.admin_login'))




app.register_blueprint(auth_admin_blueprint,url_prefix="/admin/auth")