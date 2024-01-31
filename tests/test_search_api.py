from unittest.mock import MagicMock

import pytest

from rumo_sdk.search_api import SearchApi


@pytest.fixture
def search_mock(api_mock):
    search_api = SearchApi(api_mock)
    search_api._advanced_search = MagicMock()
    return search_api


def test_advanced_search(api_mock):
    search_api = SearchApi(api_mock)
    search_params = {"key1": "value1", "key2": "value2"}
    search_api._advanced_search(search_params)
    api_mock.call_api.assert_called_once_with(
        "POST",
        "/search/advanced",
        header_params={"Content-Type": "application/json"},
        query_params={"skip": 0, "limit": 10, "details": "false"},
        json=search_params,
    )


def test_advanced_search_query_params(api_mock):
    search_api = SearchApi(api_mock)
    search_params = {"key1": "value1", "key2": "value2"}
    query_params = {"skip": 2, "limit": 3, "details": True}
    search_api._advanced_search(search_params, **query_params)
    api_mock.call_api.assert_called_once_with(
        "POST",
        "/search/advanced",
        header_params={"Content-Type": "application/json"},
        query_params={"skip": 2, "limit": 3, "details": "true"},
        json=search_params,
    )


def test_search_by_keyword_nokwargs(search_mock):
    search_mock.search_by_keyword("keyword")
    search_mock._advanced_search.assert_called_once_with(
        {
            "searchParameter": {
                "field": "categoriesFull.keyword",
                "comparator": "EQ",
                "value": "keyword",
            }
        }
    )


def test_search_by_keyword(search_mock):
    search_mock.search_by_keyword("keyword", skip=3, details=True)
    search_mock._advanced_search.assert_called_once_with(
        {
            "searchParameter": {
                "field": "categoriesFull.keyword",
                "comparator": "EQ",
                "value": "keyword",
            }
        },
        skip=3,
        details=True,
    )


def test_search_by_keyword_in_category(search_mock):
    search_mock.search_by_keyword_in_category(
        "keyword", "categorie", limit=1, details=False
    )
    search_mock._advanced_search.assert_called_once_with(
        {
            "searchParameter": {
                "field": "categories.categorie.keyword",
                "comparator": "EQ",
                "value": "keyword",
            }
        },
        limit=1,
        details=False,
    )


def test_search_label_exact(search_mock):
    search_mock.search_label_exact("title")
    search_mock._advanced_search.assert_called_once_with(
        {
            "searchParameter": {
                "field": "label",
                "comparator": "EQ",
                "value": "title",
            }
        }
    )


def test_search_label_contains(search_mock):
    search_mock.search_label_contains("title", details=True)
    search_mock._advanced_search.assert_called_once_with(
        {
            "searchParameter": {
                "field": "label.text",
                "comparator": "CONTAINS",
                "value": "title",
            }
        },
        details=True,
    )


def test_search_label_fuzzy(search_mock):
    search_mock.search_label_fuzzy("title", limit=2)
    search_mock._advanced_search.assert_called_once_with(
        {
            "searchParameter": {
                "field": "label.text",
                "comparator": "LIKE",
                "value": "title",
            }
        },
        limit=2,
    )
