FROM ubuntu:18.04

USER root
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    vim \
    openssl

WORKDIR /app
COPY . .

CMD ["bash"]
