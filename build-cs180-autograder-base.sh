# Build the CS 235 Lab Autograder Base
# Autograder base expects subsequent layers to add a file named run_tests.py 
#   that will generate /autograder/results/results.json

IMAGE_NAME="jaketruman/byucs180"
IMAGE_TAG="Fall2023"

docker buildx build \
    --platform linux/amd64,linux/arm64 \
    -t ${IMAGE_NAME}:${IMAGE_TAG} \
    --push \
    -f - . <<EOF

FROM gradescope/autograder-base:ubuntu-22.04

RUN apt-get update \
  && apt-get install -y \
      python-is-python3 \
      python-dev-is-python3

RUN apt-get install -y \
      less \
      vim

RUN apt-get clean

RUN mkdir -p /autograder/results/

RUN pip3 install byu_pytest_utils==0.7.2

COPY --chmod=755 <<INNEREOF /autograder/run_autograder
#!/bin/bash

cd /autograder
mkdir -p arena && touch arena/empty && rm -rf arena/*
cp -r submission/* arena/
cp -r src/* arena/
cd arena
python3 -m pytest -vv .
cp results.json /autograder/results/

INNEREOF

EOF

docker pull ${IMAGE_NAME}:${IMAGE_TAG}
