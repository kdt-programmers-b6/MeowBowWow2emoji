FROM node:lts-alpine

RUN mkdir /srv/docker-server
WORKDIR /srv/docker-serve

COPY package.json ./
RUN npm install --production

ADD . ./
RUN npm run build
