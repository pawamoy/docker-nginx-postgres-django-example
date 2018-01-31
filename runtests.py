import sys
import os
from os.path import abspath, dirname, join

try:
    from django.conf import settings
    from django.test.utils import get_runner

    if not os.environ.get('DJANGO_SETTINGS_MODULE'):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hello.settings")

    try:
        import django
        sys.path.append(abspath(join(dirname(__file__), 'hello')))
        setup = django.setup
    except AttributeError:
        pass
    else:
        setup()

except ImportError:
    import traceback
    traceback.print_exc()
    raise ImportError('To fix this error, maybe run `pipenv install`')


def run_tests(*test_args):
    """Discover and run tests."""
    if not test_args:
        test_args = ['tests']

    # Run tests
    runner = get_runner(settings)
    test_runner = runner()

    failures = test_runner.run_tests(test_args)

    if failures:
        sys.exit(bool(failures))


if __name__ == '__main__':
    run_tests(*sys.argv[1:])
