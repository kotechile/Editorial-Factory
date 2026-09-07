FROM node:20-alpine
WORKDIR /app
RUN apk add --no-cache python3
COPY site/ ./site/
COPY published/ ./published/
COPY context/ ./context/
COPY scripts/ ./scripts/
ENV NODE_ENV=production
ENV PORT=3000
EXPOSE 3000
CMD ["node", "site/server.mjs"]
