# Build stage
FROM node:20-alpine as builder

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install ALL dependencies (including devDependencies needed for build)
RUN npm ci && npm cache clean --force

# Copy source code
COPY . .

# Build Angular app for production
RUN npm run build -- --configuration production

# Runtime stage with nginx
FROM nginx:alpine

# Install gettext for envsubst
RUN apk add --no-cache gettext

# Copy built app from builder - Angular 17 outputs to dist/portfolio-frontend
COPY --from=builder /app/dist/portfolio-frontend /usr/share/nginx/html

# Copy nginx config template
COPY nginx.conf /etc/nginx/templates/default.conf.template

# Cloud Run provides PORT environment variable
ENV PORT=8080

EXPOSE 8080

# Start nginx - it will automatically process templates with envsubst
CMD ["sh", "-c", "envsubst '$$PORT' < /etc/nginx/templates/default.conf.template > /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'"]
