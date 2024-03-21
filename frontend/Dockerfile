FROM node:20-alpine

EXPOSE 8080:8080

WORKDIR /app/

COPY package.json /app/
COPY src/ /app/src
COPY public/ /app/public

ENV PORT 8080
ARG REACT_APP_HOSTNAME
ENV REACT_APP_HOSTNAME ${REACT_APP_HOSTNAME}

# TODO: fix dependenciess to remove force
RUN npm install --force

RUN npm run build

RUN npm install -g serve

CMD serve -s build