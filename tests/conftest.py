from unittest.mock import MagicMock

import pytest

from rumo_sdk.api_client import RumoClient
from rumo_sdk.open_api import OpenApiType


@pytest.fixture
def api_mock():
    api_mock = RumoClient("url", "source", "key", openapi_type=OpenApiType.NONE)
    api_mock.call_api = MagicMock()
    return api_mock
