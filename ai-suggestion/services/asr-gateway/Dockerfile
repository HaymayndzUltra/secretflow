FROM node:20-bullseye
WORKDIR /app
COPY package.json tsconfig.json vitest.config.ts .eslintrc.json ./
RUN npm install
COPY src ./src
RUN npm run build && npm prune --production
CMD ["node", "dist/index.js"]
