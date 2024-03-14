FROM node:20-alpine

EXPOSE 8080:8080

WORKDIR /app/

COPY package.json /app/
COPY src/ /app/src
COPY public/ /app/public

ENV PORT 8080

# TODO: fix dependenciess to remove force
RUN npm install --force

CMD ["npm", "start"]