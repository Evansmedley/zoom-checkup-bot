FROM openjdk:17-jdk-alpine

WORKDIR /app

EXPOSE 8080

COPY checkup-bot-backend/target/*.jar app.jar

ENTRYPOINT ["java","-jar","/app/app.jar"]