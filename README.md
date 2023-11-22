# Contributing to ensae_infra_api

## Clone the Repository

To begin contributing, you'll need to clone the project's repository to your local machine. You can do this by running the following command in your terminal:

```bash
git clone https://github.com/MaximeRCD/ensae_infra_api.git
```

## Create and Activate a Virtual Environment

It's a good practice to create a virtual environment to isolate your project's dependencies. You can use `venv` or `virtualenv` to create one. Navigate to the project directory and run the following commands:

```bash
cd ensae_infra_api
python -m venv venv
```

Activate the virtual environment based on your operating system:

- On Windows:
  ```bash
  venv\Scripts\activate
  ```

- On macOS and Linux:
  ```bash
  source venv/bin/activate
  ```

In your terminal you should see (venv) before command line like so:

  ```bash
  (.venv) PS C:\Users\maxim\ENSAE\Infra\ensae_infra_api>
  ```
### Install requiered packages
Run the following command :
```bash
pip install -r requirements.txt
```
### Install new dependencies
- Make sure you are under your virtual environement
    ```bash
    (.venv) PS C:\Users\maxim\ENSAE\Infra\ensae_infra_api>
    ```
- Install the dependencies or package
    ```bash
    pip install <package_name>
    ```
- If the changes which needed the package installation are pushed then do not forget to push the dependencies to the requirement.txt file
    ```bash
    pip freeze > requirement.txt
    ```

Now you are safe
## Create a New Branch

Before you start working on your contribution, create a new branch based on the `dev` branch. You should name the branch with your contributor name to make it clear who is working on the contribution. Replace `contributorname` with your actual contributor name.

```bash
git checkout -b dev_contributorname dev
```

## Pull the Latest Changes

Make sure your local branch is up-to-date with the latest changes from the `dev` branch by running the following command:

```bash
git pull origin dev
```

## Work on Your Contribution

Now you can make your changes and additions to the project. Remember to write clear and concise code, follow the project's coding style (if specified), and include relevant documentation or comments.

## Commit Your Changes

Once you have made your changes, commit them to your branch with a descriptive commit message:

```bash
git add .
git commit -m "Your commit message here"
```

## Push Your Changes

Push your branch to the remote repository on GitHub:

```bash
git push origin dev_contributorname
```

## Create a Pull Request

Finally, create a pull request (PR) on GitHub to merge your changes into the `dev` branch of the project. Provide a clear title and description for your PR, explaining the purpose and details of your contribution. A project maintainer will review your changes, provide feedback, and possibly merge your PR into the project.


# Initiating a FastAPI Project

FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard Python type hints. This guide will walk you through the steps to initiate a FastAPI project.

## Prerequisites

Before you start, make sure you have the following prerequisites installed:

- Python 3.6 or higher
- pip (Python package manager)

## Install FastAPI and Uvicorn

FastAPI relies on ASGI (Asynchronous Server Gateway Interface) servers like Uvicorn. You need to install both FastAPI and Uvicorn:

```bash
pip install fastapi uvicorn
```

## Create a FastAPI App

You can create a FastAPI app by writing a Python script. Here's a minimal example:

```python
# main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
```

## Run the FastAPI App

To run your FastAPI app, use the Uvicorn server. Replace `main` with your Python script's filename (without the .py extension):

```bash
uvicorn main:app --reload
```

- `main:app` specifies the location of your FastAPI app instance.
- `--reload` enables automatic code reloading during development.

Your FastAPI app should now be running locally at http://localhost:8000. You can access the root route at http://localhost:8000/ in your web browser or API client.

## Explore FastAPI Documentation

FastAPI provides automatic documentation for your API. You can access it at http://localhost:8000/docs or http://localhost:8000/redoc. These interactive documentation pages allow you to explore and test your API endpoints.


Certainly! Here's a Markdown explanation of the choice of project structure for a FastAPI application:

# Project Structure Explanation

When developing a FastAPI application, choosing the right project structure is essential for maintaining code clarity, organization, and scalability. In the previously described structure, we've organized the project into several directories and files for specific purposes. Here's a breakdown of why this structure is beneficial:

## `/models/`

**Purpose**: Data Model Definitions

- **Description**: The `/models/` directory is dedicated to defining Pydantic models. Pydantic models are used for request and response data validation, serialization, and structuring your API's data.

- **Explanation**: By isolating data models in this directory, you separate the concerns of data structure and API logic. This separation enhances code readability and ensures that data is handled consistently across your API.

## `/routers/`

**Purpose**: API Route Definitions

- **Description**: The `/routers/` directory houses the API route definitions. Each Python file represents a group of related routes and defines how incoming HTTP requests are handled.

- **Explanation**: Organizing routes into separate files promotes modularity and maintainability. It makes it easier to manage and extend your API as you can focus on specific areas or resources. Additionally, it simplifies the process of debugging and testing individual routes.

## `/services/`

**Purpose**: Business Logic Separation

- **Description**: The `/services/` directory is dedicated to containing business logic that's separate from route handlers. This is where you implement core functionality, data manipulation, validation, and database interactions.

- **Explanation**: Isolating business logic into services ensures that route handlers remain concise and focused on handling HTTP requests and responses. Services can be reused across different parts of your API and tested independently, making your code more modular and maintainable.

## `database.py`

**Purpose**: Database Configuration

- **Description**: The `database.py` file is responsible for configuring and managing database connections and sessions.

- **Explanation**: Centralizing database-related code in one place simplifies database interactions throughout your application. It also makes it easier to switch between different database technologies or update connection settings when needed.

## `main.py`

**Purpose**: Application Entry Point

- **Description**: The `main.py` file serves as the entry point for your FastAPI application. It's where you create the FastAPI app instance, configure middleware, and define global settings.

- **Explanation**: `main.py` is where you assemble all the components required to run your FastAPI app. It provides a clear entry point for developers to understand how your application is structured and configured. It's also the place where you start the ASGI server to run your FastAPI app.

By following this project structure, you can create a well-organized, maintainable FastAPI application that is easier to develop, test, and scale as your project evolves. It promotes separation of concerns, making it clear where different parts of your application reside and ensuring that each part has a specific responsibility.
