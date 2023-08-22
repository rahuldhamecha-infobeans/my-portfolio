from flask import Flask, render_template


# Create Ecommerce App To Use in multiple files
def create_ecommerce_app():
    app = Flask(__name__)
    return app


app = create_ecommerce_app()
app.config['SECRET_KEY'] = 'ecommerce_secret_key'



import ecommerce.register_application
