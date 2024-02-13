from copy import deepcopy
from json import JSONDecodeError
from typing import Optional

from openapi_core.contrib.requests import (
    RequestsOpenAPIRequest,
    RequestsOpenAPIResponse,
)
from requests import HTTPError, Request, Session

from rumo_sdk import open_api


class RumoClient:
    def __init__(
        self,
        api_url: str,
        source_id: str,
        api_key: str,
        openapi_type: Optional[open_api.OpenApiType] = open_api.OpenApiType.DEFAULT,
        openapi_source: Optional[str] = None,
    ):
        self._api_url = api_url.rstrip("/")
        self._api_key = api_key
        self.source_id = source_id
        self.openapi = open_api.get_openapi(openapi_type, openapi_source)

    @property
    def _base_headers(self) -> dict:
        return {"x-api-key": self._api_key}

    @property
    def _base_url(self) -> str:
        return f"{self._api_url}/{self.source_id}"

    def _generate_url(self, endpoint: str) -> str:
        return "".join([self._base_url, "/", endpoint.lstrip("/")])

    def call_api(
        self,
        method: str,
        endpoint: str,
        query_params: Optional[dict] = None,
        header_params: Optional[dict] = None,
        json: Optional[dict] = None,
        debug: Optional[bool] = False,
        validate_request: Optional[bool] = True,
        validate_response: Optional[bool] = False,
        dry_run: Optional[bool] = False,
    ) -> dict:
        url = self._generate_url(endpoint)
        headers = deepcopy(self._base_headers)
        if header_params is not None:
            headers.update(header_params)
        req = Request(method, url, params=query_params, headers=headers, json=json)
        if debug:
            for attribute in ["url", "headers", "params", "data", "files", "json"]:
                print(f"{attribute}: {getattr(req, attribute, None)}")
        if validate_request and self.openapi is not None:
            openapi_request = RequestsOpenAPIRequest(req)
            self.openapi.validate_request(openapi_request)
        if dry_run:
            return {"dry_run": True}
        prepped = req.prepare()
        session = Session()
        response = session.send(prepped)
        try:
            response.raise_for_status()
        except HTTPError:
            print(f"Response status code: {response.status_code}")
            try:
                print(f"Response message: {response.json()}")
            except JSONDecodeError:
                pass
            raise
        if validate_response and self.openapi is not None:
            openapi_response = RequestsOpenAPIResponse(response)
            self.openapi.validate_response(openapi_request, openapi_response)
        try:
            res = response.json()
        except JSONDecodeError:
            res = {"status_code": response.status_code}
        return res

    def get(self, endpoint: str, **kwargs) -> dict:
        return self.call_api("GET", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> dict:
        return self.call_api("DELETE", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs) -> dict:
        return self.call_api("POST", endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs) -> dict:
        return self.call_api("PUT", endpoint, **kwargs)
