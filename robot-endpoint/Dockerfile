FROM python:3.9.18-slim-bullseye

WORKDIR /python-docker

EXPOSE 8080:8080

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ARG SERVER_ADDRESS
ENV SERVER_ADDRESS ${SERVER_ADDRESS}
ARG CLIENT_ADDRESS
ENV CLIENT_ADDRESS ${CLIENT_ADDRESS}

CMD python3 main.py -n cloud-endpoint -s ${SERVER_ADDRESS} -u ${CLIENT_ADDRESS} -p 8080 -d --hostname