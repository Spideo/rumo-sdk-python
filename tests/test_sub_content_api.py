from unittest.mock import MagicMock

import pytest

from rumo_sdk.sub_content_api import SubContentApi

relations = [
    {"contentId": "series_1", "subContentIds": ["ep-1", "ep-2", "ep-3"]},
    {"contentId": "series_2", "subContentIds": ["ep-A", "ep-B"]},
    {"contentId": "series_3", "subContentIds": ["ep-A"]},
    {"contentId": "series_4", "subContentIds": ["episode"]},
    {"contentId": "series_5", "subContentIds": ["title_1", "title_2"]},
]


@pytest.fixture
def sub_content_mock(api_mock):
    sub_content_api_mock = SubContentApi(api_mock)
    sub_content_api_mock._add_sub_contents = MagicMock()
    return sub_content_api_mock


def test_get_sub_contents(api_mock):
    sub_content_api = SubContentApi(api_mock)
    sub_content_api.get_sub_contents("id")
    api_mock.call_api.assert_called_once_with("GET", "/content/id/sub-contents")


def test_get_all_sub_contents(api_mock):
    sub_content_api = SubContentApi(api_mock)
    sub_content_api.get_all_sub_contents(skip=2)
    expected_params = {"skip": 2, "limit": 10}
    api_mock.call_api.assert_called_once_with(
        "GET", "/content/sub-contents", query_params=expected_params
    )


def test_delete_sub_contents(api_mock):
    sub_content_api = SubContentApi(api_mock)
    sub_content_api.delete_sub_contents("id")
    api_mock.call_api.assert_called_once_with("DELETE", "/content/id/sub-contents")


def test_internal_add_sub_contents(api_mock):
    sub_content_api = SubContentApi(api_mock)
    sub_content_api._add_sub_contents(relations)
    api_mock.call_api.assert_called_once_with(
        "POST", "/content/sub-contents", json=relations
    )


def test_add_sub_contents_one_batch(sub_content_mock):
    sub_content_mock.add_sub_contents(relations)
    sub_content_mock._add_sub_contents.assert_called_once_with(tuple(relations))


def test_add_sub_contents_multiple_batches(sub_content_mock):
    sub_content_mock.add_sub_contents(relations, batch_size=3)
    calls = sub_content_mock._add_sub_contents.mock_calls
    assert len(calls) == 2
    assert calls[0].args == (tuple(relations[:3]),)
    assert calls[1].args == (tuple(relations[3:]),)
