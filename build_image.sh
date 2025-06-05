#!/bin/bash

sudo docker build \
--no-cache \
-t registry.mfc.cwb/warehouse_sggm:23.11.1 \
--build-arg http_proxy=http://172.16.7.55:8888 \
--build-arg https_proxy=http://172.16.7.55:8888 \
.
