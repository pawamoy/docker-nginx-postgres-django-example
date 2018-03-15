# Example using Docker, Django, multiple Postgres databases, NginX, Gunicorn, pipenv, GitLab CI and tox
This is a [Docker][] setup for a web application based on Django.

- The [Django][] application is served by [Gunicorn][] (WSGI application).
- We use [NginX][] as reverse proxy and static files server. Static and media files are
  permanently stored in volumes.
- Multiple [Postgres][] databases can be used. Data are permanently stored in volumes.
- [Python][] dependencies are managed through [pipenv][], with `Pipfile` and `Pipfile.lock`.
- Support for multiple environment settings (variable `DJANGO_SETTINGS_MODULE` is passed
  to the `djangoapp` service).
- Tests are run using [tox][], [pytest][], and other tools such as [safety][], [bandit][], [isort][] and [prospector][].
- Continuous Integration is configured for [GitLab][] with `.gitlab-ci.yml`.
  CI follows a Build-Test-Release flow. **WARNING**: this part is not fully functional yet.

Also a [Makefile][] is available for convenience. You might need to use `sudo make`
instead of just `make` because `docker` and `docker-compose` commands often needs
admin privilege.

## Requirements
You need to install [Docker][] and [Docker-Compose][].

## Build
`docker-compose build` or `make build`.

## Migrate databases
`docker-compose run --rm djangoapp /bin/bash -c 'cd hello; ./manage.py migrate'` or `make migrate`.

## Run
`docker-compose up` or `make run`.

## Tests
- `make checksafety`
- `make checkstyle`
- `make test`
- `make coverage`

[Docker]: https://www.docker.com/
[Django]: https://www.djangoproject.com/
[Gunicorn]: http://gunicorn.org/
[NginX]: https://www.nginx.com/
[Postgres]: https://www.postgresql.org/
[Python]: https://www.python.org/
[pipenv]: https://docs.pipenv.org/
[tox]: https://tox.readthedocs.io/en/latest/
[pytest]: https://docs.pytest.org/en/latest/
[safety]: https://pyup.io/safety/
[bandit]: https://github.com/openstack/bandit
[isort]: https://github.com/timothycrosley/isort
[prospector]: https://github.com/landscapeio/prospector
[GitLab]: https://about.gitlab.com/
[Makefile]: https://www.gnu.org/software/make/manual/make.html
[Docker-Compose]: https://docs.docker.com/compose/

## Related blog post
[Docker Compose with NginX, Django, Gunicorn and multiple Postgres databases][post]

[post]: http://pawamoy.github.io/2018/02/01/docker-compose-django-postgres-nginx.html
