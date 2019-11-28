FROM 119.3.170.97:5000/ubuntu:latest
MAINTAINER pighui pighui233@163.com
WORKDIR /usr/src
ADD . /usr/src/MyhealthTornado
VOLUME /usr/src/MyhealthTornado
WORKDIR /usr/src/MyhealthTornado
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
RUN pip install gunicorn -i https://mirrors.aliyun.com/pypi/simple
RUN chmod +x run.sh
CMD /usr/src/MyhealthTornado/run.sh