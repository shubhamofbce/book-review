# Book Review App

This is a full-stack book review application built using Angular and Django.

### Watch the demo video
[![Watch the video](https://img.youtube.com/vi/3a9y276gNqM/0.jpg)](https://youtu.be/3a9y276gNqM)


## Features

1. **List Books**: View a list of all available books.
2. **Search Books**: Search for books by name, genre, or author.
3. **Submit Review**: Submit a review for a selected book.
4. **View Reviews**: View all reviews submitted for any book.
5. **Validation**: The review submission page includes validation to ensure data integrity.
6. **Pagination**: You can use next and prev to change page on the list page
7. **Sort**: You can sort the book list by title, author and average rating

## Getting Started

### Prerequisites

- Python 3.11
- Node.js (v20.x.x) and npm (v10.x.x)
- Angular CLI (if not installed globally)

## Backend Setup
The backend is already deployed on [Book Review Production](https://book-review-production.up.railway.app).
So you don't need to run the backend to test the app. Frontend is already using the deployed api.
You can also find all the APIs here at: [Postman Documentation](https://documenter.getpostman.com/view/9972670/2sA3XWdekH#d496b20a-ef50-4acb-be81-18aedc9fe024).


Follow these steps to set up the backend locally.

### Prerequisites

- Python 3.11

### Setup Instructions

1. **Install Python 3.11**:
    Download and install Python 3.11 from the [official website](https://www.python.org/downloads/).

2. **Create a Virtual Environment**:
    ```sh
    python3.11 -m venv bookenv
    ```

3. **Activate the Virtual Environment**:
    - On Windows:
        ```sh
        bookenv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source bookenv/bin/activate
        ```

4. **Install Requirements**:
    ```sh
    pip install -r requirements.txt
    ```

5. **Apply Migrations**:
    ```sh
    ./manage.py migrate app
    ```

6. **Run the Server**:
    ```sh
    ./manage.py runserver 0.0.0.0:8005
    ```

    The backend server will start on `localhost:8005`.

## Frontend Setup

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

book-review-app/       # Angular frontend project
    ├── src/           # Main application code
    ├── angular.json   # Angular configuration file
    └── package.json   # NPM dependencies and scripts
```
