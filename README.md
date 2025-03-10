# Python FastAPI Boilerplate

This repository provides a general-purpose boilerplate for Python development, built with FastAPI, incorporating queue/job processing, database seeding, and Alembic migrations.

## Features

- **FastAPI:** Robust and high-performance web framework for building APIs.
- **Alembic:** Database migration tool for managing schema changes.
- **Queue/Jobs:** Asynchronous task processing for background operations. (Example: Celery, or RQ)
- **Seeders:** Tools for populating the database with initial data.
- **Environment Management:** Using `.env` files and `python-dotenv` for configuration.
- **Structured Project Layout:** Organized `src` directory with clear separation of concerns.
- **Testing:** Basic structure for unit and integration testing.
- **Dependency Management:** Using `requirements.txt` for easy dependency installation.

## Project Structure

```
my_python_boilerplate/
├── src/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py # FastAPI application entry point
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   └── ...
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   └── ...
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   └── ...
│   │   ├── jobs/ # Queue/job processing
│   │   │   ├── __init__.py
│   │   │   └── tasks.py # Example tasks
│   │   ├── seeders/
│   │   │   ├── __init__.py
│   │   │   └── seed.py # Database seeding scripts
│   │   ├── config.py # Configuration settings
│   │   └── database.py # Database connection and setup
│   ├── alembic/ # Alembic migrations
│   │   ├── env.py
│   │   ├── README
│   │   ├── script.py.mako
│   │   └── versions/
│   └── __init__.py
├── tests/ # Testing directory
│   ├── __init__.py
│   └── ...
├── .env # Environment variables
├── requirements.txt # Project dependencies
├── alembic.ini # Alembic configuration
├── README.md # This file
```

## Getting Started

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd my_python_boilerplate
    ```

2.  **Create a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure `.env`:**

    - Create a `.env` file in the project root.
    - Set the necessary environment variables (e.g., database connection details, API keys).

5.  **Run Alembic migrations:**

    ```bash
    alembic upgrade head
    ```

6.  **Run seeders (optional):**

    ```bash
    python src/app/seeders/seed.py
    ```

7.  **Start the FastAPI application:**

    ```bash
    uvicorn src.app.main:app --reload
    ```

8.  **Run the job worker (if using a queue system like Celery):**
    ```bash
    celery -A src.app.jobs.tasks worker --loglevel=info
    ```

## Configuration

- Use the `.env` file to manage environment variables.
- Configuration settings are loaded from `.env` and accessible through `src/app/config.py`.

## Database Migrations (Alembic)

- Use Alembic to manage database schema changes.
- Run `alembic revision --autogenerate -m "Migration description"` to create a new migration.
- Run `alembic upgrade head` to apply migrations.

## Queue/Jobs

- (Example using Celery)
- Define tasks in `src/app/jobs/tasks.py`.
- Start a worker to process tasks.

## Seeders

- Create seeders in `src/app/seeders/seed.py` to populate the database.
- Run the seeders using `python src/app/seeders/seed.py`.

## Testing

- Write unit and integration tests in the `tests` directory.
- Use `pytest` to run tests.

## Dependencies

- Dependencies are managed using `requirements.txt`.
- Use `pip freeze > requirements.txt` or `pipreqs ./` to update the dependencies.
- Poetry or Pipenv are recommended for more robust dependency management.

## Contributing

Feel free to contribute to this boilerplate by submitting pull requests.

## License

This project is licensed under the **MIT License**.

Copyright (c) \[2025] \[Christopher Gamella/ACES]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
