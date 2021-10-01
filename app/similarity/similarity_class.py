from transformers import AutoModel, AutoTokenizer
import numpy as np
import torch


class BertSimilarity:
    def __init__(self):
        # self.model_name_or_path = "DeepPavlov/rubert-base-cased-sentence"
        self.model_name_or_path = "/rubert"
        self.device = "cuda:0" if torch.cuda.is_available() else "cpu"
        self.model = None
        self.tokenizer = None
        self.sentence_embedding = np.array([])

        self._read_model()

    # Download pytorch model
    def _read_model(self):
        self.model = AutoModel.from_pretrained(self.model_name_or_path, local_files_only=True).to(self.device)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name_or_path, local_files_only=True)
        self.tokenizer.pad_token = self.tokenizer.eos_token
        print(f"model {self.model_name_or_path} has been loaded")
        # return model, tokenizer

    def predict_model(self, data):
        inputs = self.tokenizer(data, return_tensors="pt").to(self.device)
        outputs = self.model(**inputs)
        self.sentence_embedding = self._mean_pooling(outputs.last_hidden_state, inputs['attention_mask'])
        self.sentence_embedding = self.sentence_embedding.cpu().detach().numpy()[0]
        return self.sentence_embedding

    # Mean Pooling - Take attention mask into account for correct averaging
    @staticmethod
    def _mean_pooling(token_embeddings, attention_mask):
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        sum_embeddings = torch.sum(token_embeddings * input_mask_expanded, 1)
        sum_mask = torch.clamp(input_mask_expanded.sum(1), min=1e-9)
        return sum_embeddings / sum_mask

# Init Model with server
similarity_factory = BertSimilarity()