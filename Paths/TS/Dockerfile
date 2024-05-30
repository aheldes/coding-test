FROM node:22-alpine

ENV http_proxy http://10.255.46.226:3128
ENV https_proxy http://10.255.46.226:3128

WORKDIR /app

COPY . .

RUN npm install -g typescript
RUN npm install -D @types/node

RUN tsc main.ts

CMD ["node", "main.js"]
