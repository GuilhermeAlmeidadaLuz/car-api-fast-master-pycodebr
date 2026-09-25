# 🚗 Car API

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python" alt="Python Version" />
  <img src="https://img.shields.io/badge/FastAPI-0.141.1-009688?logo=fastapi" alt="FastAPI" />
  <img src="https://img.shields.io/badge/SQLAlchemy-2.0-red?logo=sqlalchemy" alt="SQLAlchemy" />
  <img src="https://img.shields.io/badge/Pydantic-v2-E92063?logo=pydantic" alt="Pydantic" />
  <img src="https://img.shields.io/badge/Poetry-Package%20Manager-blueviolet?logo=poetry" alt="Poetry" />
</p>

## 📌 About the Project

**Car API** is a modern, asynchronous RESTful API built with **FastAPI** and **Python**. The ecosystem is designed to manage users, automakers, and vehicles with high performance, ensuring strict contracts with **Pydantic v2**, typed relational modeling with **SQLAlchemy 2.0 (async)**, and database versioning with **Alembic**.

---

## 🏗️ Application Architecture

The project follows a layered architecture based on well-defined separation of concerns, decoupling HTTP requests, serialization, and data persistence.

* **App Server (Uvicorn):** Receives HTTP traffic and manages the asynchronous event loop (ASGI).
* **FastAPI (URLs & Routers):** Routes HTTP requests to the appropriate handlers.
* **Schemas (Pydantic):** Validates request payloads and formats public responses.
* **Models & ORM (SQLAlchemy):** Maps application data and interacts with the database.

---

## 🗄️ Data Modeling (ER Diagram)

The database schema manages **Users**, **Brands**, and **Cars**, supporting ownership relationships and automaker associations:

* **`USERS`**: Manages credentials and access metadata for the platform.
* **`BRANDS`**: Stores automaker and car manufacturer records.
* **`CARS`**: Stores technical details and vehicle availability status, linked to a manufacturer (`brand_id`) and an owner (`owner_id`).

```
 ┌───────────────────────────┐         ┌───────────────────────────┐
 │           USERS           │         │          BRANDS           │
 ├───────────────────────────┤         ├───────────────────────────┤
 │ id: int [PK]              │         │ id: int [PK]              │
 │ username: str [UK]        │         │ name: str [UK]            │
 │ email: str [UK]           │         │ description: text         │
 │ password: str             │         │ is_active: bool           │
 │ created_at: datetime      │         │ created_at: datetime      │
 │ updated_at: datetime      │         │ updated_at: datetime      │
 └─────────────┬─────────────┘         └─────────────┬─────────────┘
               │ 1                                   │ 1
               │ possui (owns)                       │ pertence (belongs_to)
               │                                     │
               │ N                                 N │
         ┌─────┴─────────────────────────────────────┴─────┐
         │                      CARS                       │
         ├─────────────────────────────────────────────────┤
         │ id: int [PK]                                    │
         │ model: str                                      │
         │ factory_year: int                               │
         │ model_year: int                                 │
         │ color: str                                      │
         │ plate: str [UK]                                 │
         │ fuel_type: str                                  │
         │ transmission: str                               │
         │ price: decimal                                  │
         │ description: text                               │
         │ is_available: bool                              │
         │ brand_id: int [FK -> brands.id]                 │
         │ owner_id: int [FK -> users.id]                  │
         │ created_at: datetime                            │
         │ updated_at: datetime                            │
         └─────────────────────────────────────────────────┘
```

---

## 📂 Directory Structure

```
car_api/
├── car_api/
│   ├── core/                  # Global configurations and database setup
│   │   ├── database.py        # Async engine configuration and session factory
│   │   └── settings.py        # Environment variables with pydantic-settings
│   ├── models/                # Application ORM models (SQLAlchemy)
│   │   ├── base.py            # Shared declarative base
│   │   └── users.py           # Definition of the 'users' table
│   ├── routers/               # API routes and controllers
│   │   └── users.py           # User endpoints (CRUD)
│   ├── schemas/               # Validation and serialization schemas (Pydantic)
│   │   └── users.py           # Input and output data contracts
│   ├── app.py                 # Main FastAPI application instance
│   └── db.py                  # In-memory mock storage (temporary)
├── migrations/                # Database migrations managed by Alembic
│   ├── versions/              # Database migration versions history
│   └── env.py                 # Migration environment configuration
├── tests/                     # Automated test suite
├── .env.sample                # Sample environment file with SQLite configuration
├── alembic.ini                # Alembic configuration file
├── pyproject.toml             # Project metadata and dependencies (Poetry)
├── poetry.lock                # Locked exact versions of dependencies
└── README.md
```

---

## 🛠️ Environment Management with Pipx and Poetry

We use **pipx** to install and isolate CLI tools and **Poetry** to manage project dependencies, virtual environments, and scripts:

### 1. Environment Setup

#### 🐧 Linux (Ubuntu / Debian)
```bash
# 1. Install pipx and update PATH
sudo apt install pipx
pipx ensurepath

# 2. Install Poetry and shell plugin
pipx install poetry
pipx inject poetry poetry-plugin-shell
```

#### 🪟 Windows (via WSL2)
```bash
# 1. Install WSL with Ubuntu (if not already installed)
wsl --install
wsl --install -d Ubuntu
wsl -l -v
wsl --set-version Ubuntu 2

# 2. Inside the Ubuntu terminal, install tools:
sudo apt install pipx
pipx ensurepath

pipx install poetry
pipx inject poetry poetry-plugin-shell
```

> **Recommended VS Code Extensions:**
> * `WSL` (Microsoft)
> * `Python` (Microsoft)

---

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/GuilhermeAlmeidadaLuz/car_api.git
cd car_api
```

### 2. Install dependencies

Install the virtual environment and all packages managed by Poetry:

```bash
poetry install
```

### 3. Configure environment variables (`.env`)

Copy the `.env.sample` file to create your local `.env` file:

```bash
cp .env.sample .env
```

Open `.env` and set the connection string for asynchronous SQLite using the `aiosqlite` driver:

```ini
# Configurações do Banco de Dados
DATABASE_URL="sqlite+aiosqlite:///<database_name>.db"
```

### 4. Run database migrations with Alembic

Apply existing migrations to create tables in the SQLite database:

```bash
poetry run alembic upgrade head
```

### 5. Start the development server

You can start the server in one of two ways:

**Option A: Inside Poetry's virtual shell**

```bash
poetry shell
fastapi dev car_api/app.py
```

**Option B: Directly via `poetry run`**

```bash
poetry run fastapi dev car_api/app.py
```

---

## 🌐 Endpoints & Interactive Documentation

Once the server is running, the API will be available at:

* **Application:** [http://localhost:8000](http://localhost:8000)
* **Swagger UI (Interactive API documentation and testing):** [http://localhost:8000/docs](http://localhost:8000/docs)

### User Endpoints (`/users`)

| Method | Endpoint | Description | Response Status |
| :--- | :--- | :--- | :--- |
| `POST` | `/` | Creates a new user | `201 Created` |
| `GET` | `/` | Lists all registered users | `200 OK` |
| `PUT` | `/{user_id}` | Updates an existing user | `201 Created` |
| `DELETE` | `/{user_id}` | Removes an existing user | `204 No Content` |

---