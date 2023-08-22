from ecommerce import app
from flask_login import LoginManager

login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'auth.admin_login'

import ecommerce.auth.admin.views