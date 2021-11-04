# python_boilerplate

**python_boilerplate** is a boilerplate project for Python. Based on template [sourcery-ai/python-best-practices-cookiecutter](https://github.com/sourcery-ai/python-best-practices-cookiecutter).

[Official Docker Image](https://todo.python_boilerplate)

## Features

Here is the highlights of **python_boilerplate**:

1. Testing with [pytest](https://docs.pytest.org/en/latest/)

2. Formatting with [black](https://github.com/psf/black)

3. Import sorting with [isort](https://github.com/timothycrosley/isort)

4. Static typing with [mypy](http://mypy-lang.org/)

5. Linting with [flake8](http://flake8.pycqa.org/en/latest/)

6. Git hooks that run all the above with [pre-commit](https://pre-commit.com/)

7. Deployment ready with [Docker](https://docker.com/)

8. Continuous Integration with [GitHub Actions](https://github.com/features/actions)

9. Universal logging configuration. Log sample is like,

   ```
   2021-11-04 18:12:58 INFO     - [MainThread] [rotatingFileLogger] [__main__.py:9] : len(sys.argv) = 2, sys.argv: ['C:/Users/Johnny/Projects/PyCharmProjects/python_boilerplate/python_boilerplate/__main__.py', '10']
   2021-11-04 18:12:58 INFO     - [MainThread] [rotatingFileLogger] [__main__.py:15] : n = 10, type: <class 'int'>
   2021-11-04 18:12:58 INFO     - [MainThread] [rotatingFileLogger] [__main__.py:16] : fib(n) = 55
   ```

## Usage

1. Clone or download this project.

   ```shell
   $ git clone https://github.com/johnnymillergh/python_boilerplater.git
   ```

2. Build with newest PyCharm.

3. Click the green triangle to Run.

## Setup

1. Install dependencies

   ```shell
   $ pipenv install --dev
   ```

2. Setup pre-commit and pre-push hooks

   ```shell
   $ pipenv run pre-commit install -t pre-commit
   $ pipenv run pre-commit install -t pre-push
   ```

## Useful Commands

### Run unit test

```shell
$ pipenv run pytest --cov --cov-fail-under=50
```

### Conventional Changelog CLI

1. Install global dependencies (optional if installed):

   ```sh
   $ npm install -g conventional-changelog-cli
   ```

2. This will *not* overwrite any previous changelogs. The above generates a changelog based on commits since the last semver tag that matches the pattern of "Feature", "Fix", "Performance Improvement" or "Breaking Changes".

   ```sh
   $ conventional-changelog -p angular -i CHANGELOG.md -s
   ```

3. If this is your first time using this tool and you want to generate all previous changelogs, you could do:

   ```sh
   $ conventional-changelog -p angular -i CHANGELOG.md -s -r 0
   ```

## CI (Continuous Integration)

- GitHub Actions is for building project and running tests.
- ~~[Travis CI](https://travis-ci.com/github/johnnymillergh/media-streaming) is for publishing Docker Hub images of SNAPSHOT and RELEASE.~~

## Maintainers

[@johnnymillergh](https://github.com/johnnymillergh).

## Contributing

Feel free to dive in! [Open an issue](https://github.com/johnnymillergh/python_boilerplate/issues/new).

### Contributors

This project exists thanks to all the people who contribute. 

- Johnny Miller [[@johnnymillergh](https://github.com/johnnymillergh)]
- …


### Sponsors

Support this project by becoming a sponsor. Your logo will show up here with a link to your website. [[Become a sponsor](https://become-a-sponsor.org)]

## Credits

This package was created with Cookiecutter and the [sourcery-ai/python-best-practices-cookiecutter](https://github.com/sourcery-ai/python-best-practices-cookiecutter) project template.

Inspired by [How to set up a perfect Python project](https://sourcery.ai/blog/python-best-practices/).

## License

[Apache License](https://github.com/johnnymillergh/python_boilerplate/blob/master/LICENSE) © Johnny Miller

2021 - Present
