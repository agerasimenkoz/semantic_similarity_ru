from flask import jsonify, request
from flask_restful import Resource

# from db_utils.db_create import insert_default_sentence
from models import User, db, DefaultSentence
from similarity.similarity_class import BertSimilarity




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
                {
                    'username': user.text,
                }
            )
        return jsonify(ret, 200)


class Add(Resource):
    def get(self):
        res = User.query.all()
        new_intent = User(username=f"test_text {len(res) + 1}")
        db.session.add(new_intent)
        db.session.commit()

        return jsonify([], 200)


class HealthCheckServ(Resource):
    def get(self):
        res = DefaultSentence.query.all()
        return jsonify([res], 200)


class Similarity(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        text = json_data.get("text", None)
        response = {}
        if text:
            print(str(text))
            sentence_embedding = BertSimilarity().predict_model(text)
            response["message"] = f"{sentence_embedding}"
        else:
            response["message"] = "Please add sentence in format text='sentence'"
        return jsonify(response, 200)
