import os
# from models import db, DefaultSentence


def get_default_sentence_from_file(file_path):
    list_sentences = []
    if os.path.isfile(file_path):
        with open(file_path, "r") as file_data:
            for line in file_data:
                list_sentences.append(line)
    return list_sentences


# def insert_default_sentence(*args, **kwargs):
#     sentences = get_default_sentence_from_file("default_sentence.txt")
#     default_sentence = DefaultSentence.query.all()
#     list_default_text = []
#     if len(default_sentence) != 0:
#         list_default_text = list(map(lambda x: x.text, default_sentence))
#     for sentence in sentences:
#         if sentence not in list_default_text:
#             db.session.add(DefaultSentence(text=sentence))
#     db.session.commit()

