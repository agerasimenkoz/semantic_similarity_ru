import json
import numpy as np

from flask import jsonify, request, make_response
from flask_restful import Resource

from similarity.utils import cos_similarity_sentences, byte_to_numpy
from db_utils.db_create import insert_default_sentence
from models import User, db, DefaultSentence
from similarity.similarity_class import BertSimilarity, similarity_factory


class Index(Resource):
    def get(self):
        ret = []
        # new_intent = User(username="test_text")
        # db.session.add(new_intent)
        # db.session.commit()
        # insert_default_sentence()
        res = DefaultSentence.query.all()
        for user in res:
            ret.append(
                {"sentence": json.dumps(user.text, ensure_ascii=False)}
            )
        return make_response(jsonify(ret, 200))


class Add(Resource):
    def get(self):
        res = User.query.all()
        new_intent = User(username=f"test_text {len(res) + 1}")
        db.session.add(new_intent)
        db.session.commit()

        return make_response(jsonify([], 200))


class HealthCheckServ(Resource):
    def get(self):
        res = DefaultSentence.query.all()
        return make_response(jsonify([res], 200))


class Similarity(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        text = json_data.get("text", None)
        response = {"message": None}
        if text:
            sentence_embedding = similarity_factory.predict_model(text)
            list_default = DefaultSentence.query.all()
            dict_default = {}
            for default_sentence in list_default:
                dict_default[default_sentence.text] = byte_to_numpy(default_sentence.numpy_model)

            similarity = cos_similarity_sentences(sentence_embedding, list(dict_default.values()))
            max_similarity = max(similarity)
            index_max_similarity = similarity.index(max(similarity))
            response["text"] = f"{list(dict_default.keys())[index_max_similarity]}"
            response["similarity"] = f"{max_similarity:.2f}"
            # response["text"] = f"{similarity}"
        else:
            response["message"] = "Please add sentence in format text='sentence'"
        return make_response(jsonify(response))
