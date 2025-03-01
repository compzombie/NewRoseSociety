# Stage 1: Build React frontend
FROM node:16 AS frontend-build

WORKDIR /app/frontend

# Copy package files and install dependencies
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install

# Copy frontend source and build
COPY frontend ./
RUN npm run build

# Stage 2: Set up Python backend and serve application
FROM python:3.9

WORKDIR /app

# Install Python dependencies
COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend ./backend/

# Copy built frontend from previous stage
COPY --from=frontend-build /app/frontend/build ./frontend/build

# Set environment variable for production
ENV ENVIRONMENT=production
ENV PORT=8080

# Expose the port the app will run on
EXPOSE 8080

# Start the application
CMD ["python", "backend/main.py"]