from flask import Flask

# Create Ecommerce App To Use in multiple files
def create_ecommerce_app():
	app = Flask(__name__)
	return app

app = create_ecommerce_app()

import ecommerce.register_application