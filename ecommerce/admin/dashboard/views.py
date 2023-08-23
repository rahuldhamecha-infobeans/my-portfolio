from ecommerce import app
from flask import Blueprint,render_template
from flask_login import login_required
from ecommerce.admin.decorators import has_permission

dashboard_blueprint = Blueprint('dashboard',__name__)
@dashboard_blueprint.route('/')
@has_permission('Dashboard')
def index():
	return render_template('admin/dashboard/index.html')


app.register_blueprint(dashboard_blueprint,url_prefix='/admin/dashboard')