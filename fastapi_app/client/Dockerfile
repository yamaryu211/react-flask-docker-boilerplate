FROM node:16.8-alpine3.14

EXPOSE 3000
EXPOSE 35729

RUN mkdir /frontend
WORKDIR /frontend
COPY package.json /frontend/package.json

RUN npm install
