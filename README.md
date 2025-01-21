# BuilderCatalogue

This repository contains the code for the Builder Catalogue project.
The project is a web application that contains user, sets, and pieces information, 
as well as what pieces the user has and which sets the user can build with the pieces the user has.
The application is built using Python and the FastAPI framework, and it uses an SQLite database to store the data.

## Running the Application

To run the application, use the `./run_app.sh` script from the root of the project. 
The application can be accessed at `http://localhost:8000/docs` after running the script.

### Endpoints

The application has the following endpoints:
- `/users`: To get all users
- `/users/by-name/{name}`: To get user summary by users name
- `/users/by-id/{user_id}`: To get detailed information about user and pieces user has by user ID
- `/sets`: To get all sets
- `/sets/by-name/{set_name}`: To get set summary by set name
- `/sets/by-id/{set_id}`: To get full data for a set by the set ID including pieces set contains
- `/colors`: To get all colors
- `/user/{name}/buildable-sets`: To get sets that the user can build with their inventory

### Swagger UI

![Screenshot 2025-01-20 at 13 23 28](https://github.com/user-attachments/assets/0e4a40b4-0147-4d7b-9928-65d07d819033)

## Database

The project uses SQLAlchemy for ORM and SQLite as the database. 
The database URL is configured in the app/database.py file.

### ER Diagram

![Screenshot 2025-01-21 at 12 38 34](https://github.com/user-attachments/assets/9629e590-ae01-4ed3-9e42-5f25449f1482)

## Dependencies

The project dependencies are listed in the requirements.txt file 
and can be installed using `pip install -r requirements.txt` command.

```
fastapi
uvicorn
pydantic
sqlalchemy
databases
pytest
```

## Project Structure

- `app/main.py`: The entry point of the FastAPI application.
- `app/models.py`: Contains the SQLAlchemy models for the database.
- `app/api/api.py`: Contains the API endpoints.
- `app/database.py`: Configures the database connection and session.
- `run_app.sh`: Script to run the FastAPI application.
- `requirements.txt`: Lists the project dependencies.
- `tests/`: Contains the unit tests for the api.
