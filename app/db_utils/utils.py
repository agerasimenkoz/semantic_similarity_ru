from models import db, DefaultSimilarity, SentenceSimilarity
from typing import Dict


def write_sentence_similarities_to_db(dict_sentences_similarity: Dict, text_sentence: str):
    db_new_sentence_similarity = SentenceSimilarity(text=text_sentence)
    db.session.add(db_new_sentence_similarity)
    db.session.flush()
    db.session.refresh(db_new_sentence_similarity)

    for key, sentence_similarity in dict_sentences_similarity.items():
        db_new_def_similarity = DefaultSimilarity(id_default=sentence_similarity["id"],
                                                  similarity_val=sentence_similarity["similarity"],
                                                  the_best=sentence_similarity["best"],
                                                  id_sentence=db_new_sentence_similarity.id)
        db.session.add(db_new_def_similarity)
        db.session.flush()

        db.session.refresh(db_new_def_similarity)
        db_new_sentence_similarity.ids_default.append(db_new_def_similarity)

    db.session.add(db_new_sentence_similarity)
    db.session.commit()
    pass
