FROM openjdk:17-jdk-alpine

WORKDIR /app

COPY checkup-bot-backend/target/*.jar app.jar

ENTRYPOINT ["java","-jar","/app/app.jar"]