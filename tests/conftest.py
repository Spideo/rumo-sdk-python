from unittest.mock import MagicMock

import pytest

from rumo_sdk.api_client import RumoClient


@pytest.fixture
def api_mock():
    api_mock = RumoClient("url", "source", "key")
    api_mock.call_api = MagicMock()
    return api_mock
