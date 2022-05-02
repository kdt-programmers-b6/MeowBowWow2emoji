FROM nvidia/cuda:10.0-cudnn7-devel-ubuntu18.04

RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub
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

EXPOSE 8000

RUN apt-get update
RUN apt-get install -y libglib2.0-0
RUN apt-get install -y libsm6 libxext6 libxrender-dev

RUN pip install --upgrade pip
RUN pip install opencv-python
RUN pip install -r requirements.txt