FROM ubuntu:22.04
LABEL maintainer="YuTsung"

WORKDIR /workdir
COPY requirements.txt /workdir/
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Taipei
RUN apt update && \
    apt install -y libeccodes-dev python3-pip && \
    apt install -y python3-tk && \
    pip3 install -r requirements.txt && \
    apt remove -y make gcc build-essential && \
    apt autoremove -y
COPY module /workdir/module
COPY ref /workdir/ref
COPY run_gfe0p01d_demo.py /workdir/
