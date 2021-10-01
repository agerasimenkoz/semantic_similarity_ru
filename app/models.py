from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, Unicode, Text, LargeBinary, Float, ForeignKey, Boolean

db = SQLAlchemy()


class SentenceSimilarity(db.Model):
    """
    Create an sentence table to store requests
    """
    __tablename__ = 'sentence_similarity'
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8', 'mysql_collate': 'utf8_unicode_ci'}
    id = Column(Integer, primary_key=True)
    text = Column(String(1200), nullable=False)
    timestamp = Column(DateTime,
                       default=datetime.utcnow,
                       onupdate=datetime.utcnow)
    ids_default = db.relationship('DefaultSimilarity', backref='sentence_similar')

    def __repr__(self):
        return '<SentenceSimilarity %r>' % self.text


class DefaultSimilarity(db.Model):
    """
    Create auxiliary table for SentenceSimilarity
    """
    __tablename__ = 'default_similarity'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_default = Column(Integer, nullable=False)
    similarity_val = Column(Float, nullable=False)
    the_best = Column(Boolean, nullable=True, default=False)

    id_sentence = Column(Integer, ForeignKey('sentence_similarity.id'), nullable=True)


class DefaultSentence(db.Model):
    """
    Create immutable table with default sentences for compare
    """
    __tablename__ = 'default_sentence'
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8', 'mysql_collate': 'utf8_unicode_ci'}

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(120, collation='utf8_unicode_ci'), unique=True, nullable=False)
    numpy_model = Column(LargeBinary, unique=False, nullable=True)

    def __repr__(self):
        return '<DefaultSentence %r>' % self.text
