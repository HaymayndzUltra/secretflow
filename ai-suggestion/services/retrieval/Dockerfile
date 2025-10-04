FROM node:20-bullseye

ARG SERVICE_PATH=services/retrieval

WORKDIR /app

COPY ${SERVICE_PATH}/package.json ./package.json
COPY ${SERVICE_PATH}/tsconfig.json ./tsconfig.json
COPY ${SERVICE_PATH}/vitest.config.ts ./vitest.config.ts
COPY ${SERVICE_PATH}/.eslintrc.json ./.eslintrc.json
COPY tsconfig.base.json /tsconfig.base.json

RUN npm install

COPY ${SERVICE_PATH}/src ./src

RUN npm run build && npm prune --production

CMD ["node", "dist/index.js"]
