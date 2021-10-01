# Flask-Docker-MySQL Semantic Similarity Ru

This project can be used to determine the semantic similarity of sentences. Based on the DeepPavlov model. Flask API with MySQL as DB using docker-compose.

## Colab Comparison of models RuGPT-3 (sber) and RuBERT (deeppavlov) for STS
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1kmu-FOh1004cibP9sGrKm0E8hQBVylR4?usp=sharing)

## Getting Started

**Step 1:** Make sure git is installed on your os.

On ubuntu, you can install the git using  ```apt install git```

**Step 2:** Clone the project into your local machine using below command.

```git clone https://github.com/agerasimenkoz/semantic_similarity_ru.git```

### Prerequisites

**1. Docker**

Make sure you have Docker installed.

```https://docs.docker.com/compose/install/```

### Installing

**Step 1:** Change to the directory where the project was cloned in previous step.

```
cd semantic_similarity_ru
```

**Step 2:** Make sure Docker is up and running.

**Step 3:** Run

```
docker-compose up --build
```

**Step 4:** Check API

```
http://localhost:5000/health_check
```
or
```
curl http://localhost:5000/health_check
```


To check the database in the container phpMyAdmin is used at url 
```
http://localhost:5010/
```
## Running the tests
```
curl http://localhost:5000/get_intent -H "Content-Type: application/json" -d '{"text": "you_sentence"}'
```
Responce come in the format json as 

{"message":"message Error","similarity":"max similarity for sentence","text":"the best sentence"}

You can use instead script test_request.py in semantic_similarity_ru folder

## Built With

* [Docker](https://docs.docker.com/) -  Deployment model
* [Flask](https://flask.palletsprojects.com/en/2.0.x/) - The web framework
* [Python](https://www.python.org/) - programming language
* [pip](https://pypi.org/project/pip/) - Package and dependency manager
* [MySQL](https://www.mysql.com/) - Database

## Used Model
* [DeepPavlov](https://huggingface.co/DeepPavlov/rubert-base-cased-sentence) -  BERT Model

## Possible Future Improvements
* Fine-tuning Model
* Check other metrics for a more accurate comparison of models and texts. Such as pearson correlation, manhattan distance
* Check other models. For example [sentence-transformers](https://huggingface.co/sentence-transformers)
* Open datasets for STS. [15 pieces](https://paperswithcode.com/datasets?task=semantic-textual-similarity)

## License
[License](LICENSE)
