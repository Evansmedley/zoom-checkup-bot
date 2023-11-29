FROM node:20-alpine

EXPOSE 3000:3000

WORKDIR /app/

COPY package.json /app/
COPY src/ /app/src
COPY public/ /app/public

# TODO: fix dependenciess to remove force
RUN npm install --force

CMD ["npm", "start"]