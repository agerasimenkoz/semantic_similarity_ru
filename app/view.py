from flask import jsonify, request
from flask_restful import Resource

from models import User, db
# from app import similarity_factory


class Index(Resource):
    def get(self):
        ret = []
        # new_intent = User(username="test_text")
        # db.session.add(new_intent)
        # db.session.commit()

        res = User.query.all()
        for user in res:
            ret.append(
                {
                    'username': user.username,
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


# class HealthCheck(Resource):
#     def get(self):
#         return jsonify([], 200)
#
#
# class Similarity(Resource):
#     def post(self):
#         json_data = request.get_json(force=True)
#         text = json_data.get("text", None)
#         response = {}
#         if text:
#             pass
#         else:
#             response["message"] = "Please add sentence in format text='sentence'"
#             return jsonify(response, 200)
