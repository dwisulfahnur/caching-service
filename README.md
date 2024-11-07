# Caching Service

This project is a simple caching service built with [FastAPI](https://fastapi.tiangolo.com/). 
The service allows creating and reading a payload with caching implemented to avoid redundant computations.
The caching data is stored in a PostgreSQL database, but for testing purposes, it can use a temporary SQLite database.

## Features

- **POST /payload**: Creates a new payload or retrieves a cached identifier if it already exists.
- **GET /payload/{id}**: Retrieves a cached payload based on its identifier.

## Setup Database Credentials

copy .env.example to .env

```bash
cp .env.example .env
```

then adjust the db credentials in the .env file


## Run with Docker

Run this project with docker using the following command:

```bash
docker compose up -d
```

## Run on the local environment

1. **Clone the Repository**:

```bash
git clone https://github.com/dwisulfahnur/caching-service.git
cd caching-service
```

2. **Install Dependencies: Use pip to install project dependencies.**

create python virtual environment and activate it, then install the requirements.

```bash
python3.12 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

3. **Run the Application: Start the FastAPI server.**

```bash
python run.py
```

The server should now be running at http://127.0.0.1:8000.
