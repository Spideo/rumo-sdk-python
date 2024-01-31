import pytest

from rumo_sdk.users_api import UsersApi


def test_get_user_choice(api_mock):
    reco_api = UsersApi(api_mock)
    reco_api.get_user_tracking_choice("user_id")
    api_mock.call_api.assert_called_once_with("GET", "/users/user_id")


@pytest.mark.parametrize("boolean, parameter", [(True, "true"), (False, "false")])
def test_set_user_choice(boolean, parameter, api_mock):
    reco_api = UsersApi(api_mock)
    reco_api.set_user_tracking_choice("user_id", boolean)
    api_mock.call_api.assert_called_once_with(
        "PUT", "/users/user_id", query_params={"tracked": parameter}
    )


def test_delete_user_history(api_mock):
    reco_api = UsersApi(api_mock)
    reco_api.delete_user_history("user_id")
    api_mock.call_api.assert_called_once_with("DELETE", "/users/user_id")
