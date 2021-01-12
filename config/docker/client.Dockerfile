FROM mhart/alpine-node:11

WORKDIR /app

COPY frontend/package.json ./

RUN yarn

COPY config/webpack ./config/webpack/

COPY frontend/src ./src/

CMD yarn webpack