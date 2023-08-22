from ecommerce import app
from flask import Blueprint,render_template
from flask_login import login_required

user_blueprint = Blueprint('users',__name__)
@user_blueprint.route('/')
@login_required
def index():
	return render_template('admin/users/index.html')



app.register_blueprint(user_blueprint,url_prefix='/admin/users')