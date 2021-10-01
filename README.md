# Flask-Docker-MySQL Semantic Similarity Ru
https://habr.com/ru/post/564916/
This project can be used to run flask app with MySQL as DB using docker-compose.

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

**Step 4:** Open up the browser and paste the below url

```
http://localhost:5000/
```
To check the database in the container phpMyAdmin is used at url 
```
http://localhost:5010/
```
## Running the tests
```
curl http://localhost:5000/similarity -H "Content-Type: application/json" -d '{"text": "you_sentence"}'
```
Responce come in the format json as 

{"message":"message Error","similarity":"max similarity for sentence","text":"the best sentence"}

You can use instead script test_request.py in semantic_similarity_ru folder
## Deployment

## Built With

* [Docker](https://docs.docker.com/) -  Deployment model
* [Flask](https://flask.palletsprojects.com/en/2.0.x/) - The web framework
* [Python](https://www.python.org/) - programming language
* [pip](https://pypi.org/project/pip/) - Package and dependency manager
* [MySQL](https://www.mysql.com/) - Database

## Used Model
* [DeepPavlov](https://huggingface.co/DeepPavlov/rubert-base-cased-sentence) -  BERT Model

## Improvement
* Fine-tuning Model
* Check other metrics
## Authors

## License

## Acknowledgments
