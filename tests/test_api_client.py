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
    rumo_client = RumoClient(url, source, "")
    assert rumo_client._base_url == expected


@pytest.mark.parametrize(
    "endpoint, expected",
    [
        ("/a/b/c", "url/source/a/b/c"),
        ("a/b/c", "url/source/a/b/c"),
    ],
)
def test_generate_url(endpoint, expected):
    rumo_client = RumoClient("url", "source", "")
    assert rumo_client._generate_url(endpoint) == expected


def test_api_key_in_headers():
    rumo_client = RumoClient("url", "source", "key")
    assert rumo_client._base_headers == {"x-api-key": "key"}


def test_call_api(requests_mock):
    requests_mock.get("https://rumo.com/source/endpoint", json={})
    rumo_client = RumoClient("https://rumo.com", "source", "key")
    rumo_client.call_api("GET", "endpoint")
    assert requests_mock.call_count == 1
    request = requests_mock.last_request
    assert request.method == "GET"
    assert request.url == "https://rumo.com/source/endpoint"
    assert request.path == "/source/endpoint"
    assert {"x-api-key": "key"}.items() <= request.headers.items()


def test_call_api_query_params(requests_mock):
    requests_mock.get("https://rumo.com/source/endpoint", json={})
    rumo_client = RumoClient("https://rumo.com", "source", "key")
    query_params = {"key1": "value1", "key2": "value2"}
    rumo_client.call_api("GET", "endpoint", query_params=query_params)
    assert requests_mock.call_count == 1
    request = requests_mock.last_request
    assert request.url in [
        "https://rumo.com/source/endpoint?key1=value1&key2=value2",
        "https://rumo.com/source/endpoint?key2=value2&key1=value1",
    ]


def test_call_api_headers(requests_mock):
    requests_mock.get("https://rumo.com/source/endpoint", json={})
    rumo_client = RumoClient("https://rumo.com", "source", "key")
    header_params = {"key1": "value1", "key2": "value2"}
    expected_headers = {"key1": "value1", "key2": "value2", "x-api-key": "key"}
    rumo_client.call_api("GET", "endpoint", header_params=header_params)
    assert requests_mock.call_count == 1
    request = requests_mock.last_request
    assert request.url == "https://rumo.com/source/endpoint"
    assert expected_headers.items() <= request.headers.items()
