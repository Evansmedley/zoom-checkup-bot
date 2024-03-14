FROM python:3.8-slim-buster

WORKDIR /python-docker

EXPOSE 8080:8080

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ARG SERVER_ADDRESS

CMD [ "python3", "main.py", "-n", "cloud", "-s", "${SERVER_ADDRESS}", "-p", "8080", "-d", "-l" ]