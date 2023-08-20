from ecommerce import app
from flask import Blueprint, render_template

public_blueprint = Blueprint('front',__name__)

@public_blueprint.route('/')
def index():
    return "<h1>Homepage</h1>"

app.register_blueprint(public_blueprint,url_prefix='/')