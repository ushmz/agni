FROM mysql:5.7

RUN apt-get update
RUN apt-get -y install locales-all
# RUN apt-get -y install curl
# RUN curl -fsSL -o /usr/local/bin/dbmate https://github.com/amacneil/dbmate/releases/latest/download/dbmate-linux-amd64
# RUN chmod +x /usr/local/bin/dbmate

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8

COPY mysql/conf.d/* /etc/mysql/conf.d/
