from rumo_sdk.editorial_list_api import EditorialListApi


def test_get_list(api_mock):
    list_api = EditorialListApi(api_mock)
    list_api.get_list()
    api_mock.call_api.assert_called_once_with("GET", "/list")


def test_get_list_by_id(api_mock):
    list_api = EditorialListApi(api_mock)
    list_api.get_list_by_id("listId")
    api_mock.call_api.assert_called_once_with("GET", "/list/listId")


def test_delete_list_by_id(api_mock):
    list_api = EditorialListApi(api_mock)
    list_api.delete_list_by_id("listId")
    api_mock.call_api.assert_called_once_with("DELETE", "/list/listId")


def test_post_list(api_mock):
    list_api = EditorialListApi(api_mock)
    list = {"listId": "1", "listName": "name", "content": ["1", "2", "3", "4", "5"]}
    list_api.post_list(list)
    api_mock.call_api.assert_called_once_with("POST", "/list", json=list)
