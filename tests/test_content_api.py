from unittest.mock import MagicMock

import pytest

from rumo_sdk.api_client import RumoClient
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
def api_mock():
    api_mock = RumoClient("url", "source", "key")
    api_mock.call_api = MagicMock()
    return api_mock


def test_get_items(api_mock):
    reco_api = ContentApi(api_mock)
    reco_api.get_items()
    api_mock.call_api.assert_called_once_with(
        "GET", "/content", query_params={"skip": 0, "limit": 10}
    )


def test_get_items_skip_limit(api_mock):
    reco_api = ContentApi(api_mock)
    reco_api.get_items(skip=2, limit=3)
    api_mock.call_api.assert_called_once_with(
        "GET", "/content", query_params={"skip": 2, "limit": 3}
    )


def test_get_item_by_id(api_mock):
    reco_api = ContentApi(api_mock)
    reco_api.get_item_by_id("contentId")
    api_mock.call_api.assert_called_once_with("GET", "/content/contentId")


def test_delete_item_by_id(api_mock):
    reco_api = ContentApi(api_mock)
    reco_api.delete_item_by_id("contentId")
    api_mock.call_api.assert_called_once_with("DELETE", "/content/contentId")


def test_delete_all(api_mock):
    reco_api = ContentApi(api_mock)
    reco_api._delete_all()
    api_mock.call_api.assert_called_once_with("DELETE", "/content")


def test_get_item_count(api_mock):
    reco_api = ContentApi(api_mock)
    reco_api.get_item_count()
    api_mock.call_api.assert_called_once_with("GET", "/content-count")


def test_post_content(api_mock):
    reco_api = ContentApi(api_mock)
    reco_api.post_content(content_1)
    api_mock.call_api.assert_called_once_with("POST", "/content", json=[content_1])


def test_post_catalog(api_mock):
    reco_api = ContentApi(api_mock)
    catalog = [content_1, content_2]
    reco_api.post_catalog(catalog)
    api_mock.call_api.assert_called_once_with("POST", "/content", json=catalog)


def test_validate_content(api_mock):
    reco_api = ContentApi(api_mock)
    reco_api.validate_content(content_1)
    api_mock.call_api.assert_called_once_with(
        "POST", "/content", json=[content_1], dry_run=True
    )


def test_validate_catalog(api_mock):
    reco_api = ContentApi(api_mock)
    catalog = [content_1, content_2]
    reco_api.validate_catalog(catalog)
    assert api_mock.call_api.call_count == len(catalog)
    for content, call in zip(catalog, api_mock.call_api.mock_calls):
        assert call.args == ("POST", "/content")
        assert call.kwargs == {"json": [content], "dry_run": True}
