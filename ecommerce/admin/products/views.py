from ecommerce import app
from flask import Blueprint,render_template
from flask_login import login_required
from ecommerce.admin.decorators import has_permission

products_blueprint = Blueprint('products',__name__)
@products_blueprint.route('/')
@has_permission('Products')
def index():
	return render_template('admin/products/index.html')


app.register_blueprint(products_blueprint,url_prefix='/admin/products')