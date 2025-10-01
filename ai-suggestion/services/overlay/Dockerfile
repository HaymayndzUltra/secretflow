FROM node:20-bullseye
WORKDIR /app
COPY package.json tsconfig.json tsconfig.main.json vite.config.ts vitest.config.ts .eslintrc.json ./
RUN npm install
COPY src ./src
RUN npm run build && npm prune --production
CMD ["npm", "run", "start"]
