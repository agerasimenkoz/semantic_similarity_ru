# FROM python:3.7.4-alpine3.10
FROM python:3.8
# apt is the ubuntu command line tool for advanced packaging tool(APT) for sw upgrade '''

RUN apt update && \
    apt install -y netcat-openbsd
# RUN apk add --no-cache --virtual .build-deps g++ python3-dev libffi-dev openssl-dev && \
#     apk add --no-cache --update python3 && \
RUN    pip3 install --upgrade pip setuptools
RUN pip3 install pendulum service_identity
RUN mkdir /app
WORKDIR /app
RUN pip install PyMySQL
COPY app/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY app /app
ENTRYPOINT ["python"]
CMD ["app.py"]
