# Makefile for car-pooling-challenge
# vim: set ft=make ts=8 noet
# Copyright Cabify.com
# Licence MIT

# Variables
# UNAME		:= $(shell uname -s)

COMPOSE_CMD = docker-compose

.EXPORT_ALL_VARIABLES:

# this is godly
# https://news.ycombinator.com/item?id=11939200
.PHONY: help
help:	### this screen. Keep it first target to be default
ifeq ($(UNAME), Linux)
	@grep -P '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
else
	@# this is not tested, but prepared in advance for you, Mac drivers
	@awk -F ':.*###' '$$0 ~ FS {printf "%15s%s\n", $$1 ":", $$2}' \
		$(MAKEFILE_LIST) | grep -v '@awk' | sort
endif

# Build defaults
app_env = local

# Targets
#
.PHONY: debug
debug:	### Debug Makefile itself
	@echo $(UNAME)

.PHONY: build
build: ### Build the docker image
	$(COMPOSE_CMD) build --build-arg APP_ENV=$(app_env) $(service)

.PHONY: up
up: ### Boot up containers
	$(COMPOSE_CMD) up -d
	sleep 1
	$(COMPOSE_CMD) ps

.PHONY: down
down: ### Stop containers
	$(COMPOSE_CMD) down

.PHONY: clean
clean: ### Stop and delete containers and volumes
	$(COMPOSE_CMD) down -v --remove-orphans

.PHONY: recreate
recreate: clean build up

## Debugging

.PHONY: logs
logs: ### Show all container logs
	$(COMPOSE_CMD) logs -f

.PHONY: bash-console
bash-console: ### Show all container logs
	$(COMPOSE_CMD) run --rm landbot_challenge bash

## Testing and development

.PHONY: test
test: ## Run all or specific tests. Arguments: name=NAME-OF-TEST will run a specific test
	$(COMPOSE_CMD) run --rm landbot_challenge sh /code/scripts/run-tests.sh $(name)

.PHONY: linting
linting: ### Check of fix code linting using black and isort. Arguments: fix=yes will force changes
	$(COMPOSE_CMD) run --rm landbot_challenge sh /code/scripts/run-linting.sh $(fix)
