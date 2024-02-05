# Python SDK for Rumo

## What is Rumo ?

[Rumo](https://www.rumo.co) is a flexible SaaS recommendation system adaptable to all entertainment industries (films, music, podcasts, video games, sports, etc.) and based on both content metadata and user behaviors. Rumo's algorithms are transparent and explainable, providing full control over the recommendation process.

To start working with Rumo, you will generally need to start by [creating an account](https://dashboard.rumo.co/auth/register) on the Rumo dashboard,
in order to generate an environment and the associated credentials.


## What is this reposotiry ?

This is the first release of the Python SDK for Rumo.

By installing this library (see below how) and running a few simples of Python code, you will be able to
perform most of the basic operations on Rumo's APIs (=> see official Rumo API documentation [here](https://apidoc.rumo.co/)),
and in particular:
    * uploading your catalog to Rumo (and viewing, updating and deleting content items)
    * using the recommendation and search features
    * creating user interactions
    * generating personalized recommendations

Importantly, all of the API requests will automatically be validated against the Rumo documentation
using the standard OpenAPI format,
ensuring that all content items and API calls are well formatted.

Additional options are also available for validating the API responses, and for additional "debug" logging of the API calls.

## Working with this repository

### From github

To install directly from the remote github repository:

`pip install git+ssh://git@github.com/Spideo/rumo-sdk-python.git`

This can also be adapted in your `pyproject.toml` or `requirements.txt` file.

### Locally

To install instead from your local directory, use:

`pip install -e {PATH_TO_LOCAL_DIR}`.

This corresponds to an [editable install](https://pip.pypa.io/en/stable/topics/local-project-installs/#editable-installs),
useful when you are both using and developing the library at the same time.


## Getting started

Most of the common examples of using the Rumo API are presented in the `post_content.ipynb` (for catalog upload)
and `tutorial.ipynb` (for all other use cases) Python notebook, which should get you started making simple calls to the APIs.

You will of course need to adapt these examples to your own Rumo environment (source + API key), catalog data and recommendation use cases.

---------------------------------------

## Contact us

For any question directly related to this SDK, do not hesitate to create issues and Pull Requests.

For any general question about Rumo, please feel free to write to contact@rumo.co.
