from unittest.mock import MagicMock

import pytest

from rumo_sdk.api_client import RumoClient
from rumo_sdk.recommendation_api import RecommendationApi


@pytest.fixture
def api_mock():
    api_mock = RumoClient("url", "source", "key")
    api_mock.call_api = MagicMock()
    return api_mock


def test_similar(api_mock):
    reco_api = RecommendationApi(api_mock)
    reco_api.get_similar("content_id")
    api_mock.call_api.assert_called_once_with(
        "GET", "/content/content_id/similar", query_params={"algo": "cosine"}
    )


def test_explain(api_mock):
    reco_api = RecommendationApi(api_mock)
    reco_api.explain_similar("content_a", "content_b")
    api_mock.call_api.assert_called_once_with(
        "GET", "/content/content_a/similar/content_b/explain"
    )


def test_user_reco(api_mock):
    reco_api = RecommendationApi(api_mock)
    reco_api.get_user_recommendation("user_id")
    api_mock.call_api.assert_called_once_with(
        "GET", "/users/user_id/recommendation", query_params={"algo": "cosine"}
    )


def test_user_profile(api_mock):
    reco_api = RecommendationApi(api_mock)
    reco_api.get_user_profile("user_id")
    api_mock.call_api.assert_called_once_with(
        "GET", "/users/user_id/recommendation/profile"
    )
