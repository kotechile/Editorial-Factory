FROM node:20-alpine
WORKDIR /app
RUN apk add --no-cache python3 bash curl
COPY site/ ./site/
COPY published/ ./published/
COPY context/ ./context/
COPY scripts/ ./scripts/
COPY skills/ ./skills/
COPY .agents/ ./.agents/
ENV NODE_ENV=production
ENV PORT=3000
EXPOSE 3000
CMD ["node", "site/server.mjs"]
