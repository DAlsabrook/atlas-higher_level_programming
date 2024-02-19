![Python MySQL Dolphin](https://github.com/DAlsabrook/atlas-higher_level_programming/assets/112190470/95509aa9-b8d8-4d62-b5db-5595376546ea)

# Python Object Relational Mapping

## Directory Overview
The `python-object_relational_mapping` directory contains a collection of Python scripts that demonstrate the interaction between a Python application and a MySQL database using both direct connections and an Object Relational Mapper (ORM). This project serves as a practical introduction to database operations in Python, transitioning from traditional SQL execution to the use of SQLAlchemy, an ORM that abstracts SQL expressions into Python code.

Scripts in this directory facilitate a variety of tasks ranging from querying states and cities to modifying database records—all through Python. By abstracting direct SQL queries into Python classes and objects, these scripts highlight the powerful simplicity ORM brings to database interactions.

Here’s what each part of the directory focuses on:

* Direct Database Queries: Scripts like `0-select_states.py` to `5-filter_cities.py` use MySQLdb to connect to the database and execute SQL queries directly from Python scripts.

* Transition to ORM: Starting from `7-model_state_fetch_all.py`, the scripts employ SQLAlchemy for database operations, eliminating the need for handwritten SQL commands.

* ORM Modeling: `model_state.py` and `model_city.py` define Python classes that map to MySQL tables, demonstrating how to create a model of your database structure within Python code.

This directory is designed for developers who wish to understand how to couple Python with a database, implement ORM, and streamline database operations within their Python applications.

## Files Description

- [0-select_states.py](python-object_relational_mapping/0-select_states.py) - Connects to a MySQL database and retrieves all states from the `states` table.
- [1-filter_states.py](python-object_relational_mapping/1-filter_states.py) - Fetches all states with a name starting with the letter 'N'.
- [2-my_filter_states.py](python-object_relational_mapping/2-my_filter_states.py) - Filters states by a user-provided argument.
- [3-my_safe_filter_states.py](python-object_relational_mapping/3-my_safe_filter_states.py) - Implements a SQL injection-safe query to filter states.
- [4-cities_by_state.py](python-object_relational_mapping/4-cities_by_state.py) - Retrieves all cities belonging to a state, sorted in ascending order.
- [5-filter_cities.py](python-object_relational_mapping/5-filter_cities.py) - Filters cities by a user-specified state argument.
- [7-model_state_fetch_all.py](python-object_relational_mapping/7-model_state_fetch_all.py) - Uses SQLAlchemy to list all `State` objects from a database.
- [8-model_state_fetch_first.py](python-object_relational_mapping/8-model_state_fetch_first.py) - Fetches the first `State` object from the database.
- [9-model_state_filter_a.py](python-object_relational_mapping/9-model_state_filter_a.py) - Filters `State` objects that contain the letter 'a'.
- [10-model_state_my_get.py](python-object_relational_mapping/10-model_state_my_get.py) - Retrieves the `State` object with the name passed as argument.
- [11-model_state_insert.py](python-object_relational_mapping/11-model_state_insert.py) - Adds a new `State` object to the database.
- [12-model_state_update_id_2.py](python-object_relational_mapping/12-model_state_update_id_2.py) - Updates the name of the `State` object with `id = 2`.
- [13-model_state_delete_a.py](python-object_relational_mapping/13-model_state_delete_a.py) - Deletes all `State` objects with a name containing the letter 'a'.
- [14-model_city_fetch_by_state.py](python-object_relational_mapping/14-model_city_fetch_by_state.py) - Lists all `City` objects from the database.
- [model_city.py](python-object_relational_mapping/model_city.py) - Defines the `City` class, a Python class that maps to the `cities` table in the database.
- [model_state.py](python-object_relational_mapping/model_state.py) - Defines the `State` class, a Python class that maps to the `states` table in the database.

## Getting Started

1. Ensure that MySQL 8.0 is installed and running on your Ubuntu 20.04 server.
2. Clone this repository to your local machine.
3. Install the required Python packages: `MySQLdb` for direct database connection scripts and `SQLAlchemy` for ORM scripts.
4. Execute the scripts in your terminal. For ORM scripts, ensure you have created the models in your database.

## Author

[David Alsabrook](https://github.com/DAlsabrook)
