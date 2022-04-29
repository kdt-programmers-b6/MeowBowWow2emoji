FROM nvidia/cuda:10.0-cudnn7-devel-ubuntu18.04

RUN apt-get update && apt-get upgrade -y && apt-get clean
RUN apt-get install -y curl python3.7 python3.7-dev python3.7-distutils
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1
RUN update-alternatives --set python /usr/bin/python3.7

RUN curl -s https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python get-pip.py --force-reinstall && \
    rm get-pip.py

RUN apt-get -y install vim

ENV PYTHONUNBUFFERED 1 

RUN mkdir /srv/docker-server
ADD . /srv/docker-server
WORKDIR /srv/docker-server

RUN pip install --upgrade pip
RUN pip install -r requirements.txt