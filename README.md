Dev: [![Build Status](https://travis-ci.com/marclanepitt/tutory_api.svg?token=QxTgpKzhU3nxqVJMzhCC&branch=dev)](https://travis-ci.com/marclanepitt/tutory_api)

Master: [![Build Status](https://travis-ci.com/marclanepitt/tutory_api.svg?token=QxTgpKzhU3nxqVJMzhCC&branch=master)](https://travis-ci.com/marclanepitt/tutory_api)

## General
* All apps should go in the `apps/` folder.
* The `common` app is used to for general management commands, any other general things.
* The inner `tutory_api/` folder holds:
    * `settings/`: Module for all settings (`settings.py` imports the necessary testing, local settings files)
        * During local development settings in `settings.py` are overridden by the values in `local_settings.py`. This file is a symlink to `local_settings.py.dev` and is .gitignored. See Dev setup instructions below.
        * `testing_settings.py` are used during testing.
    * `urls.py`: The root url conf. Add new urls for `v1` of the api to `v1_urls`.
* `.coveragerc`: Config file for coverage package. This package reports how much of your code is actually being tested by the tests you write.
* `.flake8`: Config file for flake8, which checks python code quality and lints it. (Tells you about unneeded code, etc.)
`.pre-commit-config.yaml`: Config file for pre-commit, which runs everytime you commit code. This runs flake8 and some other useful tools.
* `.travis.yml`: Config file for travis-ci which runs your test suite when a pull request on GitHub is opened.
* `run_tests.sh`: Helper script that runs the test suite with coverage enabled.

## App Structure
* `factories/`: Where testing factories are stored. Remember to import the factory in `__init__.py`, so you can do `from users.factories import UserFactory`. See all files in `users/factories/` for reference.
    * Factories make it easy to create objects during testing.
* `v1/`: Stores all serializers, views, urls, etc for v1 of this app's api.
    * Api versioning is a best practice. In the future you would create `v2/`, etc. directories. When doing this you will likely `cp v1/ v2/` and modify as needed.
    * The `tests/` folder holds serializer, view, etc. tests
        * Name the test files `test_<module>` where `<module>` is the file you are testing.
* The rest are the normal `models.py`, `admin.py`, and anything not specific to a certain api version.

## Dev setup
* `virtualenv venv -p python3`
* `source venv/bin/activate` or the equivalent on windows
* `pip install -r requirements.txt`
* `cd tutory_api/settings` , `cp local_settings.py.dev local_settings.py`
* `pre-commit install`
* `python manage.py migrate`
* `python manage.py run_seeds`
* `python manage.py runserver`
