ENV = dev
WEB_CONTAINER_NAME = library-web
EXEC_PREFIX = docker exec -it $(WEB_CONTAINER_NAME)
MANAGEMENT_PREFIX = $(EXEC_PREFIX) bash -c "python manage.py

DOCKER_COMPOSE = docker-compose -f docker-compose-$(ENV).yml
BUILD = $(DOCKER_COMPOSE) build
DOWN_ALL = $(DOCKER_COMPOSE) down -v

MAKE_MIGRATIONS = $(MANAGEMENT_PREFIX) makemigrations"
APPLY_MIGRATIONS = $(MANAGEMENT_PREFIX) migrate"
VALIDATE_TESTS = $(MANAGEMENT_PREFIX) test"
SEED_DB = $(EXEC_PREFIX) python -m _db_seed


build:
	# Build containers
	$(BUILD)
run:
	# Run containers
	$(DOCKER_COMPOSE) up
run-d:
	# Run containers detached
	$(DOCKER_COMPOSE) up -d
stop:
	# Stop all currently running containers for current project
	$(DOCKER_COMPOSE) stop
down-all:
	# Stop containers and removes containers, networks, volumes, and images
	# created by `up`.
	$(DOWN_ALL)
clean-build: down-all
	# Do a `down-all` first and re-build containers.
	$(MAKE) build
clean-run: clean-build
	# Do a `clean-build` first and run containers.
	$(MAKE) run

migrations:
	# Make database migrations.
	$(MAKE_MIGRATIONS)
apply-migrations:
	# Apply database migrations.
	$(APPLY_MIGRATIONS)

test:
	# check all test cases
	$(VALIDATE_TESTS)

full-run:
	# Used to run everything needed to bring the project up.
	# (Includes database seeding.)
	$(MAKE) down-all
	$(MAKE) run-d
	# We sleep some time to wait for db to be ready so no error occurs if we're
	# running this after just creating db container.
	sleep 5
	$(MAKE) apply-migrations
	$(MAKE) seed-db
