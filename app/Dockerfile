FROM ubuntu:16.04   # EOL base image ❌

ENV API_KEY="hardcoded-secret-key"   # secret exposure ❌
ENV DB_PASSWORD="password123"        # secret exposure ❌

RUN apt-get update && apt-get install -y \
    curl \
    wget \
    netcat \
    telnet \
    ftp \
    vim \
    nano \
    openssh-server \
    sudo \
    python \
    python-pip \
    build-essential \
    ca-certificates

WORKDIR /app
COPY . .

RUN chmod -R 777 /app   # over-permissive permissions ❌

EXPOSE 22 21 80 443     # unnecessary exposed ports ❌

USER root               # running as root ❌

CMD ["/bin/bash"]
