from enum import Enum
from typing import Optional
from urllib.request import urlopen

from openapi_core import OpenAPI

RUMO_API_URL = "https://apidoc.rumo.co/rumo_api.yaml"


class OpenApiType(Enum):
    NONE = None
    DEFAULT = "default"
    URL = "URL"
    FILE = "FILE"


def get_openapi(
    openapi_type: OpenApiType, openapi_source: Optional[str] = None
) -> Optional[OpenAPI]:
    match openapi_type:
        case OpenApiType.NONE:
            return None
        case OpenApiType.DEFAULT:
            return openapi_from_url(RUMO_API_URL)
        case OpenApiType.URL:
            return openapi_from_url(openapi_source)
        case OpenApiType.FILE:
            return openapi_from_file(openapi_source)


def openapi_from_url(url: str) -> OpenAPI:
    with urlopen(url) as f:
        openapi = OpenAPI.from_file(f)
    return openapi


def openapi_from_file(filepath: str) -> OpenAPI:
    return OpenAPI.from_file_path(filepath)
