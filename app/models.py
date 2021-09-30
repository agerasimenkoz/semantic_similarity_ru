from flask_sqlalchemy import SQLAlchemy

from db_utils.db_create import get_default_sentence_from_file

db = SQLAlchemy()


class User(db.Model):
    """
    Create an Employee table
    """
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False)

    def __repr__(self):
        return '<User %r>' % self.username


class SentenceSimilarity(db.Model):
    """
    Create an Employee table
    """
    __tablename__ = 'sentence_similarity'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1200), unique=True, nullable=False)
    similarity = db.Column(db.String(1200), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.text


class DefaultSentence(db.Model):
    """
    Create an Employee table
    """
    __tablename__ = 'default_sentence'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1200), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.text

    @staticmethod
    def create_table():
        sentences = get_default_sentence_from_file("default_sentence.txt")
        default_sentence = DefaultSentence.query.all()
        list_default_text = []
        if len(default_sentence) != 0:
            list_default_text = list(map(lambda x: x.text, default_sentence))
        for sentence in sentences:
            if sentence not in list_default_text:
                db.session.add(DefaultSentence(text=sentence))
        db.session.commit()
