FROM node:20-alpine
WORKDIR /app
COPY site/ ./site/
COPY published/ ./published/
ENV NODE_ENV=production
ENV PORT=3000
EXPOSE 3000
CMD ["node", "site/server.mjs"]
