# Backend Documentation

This directory contains the backend implementation of the application using FastAPI.

## Project Structure

- **app/**: Contains the main application code.
  - **__init__.py**: Marks the directory as a Python package.
  - **main.py**: The entry point for the FastAPI application. Initializes the app and sets up the routes.
  - **api/**: Contains the API-related modules.
    - **__init__.py**: Marks the directory as a Python package for API modules.
    - **endpoints.py**: Defines the API endpoints for the FastAPI application.
  - **models/**: Contains the data models used in the application.
    - **__init__.py**: Marks the directory as a Python package for models.
    - **models.py**: Defines the data models.

## Requirements

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Running the Application

To run the FastAPI application, execute the following command:

```
uvicorn app.main:app --reload
```

This will start the server with live reloading enabled.

## API Documentation

Once the server is running, you can access the interactive API documentation at:

```
http://localhost:8000/docs
```

## Additional Information

For more details on FastAPI, refer to the official documentation at [FastAPI Documentation](https://fastapi.tiangolo.com/).