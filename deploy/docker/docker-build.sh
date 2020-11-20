#!/bin/bash

# Ensure Docker on system
rm -rf storage-benchmark
git clone https://github.com/txu2k8/storage-benchmark.git
cd storage-benchmark || exit
rm -rf .git
cd ../
tar -zcvf storage-benchmark.tar storage-benchmark


cat > Dockerfile << EOF
FROM ubuntu:20.04
MAINTAINER tao.xu <tao.xu2008@outlook.com>
ADD storage-benchmark.tar /

WORKDIR /storage-benchmark
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install -y unzip php-cli apt-utils mesa-utils git-core apt-file
RUN apt-file update
RUN apt-get install -y python3-pip fio attr
RUN pip3 install -r requirements.txt

#ENTRYPOINT ["python3"]
#CMD ["storage_bm.py", "mnt sanity -d /mnt -h"]
EOF

docker build -t storage-benchmark:`date "+%Y-%m-%d-%H-%M-%S"` .

# docker tag storage-benchmark registry/storage-benchmark:v1
# docker push registry/storage-benchmark:v1
# docker run -it storage-benchmark

# clean up
rm -rf Dockerfile
rm -rf storage-benchmark

