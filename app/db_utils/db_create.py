import os
from models import db, DefaultSentence
# from app.models import DefaultSentence, db


def get_default_sentence_from_file(file_path):
    list_sentences = []
    print(f"Is file {os.path.isfile(file_path)}")
    if os.path.isfile(file_path):
        with open(file_path, "r") as file_data:
            for line in file_data:
                list_sentences.append(line.strip())
    return list_sentences


def insert_default_sentence(*args, **kwargs):
    sentences = get_default_sentence_from_file("db_utils/default_sentence.txt")
    print(f"{sentences}")
    default_sentence = DefaultSentence.query.all()
    list_default_text = []
    if len(default_sentence) != 0:
        list_default_text = list(map(lambda x: x.text, default_sentence))
    for sentence in sentences:
        if sentence not in list_default_text:
            print(f"Added {sentence} to default table")
            db.session.add(DefaultSentence(text=sentence))
            db.session.commit()

