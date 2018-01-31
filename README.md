# Example using Docker, Django, multiple Postgres databases, NginX, Gunicorn, pipenv, GitLab CI and tox
This is a Docker setup for a web application based on Django.

- The Django application is served by Gunicorn (WSGI application).
- We use NginX as reverse proxy and static files server. Static and media files are
  permanently stored in volumes.
- Multiple Postgres databases can be used. Data are permanently stored in volumes.
- Python dependencies are managed through pipenv, with `Pipfile` and `Pipfile.lock`.
- Support for multiple environment settings (variable `DJANGO_SETTINGS_MODULE` is passed
  to the `djangoapp` service).
- Tests are run using tox, pytest, and other tools such as safety, bandit, isort and prospector.
- Continuous Integration is configured for GitLab with `.gitlab-ci.yml`.
  CI follows a Build-Test-Release flow. **WARNING**: this part is not fully functional yet.

Also a Makefile is available for convenience. You might need to use `sudo make`
instead of just `make` because `docker` and `docker-compose` commands often needs
admin privilege.

## Requirements
You need to install Docker and Docker-Compose.

## Build
`docker-compose build` or `make build`.

## Migrate databases
`docker-compose run --rm djangoapp /bin/bash -c 'cd hello; ./manage.py migrate'` or `make migrate`.

## Run
`docker-compose up` or `make run`.
