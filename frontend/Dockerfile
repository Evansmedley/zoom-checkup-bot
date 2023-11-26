FROM node:20.10.0-alpine3.18

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json ./
COPY package-lock.json ./
RUN npm install --force

COPY . ./

CMD ["npm", "start"]