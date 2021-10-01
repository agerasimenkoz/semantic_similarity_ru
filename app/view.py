from flask import jsonify, request, make_response
from flask_restful import Resource

from db_utils.utils import write_sentence_similarities_to_db
from similarity.utils import cos_similarity_sentences, byte_to_numpy
from db_utils.health_check import check_db, check_model
from models import DefaultSentence
from similarity.similarity_class import similarity_factory


class HealthCheckServ(Resource):
    def get(self):
        response = {"message": None}
        try:
            check_db()
            check_model()
            response["message"] = "API work"
        except Exception:
            response["message"] = "API don't work! Something is broken"

        return make_response(jsonify(response))


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
                dict_default[default_sentence.text] = {
                    "narray": byte_to_numpy(default_sentence.numpy_model),
                    "id": default_sentence.id,
                }
            narrays = [item["narray"] for item in dict_default.values()]
            similarity = cos_similarity_sentences(sentence_embedding, narrays)
            max_similarity = max(similarity)
            index_max_similarity = similarity.index(max(similarity))

            for (_, item), similarity_item in zip(dict_default.items(), similarity):
                item["similarity"] = similarity_item
                item["best"] = True if similarity_item == max_similarity else False

            write_sentence_similarities_to_db(dict_default, text)

            response["text"] = f"{list(dict_default.keys())[index_max_similarity]}"
            response["similarity"] = f"{max_similarity:.2f}"
        else:
            response["message"] = "Please add sentence in format text='sentence'"
        return make_response(jsonify(response))
