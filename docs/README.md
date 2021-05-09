Preform
=======

* FastAPI
> FastAPI is a high-performance API based on Pydantic and Starlette.
```

```

* SQLAlchemy
```
SQLAlchemy supports PostgreSQL, MySQL, SQLite, Oracle, Microsoft SQL Server

declarative_base()  -- is a factory function that constructs a base class for declarative class definitions

Base.metadata.create_all()

```

* Modular App Structure
```
├── app
│   ├── __init__.py
│   ├── database.py
│   ├── main.py
│   ├── models.py       # SQLAlchemy models
│   └── schemas.py      # Pydantic models
├── load.py

```

* Pydantic
```
Remember that FastAPI is built upon Pydantic.
The primary means of defining objects in Pydantic is via models that inherit from BaseModel
```
