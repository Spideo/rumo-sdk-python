---
description: "Review changes against Rumo SDK guidelines. Use `/review` for local changes, or `/review COMMIT_RANGE` for commits (e.g. `HEAD~3..HEAD`, `main..HEAD`)."
agent: "agent"
argument-hint: "Optional: commit range like HEAD~3..HEAD or main..HEAD. Omit to review staged/unstaged changes."
tools: [get_changed_files, read_file, run_in_terminal]
---

Review changes in this repository against the project guidelines in [copilot-instructions.md](../copilot-instructions.md).

**Argument**: Leave blank to review your current working directory changes (staged + unstaged). Provide a commit range (e.g., `HEAD~3..HEAD` or `main..HEAD`) to review specific commits.

## Steps

1. **Get the diff** — if no argument: run `git diff HEAD` to see unstaged changes. If argument provided: run `git diff <argument>` to see commits in that range.
2. **Read changed files** — read the full content of any modified source or test files.
3. **Check each guideline below** and flag any violations with file + line reference.

## Checklist

### API module conventions
- [ ] Every new API class follows `class FooApi: def __init__(self, rumo_client: RumoClient)` — no other constructor pattern
- [ ] All public methods pass `**kwargs` through to the underlying `self._rumo_client` call
- [ ] No direct use of `requests` — all HTTP goes through `RumoClient`

### Filters
- [ ] Dict filters are converted via `RumoFilters(...).format_filters_to_query_params()` — not built manually

### Bulk operations
- [ ] Bulk methods use `batched()` from `utils.py` with a configurable `batch_size` defaulting to `10`
- [ ] The public method orchestrates batches; single-batch logic lives in a private `_method()`

### Tests
- [ ] New API methods have corresponding tests
- [ ] Tests use the `api_mock` fixture from `conftest.py` — not a real `RumoClient`
- [ ] Assertions use `api_mock.call_api.assert_called_once_with(...)` style
- [ ] No `OpenApiType` other than `NONE` used in unit tests
- [ ] HTTP-level tests (if any) use `requests_mock`, not live network calls

### General
- [ ] No new dependencies added to `pyproject.toml` without justification
- [ ] `__version__` not hardcoded — it's resolved via `importlib.metadata`

## Output format

For each violation, output:
> **[FAIL]** `path/to/file.py:line` — _what rule was broken and why_

For each area with no issues:
> **[PASS]** _area name_

End with a one-line summary: total passes, total failures, and the single most important fix if any failures exist.
