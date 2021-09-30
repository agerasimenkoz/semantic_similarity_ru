import os
import json
from flask import Flask
from flask_restful import Api

from view import Index, Add
from models import db
from healthcheck import HealthCheck
# from serializers import AlchemyEncoder
from similarity.similarity_class import BertSimilarity

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()

api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'.format(
    os.getenv('DB_USER', 'flask'),
    os.getenv('DB_PASSWORD', ''),
    os.getenv('DB_HOST', 'mysql'),
    os.getenv('DB_NAME', 'flask')
)
# db = SQLAlchemy(app)
db.init_app(app)

# health = HealthCheck()
# # Add a flask route to expose information
# app.add_url_rule('/healthcheck', 'healthcheck', view_func=lambda: health.check())
# similarity_factory = BertSimilarity()


# create the DB on demand
@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Index, '/')
api.add_resource(Add, '/add')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)
