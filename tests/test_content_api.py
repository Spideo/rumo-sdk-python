from unittest.mock import call

from rumo_sdk.content_api import ContentApi


def test_get_items(api_mock):
    content_api = ContentApi(api_mock)
    content_api.get_items()
    api_mock.call_api.assert_called_once_with(
        "GET", "/content", query_params={"skip": 0, "limit": 10}
    )


def test_get_items_skip_limit(api_mock):
    content_api = ContentApi(api_mock)
    content_api.get_items(skip=2, limit=3)
    api_mock.call_api.assert_called_once_with(
        "GET", "/content", query_params={"skip": 2, "limit": 3}
    )


def test_get_items_filters(api_mock):
    reco_api = ContentApi(api_mock)
    filters = {"f_a": ["v_a", "v_b"], "f_b": ["v_c"]}
    reco_api.get_items(filters=filters)
    api_mock.call_api.assert_called_once_with(
        "GET",
        "/content",
        query_params={
            "skip": 0,
            "limit": 10,
            "filters": ["f_a:v_a,v_b", "f_b:v_c"],
            "filterOperator": "OR",
        },
    )


def test_get_items_id(api_mock):
    content_api = ContentApi(api_mock)
    content_api.get_items_id()
    api_mock.call_api.assert_called_once_with("GET", "/ids")


def test_get_item_by_id(api_mock):
    content_api = ContentApi(api_mock)
    content_api.get_item_by_id("contentId")
    api_mock.call_api.assert_called_once_with("GET", "/content/contentId")


def test_delete_item_by_id(api_mock):
    content_api = ContentApi(api_mock)
    content_api.delete_item_by_id("contentId")
    api_mock.call_api.assert_called_once_with("DELETE", "/content/contentId")


def test_delete_items_by_id(api_mock):
    content_api = ContentApi(api_mock)
    contents_id = ["1", "2", "3"]
    content_api.delete_items_by_id(contents_id)
    api_mock.call_api.assert_called_once_with(
        "DELETE", "/content", query_params={"id": contents_id}
    )


def test_delete_items_by_id_by_batch(api_mock):
    content_api = ContentApi(api_mock)
    contents_id = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
    content_api.delete_items_by_id(contents_id)
    expectedCalls = [
        call(
            "DELETE",
            "/content",
            query_params={"id": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]},
        ),
        call(
            "DELETE",
            "/content",
            query_params={"id": ["11"]},
        ),
    ]
    api_mock.call_api.assert_has_calls(expectedCalls, any_order=False)


def test_delete_all(api_mock):
    content_api = ContentApi(api_mock)
    content_api._delete_all()
    api_mock.call_api.assert_called_once_with("DELETE", "/all-content")


def test_get_item_count(api_mock):
    content_api = ContentApi(api_mock)
    content_api.get_item_count()
    api_mock.call_api.assert_called_once_with("GET", "/content-count")
