import json
from unittest.mock import MagicMock

import pytest
from openapi_core.validation.request.exceptions import InvalidRequestBody

from rumo_sdk.content_api import ContentApi

content_1 = {
    "id": "1",
    "label": "titre",
    "categories": {"tags": [{"weight": 100, "key": "keyword"}]},
}
content_2 = {
    "id": "2",
    "label": "another titre",
    "categories": {"tags": [{"weight": 100, "key": "another keyword"}]},
}


@pytest.fixture
def content_api_mock(api_mock):
    content_api_mock = ContentApi(api_mock)
    content_api_mock.validate_catalog = MagicMock(return_value=True)
    content_api_mock.post_catalog = MagicMock()
    return content_api_mock


@pytest.fixture
def api_mock_validation_error(api_mock):
    api_mock.post = MagicMock(side_effect=InvalidRequestBody)
    return api_mock


@pytest.fixture
def catalog_file(tmp_path_factory):
    filepath = tmp_path_factory.mktemp("data") / "catalog.json"
    catalog = [content_1, content_2]
    with open(filepath, "w") as f:
        json.dump(catalog, f)
    return filepath


def test_post_content(api_mock):
    content_api = ContentApi(api_mock)
    content_api.post_content(content_1)
    api_mock.call_api.assert_called_once_with("POST", "/content", json=[content_1])


def test_post_catalog(api_mock):
    content_api = ContentApi(api_mock)
    catalog = [content_1, content_2]
    content_api.post_catalog(catalog)
    api_mock.call_api.assert_called_once_with("POST", "/content", json=catalog)


def test_validate_content(api_mock):
    content_api = ContentApi(api_mock)
    validation = content_api.validate_content(content_1)
    api_mock.call_api.assert_called_once_with(
        "POST", "/content", json=[content_1], dry_run=True
    )
    assert validation


def test_validate_bad_content(api_mock_validation_error):
    content_api = ContentApi(api_mock_validation_error)
    validation = content_api.validate_content({"id": 2})
    api_mock_validation_error.post.assert_called_once_with(
        "/content", json=[{"id": 2}], dry_run=True
    )
    assert not validation


def test_validate_catalog(api_mock):
    content_api = ContentApi(api_mock)
    catalog = [content_1, content_2]
    content_api.validate_catalog(catalog)
    assert api_mock.call_api.call_count == len(catalog)
    for content, call in zip(catalog, api_mock.call_api.mock_calls):
        assert call.args == ("POST", "/content")
        assert call.kwargs == {"json": [content], "dry_run": True}


def test_upload_from_file(catalog_file, content_api_mock):
    content_api_mock.upload_from_file(catalog_file, batch_size=10)
    content_api_mock.validate_catalog.assert_called_once_with([content_1, content_2])
    content_api_mock.post_catalog.assert_called_once_with(
        [content_1, content_2], batch_size=10
    )


def test_upload_from_file_skip_validation(catalog_file, content_api_mock):
    content_api_mock.upload_from_file(catalog_file, batch_size=10, validate=False)
    content_api_mock.validate_catalog.assert_not_called()
    content_api_mock.post_catalog.assert_called_once_with(
        [content_1, content_2], batch_size=10
    )
