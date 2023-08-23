from ecommerce import app
from flask import Blueprint,render_template,request,redirect,url_for,flash
from flask_login import login_required
from ecommerce.admin.decorators import has_permission
# import stripe
# from ecommerce.strip_config import stripe_key,stripe_secrete


products_blueprint = Blueprint('products',__name__)

# public_key = stripe_key
# stripe.api_key = stripe_secrete

@products_blueprint.route('/')
@has_permission('Products')
def index():
	return render_template('admin/products/index.html',public_key=public_key)

# @products_blueprint.route('/payment',methods=['post'])
# def product_payment():
# 	# CUSTOMER INFORMATION
# 	customer = stripe.Customer.create(email=request.form['stripeEmail'],source=request.form['stripeToken'])
#
# 	charge = stripe.Charge.create(customer=customer.id,amount = 200,currency='inr',description='Product Image Demo')
# 	flash('Payment Done Successfully!','success')
# 	return redirect(url_for('products.index'))



app.register_blueprint(products_blueprint,url_prefix='/admin/products')