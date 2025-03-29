from flask import Flask
from spectro_api.config.config import config
from spectro_api.routes import register_routes
from spectro_api.models import db

app = Flask(__name__)

app.config.from_pyfile('/spectro_api/config/config.py')

register_routes(app)

app.config['SQLALCHEMY_DATABASE_URL'] = config.getenv('DATABASE_URL')
db.init_app(app)

if __name__ == '__main__':
  app.run(debug=True)