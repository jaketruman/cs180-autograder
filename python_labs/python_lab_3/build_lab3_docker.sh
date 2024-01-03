IMAGE_NAME="jaketruman/pythonlab3"
IMAGE_TAG="Fall2023"

docker buildx build \
    --platform linux/amd64,linux/arm64 \
    -t ${IMAGE_NAME}:${IMAGE_TAG} \
    --push \
    -f - . <<EOF

FROM jaketruman/byucs180:${IMAGE_TAG}

COPY solution/test_files /autograder/src/test_files/
COPY solution/test*.py /autograder/src/

EOF

docker pull ${IMAGE_NAME}:${IMAGE_TAG}
