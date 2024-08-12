# Django JWT Project
This project uses best practices and provide boilerplate code to include user authentication using **django-simplejwt**. Tests and OpenAPI (swagger) is included. You may use this as template for your Django-Rest-Framework (DRF) application. Suitable for dev and production!

## Running the app locally

**Note:** If you're building the docker image for the first time, copy requirements-{ENV}.txt from packaging/requirements/ to the project's root.

### Copy requirements file

```sh
cp packaging/requirements/requirements.{ENV}.txt requirements.txt
```

### Copy environment file

```shell script
cp packaging/environment/env.{ENV}.example .env
```
If needed, fill in the values in .env file

### Run project

```shell script
make run
```

### Apply database migrations in a SEPARATE terminal tab

```sh
make apply-migrations
```

### below command is not necessary to run project
To seed the DB, run the following command:

```shell script
make seed-db
```

### View the application at localhost:8000
