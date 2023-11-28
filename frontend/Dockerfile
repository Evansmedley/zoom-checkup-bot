FROM node:20-alpine

WORKDIR /app

COPY package.json /
COPY src/ /src
COPY public/ /public

# TODO: fix dependenciess to remove force
RUN npm install --force

CMD ["npm", "start"]