FROM node:22.7.0-alpine AS builder

WORKDIR /app

COPY package*.json ./

RUN npm install --frozen-lockfile

COPY . .

RUN rm .env*

RUN SKIP_FETCH=1 npm run build

# Instalar solo las dependencias de producción
RUN npm prune --omit=dev

# Stage 2
FROM node:22.7.0-alpine

WORKDIR /app

COPY --from=builder /app/node_modules ./node_modules

COPY --from=builder /app/.next ./.next

COPY --from=builder /app/public ./public

COPY --from=builder /app/package.json ./

EXPOSE 3000

CMD ["npm", "run", "start"]