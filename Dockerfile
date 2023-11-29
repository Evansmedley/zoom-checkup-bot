FROM node:20-alpine

EXPOSE 3000:3000

WORKDIR /app/

COPY frontend/package.json /app/
COPY frontend/src/ /app/src
COPY frontend/public/ /app/public

# TODO: fix dependenciess to remove force
RUN npm install --force

CMD ["npm", "start"]

FROM openjdk:17-jdk-alpine

WORKDIR /app

EXPOSE 8080:8080

COPY /checkup-bot-backend/target/*.jar app.jar

FROM nginx:alpine

ADD nginx/nginx.conf /etc/nginx/

ENTRYPOINT ["java","-jar","/app/app.jar"]