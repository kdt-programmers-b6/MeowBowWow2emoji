FROM node:lts-alpine as builder

RUN mkdir /srv/docker-server
WORKDIR /srv/docker-server

COPY package*.json ./
RUN npm install

COPY . .

RUN npm run build

FROM nginx:stable-alpine

RUN rm -rf /etc/nginx/conf.d/default.conf
COPY --from=builder /srv/docker-server/nginx.conf /etc/nginx/conf.d/default.conf

RUN rm -rf /usr/share/nginx/html/*
COPY --from=builder /srv/docker-server/dist /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]