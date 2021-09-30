from transformers import AutoModel, AutoTokenizer
import numpy as np
import torch


class BertSimilarity:
    def __init__(self):
        self.model_name = "DeepPavlov/rubert-base-cased-sentence"
        self.device = "cuda:0" if torch.cuda.is_available() else "cpu"
        self.model = None
        self.tokenizer = None
        self.sentence_embedding = np.array([])

        self.read_model()

    # Download pytorch model
    def read_model(self):
        self.model = AutoModel.from_pretrained(self.model_name).to(self.device)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.tokenizer.pad_token = self.tokenizer.eos_token
        print(f"model {self.model_name} has been loaded")
        # return model, tokenizer

    def predict_model(self, data):
        inputs = self.tokenizer(data, return_tensors="pt").to(self.device)
        outputs = self.model(**inputs)
        self.sentence_embedding = self.mean_pooling(outputs.last_hidden_state, inputs['attention_mask'])
        # return sentence_embedding.cpu().detach().numpy()[0]

    # def similarity_model_processing(self, dataframe_processing, model, tokenizer):
    #     result_model = np.array([], dtype=np.float32)
    #     time_check = datetime.now()
    #     num_bad_similarity = 0
    #     for i, list_sentence in enumerate(dataframe_processing):
    #         sentence_embeddings = []
    #         for sentence in list_sentence:
    #             sentence_embeddings.append(predict_model(sentence, model, tokenizer))
    #         if (i % 100 == 0):
    #             print(f"complete {i} row")
    #         if len(sentence_embeddings) >= 2:
    #             similarity = cosine_similarity(
    #                 [sentence_embeddings[0]],
    #                 sentence_embeddings[1:]
    #             )[0]
    #             if similarity.mean() < 0.5:
    #                 num_bad_similarity += 1
    #                 print(f"""
    #               Similarity for {i} sentence = {similarity.mean()} \n
    #               {".| ".join(list_sentence)}
    #               """
    #                       )
    #             result_model = np.concatenate((result_model, similarity))
    #     print(f"Time complete {datetime.now() - time_check}")
    #     return result_model, num_bad_similarity / dataframe_processing.shape[0]

    # Mean Pooling - Take attention mask into account for correct averaging
    @staticmethod
    def mean_pooling(token_embeddings, attention_mask):
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        sum_embeddings = torch.sum(token_embeddings * input_mask_expanded, 1)
        sum_mask = torch.clamp(input_mask_expanded.sum(1), min=1e-9)
        return sum_embeddings / sum_mask


