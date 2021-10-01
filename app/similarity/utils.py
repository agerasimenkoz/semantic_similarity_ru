from typing import List
import numpy as np
from io import BytesIO
from sklearn.metrics.pairwise import cosine_similarity


def cos_similarity_sentences(sentence_check: str, list_other_sentence: List[str]):
    return cosine_similarity(
        [sentence_check],
        list_other_sentence
    )[0].tolist()


def numpy_to_byte(array_data):
    np_bytes = BytesIO()
    np.save(np_bytes, array_data, allow_pickle=True)
    np_bytes.seek(0)
    return np_bytes.getvalue()


def byte_to_numpy(byte_data):
    serialized_bytes = BytesIO(byte_data)
    serialized_bytes.seek(0)
    loaded_np = np.load(serialized_bytes, allow_pickle=True)
    return loaded_np
