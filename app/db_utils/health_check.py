from models import db
from similarity.similarity_class import similarity_factory
from sqlalchemy.sql import text


def check_db():
    # db.session.query("1").from_statement(text("SELECT 1")).all()
    db.engine.execute(text("SELECT 1"))


def check_model():
    similarity_factory.predict_model("test")