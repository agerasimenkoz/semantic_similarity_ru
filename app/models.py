from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

# from db_utils.db_create import get_default_sentence_from_file
# from db_utils.db_create import get_default_sentence_from_file
from sqlalchemy import Column, Integer, String, DateTime, Unicode, Text

db = SQLAlchemy()


class User(db.Model):
    """
    Create an Employee table
    """
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=False)

    def __repr__(self):
        return '<User %r>' % self.username


class SentenceSimilarity(db.Model):
    """
    Create an Employee table
    """
    __tablename__ = 'sentence_similarity'
    id = Column(Integer, primary_key=True)
    text = Column(String(1200), unique=True, nullable=False)
    similarity = Column(String(1200), unique=True, nullable=False)
    timestamp = Column(DateTime,
                       default=datetime.utcnow,
                       onupdate=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.text


class DefaultSentence(db.Model):
    """
    Create an Employee table
    """
    __tablename__ = 'default_sentence'
    id = Column(Integer, primary_key=True)
    text = Column(String(1200), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.text

    # @staticmethod
    # def create_table(*args, **kwargs):
    #     sentences = get_default_sentence_from_file("default_sentence.txt")
    #     default_sentence = DefaultSentence.query.all()
    #     list_default_text = []
    #     if len(default_sentence) != 0:
    #         list_default_text = list(map(lambda x: x.text, default_sentence))
    #     for sentence in sentences:
    #         print(f"Added {sentence} to default table")
    #         if sentence not in list_default_text:
    #             db.session.add(DefaultSentence(text=sentence))
    #     db.session.commit()
