import os
from flask import Flask
from flask_restful import Api

from db_utils.db_create import insert_default_sentence
from models import db
from view import HealthCheckServ, Similarity

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()

api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}?charset=utf8'.format(
    os.getenv('DB_USER', 'flask'),
    os.getenv('DB_PASSWORD', ''),
    os.getenv('DB_HOST', 'mysql'),
    os.getenv('DB_NAME', 'flask')
)
app.config['MYSQL_DATABASE_CHARSET'] = 'utf8mb4'
app.config['MYSQL_CHARSET'] = 'utf8mb4'

# For Unicode in response
app.config['JSON_AS_ASCII'] = False

db.init_app(app)


# create the DB on demand
@app.before_first_request
def create_tables():
    db.create_all()
    # Initial Default Sentences
    insert_default_sentence()


api.add_resource(HealthCheckServ, '/health_check')
api.add_resource(Similarity, '/get_intent')
