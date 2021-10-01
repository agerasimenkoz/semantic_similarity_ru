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

```
curl http://localhost:5000/similarity -H "Content-Type: application/json" -d '{"text": "you_sentence"}'
curl -i -X GET -H "Content-Type: application/json" -d "{\"text\":\"привет\"}" http://localhost:5000/similarity
```

## Running the tests

## Deployment

## Built With

* [Docker](https://docs.docker.com/) -  Deployment model
* [Flask](https://flask.palletsprojects.com/en/2.0.x/) - The web framework
* [Python](https://www.python.org/) - programming language
* [pip](https://pypi.org/project/pip/) - Package and dependency manager
* [MySQL](https://www.mysql.com/) - Database

## Contributing

## Versioning

## Authors

## License

## Acknowledgments
