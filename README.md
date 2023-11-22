# Spideo Python Template

This is the generic template for Spideo libraries.

Feel free to use it when setting up a new repository for an internal lib.

## Working with this repository

### Dependency management

This repository uses [Poetry](https://python-poetry.org/) to manage package dependencies,
read the [Poetry docs](https://python-poetry.org/docs/basic-usage/) to understand how it works.

Most of the basic commands that you will need should already be available via the `Makefile`, e.g. `make install`.

### Linting

All code in this repository must respect
* Python [PEP8](https://peps.python.org/pep-0008/) standard, automatically checked by [flake8](https://flake8.pycqa.org/),
* The _"opinionated"_ [Black](https://github.com/psf/black) code style,
* Imports sorted according to [isort](https://github.com/PyCQA/isort) rules.

The reasoning is to make sure code style is harmonized across all our code-base,
and also to ensure minimal and readable `git diff` results.

All PRs will be checked against these standards, and must pass the checks in order to be merged.

If you don't want to spend time thinking about code linting, simply install the
[Black integration](https://black.readthedocs.io/en/stable/integrations/editors.html)
and [isort integration](https://github.com/pycqa/isort/wiki/isort-Plugins)
for your favorite editor.
Extensions or plugins are available for most popular editors, and can usually be configured
to _run on save_.

### Testing

Unit tests are run with `pytest`, with all tests in the `tests` module.
See [official docs](https://docs.pytest.org/) for help on organizing and naming tests.

The `tests` folder contains a few examples, including how to check for raised exceptions,
and parametrizing tests. This should be further enriched in the future, in particular
for the usage of fixtures, mocks and temporary files.

### Documenting

Docstrings are not mandatory, but should be detailed for key functions and libraries that
are intended to be used outside of the library when importing it.

We should follow the [numpy style guide](https://numpydoc.readthedocs.io/en/latest/format.html) for library docstrings.

## Importing the repository

### From github

To install directly from the remote github repository:

`pip install git+ssh://git@github.com/Spideo/spideo-python-template.git`

This can also be adapted in a `pyproject.toml` or `requirements.txt` file.

### Locally

To install instead from your local directory, use:

`pip install -e {PATH_TO_LOCAL_DIR}`.

This corresponds to an [editable install](https://pip.pypa.io/en/stable/topics/local-project-installs/#editable-installs),
useful when you are both using and developing the library at the same time.