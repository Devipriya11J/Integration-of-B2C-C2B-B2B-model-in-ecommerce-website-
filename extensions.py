from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_mail import Mail

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
mail = Mail()

def init_extensions(app):
    # Initialize extensions with app
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info' 