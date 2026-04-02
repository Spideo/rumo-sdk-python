# Rumo Python SDK – Project Guidelines

Python SDK for the [Rumo recommendation API](https://apidoc.rumo.co/). Wraps HTTP calls with optional OpenAPI request/response validation.

## Build and Test

```bash
poetry install          # install all dependency groups

make test               # run pytest -v
make test-cov           # run with coverage report (HTML + terminal)

make format             # black + isort (auto-fix)
make lint               # black + isort + flake8 (check only)
make pytype             # static type checking
```

All commands run via `poetry run` — ensure Poetry is active.

## Architecture

Three-layer structure:

1. **`api_client.py` — `RumoClient`**: HTTP foundation. Constructs URLs as `{base_url}/{source_id}/{endpoint}`, injects `x-api-key` header, runs OpenAPI validation, supports `dry_run` and `debug` flags.
2. **`open_api.py`**: Loads the OpenAPI spec (default: remote YAML, or local file). Returns `None` for `OpenApiType.NONE` — used in tests to skip validation.
3. **API modules** (`content_api.py`, `recommendation_api.py`, etc.): Thin wrappers over `RumoClient`. Each class takes a `RumoClient` in `__init__` and delegates to `self._rumo_client.get/post/put/delete()`.

`utils.py` provides `batched()`, `RumoFilters`, `FilterOperatorType`, and `ItemType` shared across modules.

## Conventions

**API module pattern** — every API class follows the same shape:
```python
class FooApi:
    def __init__(self, rumo_client: RumoClient):
        self._rumo_client = rumo_client

    def do_something(self, ..., **kwargs):
        return self._rumo_client.get("/endpoint", query_params={...}, **kwargs)
```
Pass `**kwargs` through to `call_api` so callers can set `validate_request`, `validate_response`, `dry_run`, `debug`.

**Filters** — convert dict filters via `RumoFilters`:
```python
RumoFilters({"genre": ["action", "drama"]}).format_filters_to_query_params()
# → {"filters": ["genre:action,drama"], "filterOperator": "OR"}
```

**Bulk operations** — use `batched()` from `utils.py` with a configurable `batch_size` (default `10`). Keep the public method as the orchestrator and the single-batch logic in a private `_method()`.

## Testing

- Fixtures live in `tests/conftest.py`. The core fixture is `api_mock`: a `RumoClient` with `OpenApiType.NONE` and `call_api` replaced by `MagicMock()`.
- Unit tests instantiate an API class with `api_mock`, call a method, then assert `api_mock.call_api.assert_called_once_with(...)`.
- Integration/HTTP-level tests use `requests_mock` (see `test_api_client.py`).
- Do **not** enable real OpenAPI validation in unit tests — keep `OpenApiType.NONE`.

## Pitfalls

- **JSONDecodeError fallback**: empty or non-JSON responses return `{"status_code": <code>}` instead of raising.
- **Endpoint normalization**: `_generate_url()` strips leading slashes — pass endpoints with or without `/`.
- **`dry_run=True`** skips the network call entirely and returns `{"dry_run": True}`; useful for validating request shape without side effects.
- **`__version__`** is loaded dynamically via `importlib.metadata.version("rumo-sdk")` — the package must be installed for it to resolve.
