from unittest.mock import MagicMock

import pytest

from rumo_sdk.api_client import RumoClient
from rumo_sdk.content_api import ContentApi


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


def test_get_item_count(api_mock):
    reco_api = ContentApi(api_mock)
    reco_api.get_item_count()
    api_mock.call_api.assert_called_once_with("GET", "/content-count")
