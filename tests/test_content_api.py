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


def test_delete_all(api_mock):
    content_api = ContentApi(api_mock)
    content_api._delete_all()
    api_mock.call_api.assert_called_once_with("DELETE", "/content")


def test_get_item_count(api_mock):
    content_api = ContentApi(api_mock)
    content_api.get_item_count()
    api_mock.call_api.assert_called_once_with("GET", "/content-count")
