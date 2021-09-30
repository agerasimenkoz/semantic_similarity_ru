from flask_sqlalchemy import SQLAlchemy

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
