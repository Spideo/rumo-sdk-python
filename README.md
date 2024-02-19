# Python SDK for Rumo

![Build](https://github.com/spideo/rumo-sdk-python/actions/workflows/build.yml/badge.svg?branch=main)

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)




## What is Rumo ?

[Rumo](https://www.rumo.co) is a flexible SaaS recommendation system adaptable to all entertainment industries (films, music, podcasts, video games, sports, etc.) and based on both content metadata and user behaviors. Rumo's algorithms are transparent and explainable, providing full control over the recommendation process.

To start working with Rumo, you will generally need to start by [creating an account](https://dashboard.rumo.co/auth/register) on the Rumo dashboard,
in order to generate an environment and the associated credentials.

More detailed information is available in the [official Rumo API documentation](https://apidoc.rumo.co/).


## What is this repository ?

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

Most of the common examples of using the Rumo API are presented in the [`post_content.ipynb`](post_content.ipynb) (for catalog upload)
and [`tutorial.ipynb`](tutorial.ipynb) (for all other use cases) Python notebook, which should get you started making simple calls to the APIs.

You will of course need to adapt these examples to your own Rumo environment (source + API key), catalog data and recommendation use cases.

---------------------------------------

## Contributions

We are excited to receive contributions from the community! Before contributing, please read these guidelines to ensure a smooth process.

### Reporting Issues

If you find a bug or have an idea to improve the SDK, please [open an issue on our GitHub issues page](https://github.com/Spideo/rumo-sdk-python/issues). Make sure to include as many details as possible, including steps to reproduce the issue.

### Submitting a Feature Request

If you have an idea for a new feature or improvement, we'd love to hear about it! [Open a pull request on GitHub](https://github.com/Spideo/rumo-sdk-python/pulls) and clearly explain what you would like to see added and why it would be beneficial.

### Proposing Changes

If you want to contribute by proposing changes to the source code, please follow these steps:

1. **Fork the Repository:** Start by [forking the GitHub repository](https://github.com/Spideo/rumo-sdk-python/fork) to your own account.

2. **Clone the Forked Repository:** Clone your fork locally on your machine.

   ```bash
   git clone https://github.com/YourUsername/rumo-sdk-python.git


3. **Create a Branch:** Create a new branch for your feature or bug fix.

   ```bash
   git checkout -b my-new-feature

4. **Make Your Changes:** Make the necessary modifications and ensure to document your code properly.

5. **Test Your Changes:** Ensure that existing tests pass and add tests if necessary.

6. **Commit and Push:** Commit your changes and push them to your fork.

   ```bash
   git commit -m "Adding the new feature"
   git push origin my-new-feature

7. **Submit a Pull Request:** Open a pull request on the main repository and explain your changes.

After you've submitted your pull request, we will review it and merge it if approved.
Thank you for contributing to improving the SDK Rumo Python!

## Contact us

For any general question about Rumo, please feel free to write to contact@rumo.co.