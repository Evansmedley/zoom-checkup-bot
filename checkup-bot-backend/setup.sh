#!/bin/bash

# Package project
mvn package

# Build docker image
docker build -t checkup-bot-backend .

# Run docker images with docker-compose
docker compose up -d
