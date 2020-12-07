FROM nginx:latest

WORKDIR /etc/nginx/conf.d
COPY default.conf default.conf

WORKDIR /usr/share/nginx/html
COPY $PWD/index.html .

RUN mkdir js
COPY $PWD/search.js ./js

EXPOSE 80
