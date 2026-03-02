FROM node:12   # EOL + vulnerable base image
WORKDIR /app
COPY . .
RUN npm install
CMD ["node", "app.js"]
