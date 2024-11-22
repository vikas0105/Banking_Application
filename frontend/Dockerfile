# Stage 1: Build the React app
FROM node:16 AS build

WORKDIR /app

# Copy package.json to the working directory
COPY package.json ./

# Install dependencies (npm install will resolve dependencies from package.json)
RUN npm install

# Copy the rest of the app source code
COPY . .

# Build the React app for production
RUN npm run build

# Stage 2: Serve with Nginx
FROM nginx:alpine

# Copy the build output to the Nginx HTML folder
COPY --from=build /app/build /usr/share/nginx/html

# Expose port 80 to access the app
EXPOSE 80

# Start Nginx to serve the app
CMD ["nginx", "-g", "daemon off;"]

