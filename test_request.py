import requests
import json


def main(text):
    headers = {
        'Content-type': 'application/json',
    }
    data = json.dumps({"text": text})
    response = requests.post('http://localhost:5000/get_intent', headers=headers, data=data)
    return response.json()


if __name__ == '__main__':
    response = main("библиотека")
    print(response.get("text", None))
