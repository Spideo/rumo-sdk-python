from unittest.mock import MagicMock

import pytest

from rumo_sdk.api_client import RumoClient
from rumo_sdk.interactions_api import InteractionsApi, InteractionType


@pytest.fixture
def api_mock():
    api_mock = RumoClient("url", "source", "key")
    api_mock.call_api = MagicMock()
    return api_mock


@pytest.fixture
def interactions_mock():
    api_mock = RumoClient("url", "source", "key")
    search_api = InteractionsApi(api_mock)
    search_api._post_interaction = MagicMock()
    return search_api


def test_post_interactions(api_mock):
    interactions_api = InteractionsApi(api_mock)
    interactions_api._post_interaction("uid", InteractionType.CLICK, "cid")
    api_mock.call_api.assert_called_once_with(
        "POST", "/users/uid/interactions/click/content/cid"
    )


def test_delete_interaction(api_mock):
    interactions_api = InteractionsApi(api_mock)
    interactions_api.delete_interaction("uid", InteractionType.SHARE, "cid")
    api_mock.call_api.assert_called_once_with(
        "DELETE", "/users/uid/interactions/share/content/cid"
    )


@pytest.mark.parametrize(
    "kwargs",
    [
        ({}),
        ({"skip": 2, "limit": 3}),
        ({"content_id": "cid"}),
        ({"interaction_type": InteractionType.START}),
        ({"content_id": "cid", "interaction_type": InteractionType.DISLIKE}),
        (
            {
                "skip": 2,
                "limit": 3,
                "content_id": "cid",
                "interaction_type": InteractionType.LIKE,
            }
        ),
    ],
)
def test_get_interactions(api_mock, kwargs):
    interactions_api = InteractionsApi(api_mock)
    interactions_api.get_interactions("uid", **kwargs)
    qtype = kwargs["interaction_type"].value if "interaction_type" in kwargs else None
    query_params = {
        "skip": kwargs.get("skip", 0),
        "limit": kwargs.get("limit", 10),
        "contentId": kwargs.get("content_id", None),
        "type": qtype,
    }
    api_mock.call_api.assert_called_once_with(
        "GET", "/users/uid/interactions", query_params=query_params
    )


def test_click(interactions_mock):
    interactions_mock.click("uid", "cid")
    interactions_mock._post_interaction.assert_called_once_with(
        "uid", InteractionType.CLICK, "cid"
    )


def test_purchase(interactions_mock):
    interactions_mock.purchase("uid", "cid")
    interactions_mock._post_interaction.assert_called_once_with(
        "uid", InteractionType.PURCHASE, "cid"
    )


def test_bookmark(interactions_mock):
    interactions_mock.bookmark("uid", "cid")
    interactions_mock._post_interaction.assert_called_once_with(
        "uid", InteractionType.BOOKMARK, "cid"
    )


def test_like(interactions_mock):
    interactions_mock.like("uid", "cid")
    interactions_mock._post_interaction.assert_called_once_with(
        "uid", InteractionType.LIKE, "cid"
    )


def test_dislike(interactions_mock):
    interactions_mock.dislike("uid", "cid")
    interactions_mock._post_interaction.assert_called_once_with(
        "uid", InteractionType.DISLIKE, "cid"
    )


def test_more_info(interactions_mock):
    interactions_mock.more_info("uid", "cid")
    interactions_mock._post_interaction.assert_called_once_with(
        "uid", InteractionType.MOREINFO, "cid"
    )


def test_start(interactions_mock):
    interactions_mock.start("uid", "cid")
    interactions_mock._post_interaction.assert_called_once_with(
        "uid", InteractionType.START, "cid"
    )


def test_complete(interactions_mock):
    interactions_mock.complete("uid", "cid")
    interactions_mock._post_interaction.assert_called_once_with(
        "uid", InteractionType.COMPLETE, "cid"
    )


def test_add_to_list(interactions_mock):
    interactions_mock.add_to_list("uid", "cid")
    interactions_mock._post_interaction.assert_called_once_with(
        "uid", InteractionType.ADDTOLIST, "cid"
    )


def test_share(interactions_mock):
    interactions_mock.share("uid", "cid")
    interactions_mock._post_interaction.assert_called_once_with(
        "uid", InteractionType.SHARE, "cid"
    )
