FROM node:20-alpine

WORKDIR /app/

COPY package.json /app/
COPY src/ /app/src
COPY public/ /app/public

# TODO: fix dependenciess to remove force
RUN npm install --force

CMD ["npm", "start"]