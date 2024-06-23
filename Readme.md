# Book Review App

This is a full-stack book review application built using Angular and Django.

## Features

1. **List Books**: View a list of all available books.
2. **Search Books**: Search for books by name, genre, or author.
3. **Submit Review**: Submit a review for a selected book.
4. **View Reviews**: View all reviews submitted for any book.
5. **Validation**: The review submission page includes validation to ensure data integrity.

## Getting Started

### Prerequisites

- Docker and Docker Compose
- Node.js (v20.x.x) and npm (v10.x.x)
- Angular CLI (if not installed globally)

### Backend Setup

1. **Navigate to the backend directory**:
    ```sh
    cd book_review
    ```

2. **Make the entrypoint file executable**:
    ```sh
    chmod +x entrypoint.sh
    ```

3. **Build and start the backend server using Docker Compose**:
    ```sh
    docker-compose up --build
    ```

    The server will start on `localhost:8005`.

### Frontend Setup

1. **Navigate to the frontend directory**:
    ```sh
    cd book-review-app
    ```

2. **Install Angular CLI globally (if not already installed)**:
    ```sh
    npm install -g @angular/cli
    ```

3. **Install the necessary dependencies**:
    ```sh
    npm install
    ```

4. **Start the frontend server**:
    ```sh
    ng serve
    ```

    The frontend will start on `localhost:4200` and you will see the list of books on the homepage.

## Project Structure

```
book_review/           # Django backend project
    ├── app/           # Main application code
    ├── Dockerfile     # Docker configuration for the backend
    ├── entrypoint.sh  # Entrypoint script for Docker
    └── docker-compose.yml # Docker Compose configuration

book-review-app/       # Angular frontend project
    ├── src/           # Main application code
    ├── angular.json   # Angular configuration file
    └── package.json   # NPM dependencies and scripts
```
