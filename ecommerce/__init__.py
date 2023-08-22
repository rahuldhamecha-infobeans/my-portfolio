from flask import Flask,render_template

# Create Ecommerce App To Use in multiple files
def create_ecommerce_app():
	app = Flask(__name__)
	return app

app = create_ecommerce_app()
app.config['SECRET_KEY'] = 'ecommerce_secret_key'

@app.route('/admin/dashboard')
def dashboard():
	return render_template('admin/dashboard/index.html')

import ecommerce.register_application