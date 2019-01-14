FROM fedora
MAINTAINER Sofyan Saputra "sofyan@biznetgio.com"


RUN dnf update -y && \
    mkdir /BLESS
COPY . /BLESS
WORKDIR /BLESS
RUN dnf install -y gcc bash git openssl openssl-devel
RUN dnf install -y python3 python3-devel
RUN pip3 install --upgrade pip
RUN pip3 install -e .
EXPOSE 6969