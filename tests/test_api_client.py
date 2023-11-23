import pytest

from rumo_sdk.api_client import RumoClient


@pytest.mark.parametrize(
    "url, source, expected",
    [
        ("url/", "source", "url/source"),
        ("url", "source", "url/source"),
    ],
)
def test_base_url(url, source, expected):
    api_client = RumoClient(url, source, "")
    assert api_client._base_url == expected


@pytest.mark.parametrize(
    "endpoint, expected",
    [
        ("/a/b/c", "url/mysource/a/b/c"),
        ("a/b/c", "url/mysource/a/b/c"),
    ],
)
def test_generate_url(endpoint, expected):
    api_client = RumoClient("url", "mysource", "")
    assert api_client._generate_url(endpoint) == expected


def test_api_key_in_headers():
    api_client = RumoClient("url", "mysource", "key")
    assert api_client._base_headers == {"x-api-key": "key"}
