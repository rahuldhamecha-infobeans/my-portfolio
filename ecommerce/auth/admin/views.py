from flask import Blueprint, render_template
from ecommerce import app

auth_admin_blueprint = Blueprint('auth',__name__)

@auth_admin_blueprint.route('/login')
def admin_login():
    return render_template('auth/admin/login.html')

@auth_admin_blueprint.route('/register')
def admin_register():
    return render_template('auth/admin/register.html')


@auth_admin_blueprint.route('/forgot-password.html')
def admin_forgot_password():
    return render_template('auth/admin/forgot-password.html')




app.register_blueprint(auth_admin_blueprint,url_prefix="/admin/auth")