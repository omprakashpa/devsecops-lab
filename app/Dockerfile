# EOL base image (vulnerable on purpose for testing)
FROM ubuntu:16.04

# hardcoded secrets (intentionally vulnerable)
ENV API_KEY=hardcoded-secret-key
ENV DB_PASSWORD=password123

RUN apt-get update && apt-get install -y python3

CMD ["python3", "--version"]
