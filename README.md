# Python SDK for Rumo

This is the first attempt at a public SDK for Rumo.

See official Rumo API documentation [here](https://apidoc.rumo.co/)

## Importing the repository

### From github

To install directly from the remote github repository:

`pip install git+ssh://git@github.com/Spideo/rumo-sdk-python.git`

This can also be adapted in your `pyproject.toml` or `requirements.txt` file.

### Locally

To install instead from your local directory, use:

`pip install -e {PATH_TO_LOCAL_DIR}`.

This corresponds to an [editable install](https://pip.pypa.io/en/stable/topics/local-project-installs/#editable-installs),
useful when you are both using and developing the library at the same time.


## Tutorial

See Python notebook file `tutorial.ipynb` for some examples, which you will of course need to adapt to your own catalog data.

## TODO for release

List of features to be implemented before we can release this SDK

- [x] Configurable API client
- [x] Basic catalog endpoints (get, count and delete content)
- [x] Create user interactions (also get and delete)
- [x] Advanced search endpoints
- [ ] Recommendation endpoints (C2C and U2C, including USF)
- [ ] Simple POST/content from `list` of `dict` (or `JSON` file)
- [ ] Advanced POST/content (splitting large `list` or file by batches)
- [ ] Detailed validation of all contents
- [ ] "GDPR" endpoints
- [ ] (optional?) Implement filters everywhere
- [ ] Documentation (relevant level TBD)
- [ ] Improve error handling (also TBD)
- [ ] Write some unit tests (no need to be exhaustive)
