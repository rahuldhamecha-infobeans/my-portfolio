from ecommerce import app
from flask import Blueprint,render_template
from flask_login import login_required

permissions_blueprint = Blueprint('permissions',__name__)
@permissions_blueprint.route('/')
@login_required
def index():
	return render_template('admin/permissions/index.html')



app.register_blueprint(permissions_blueprint,url_prefix='/admin/permissions')