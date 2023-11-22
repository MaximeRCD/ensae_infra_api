# Contributing to ensae_infra_api

Thank you for your interest in contributing to the `ensae_infra_api` project! We welcome contributions from the community to help improve and maintain this project. Please follow these guidelines to get started:

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
