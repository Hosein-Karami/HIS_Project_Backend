FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf
COPY default.conf /etc/nginx/conf.d/

COPY staticfiles /var/www/html/staticfiles
COPY dist/ /var/www/html/app