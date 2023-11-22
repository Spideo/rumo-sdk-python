from copy import deepcopy
from typing import Optional

from requests import request


class RumoClient:
    def __init__(self, api_url: str, source_id: str, api_key: str):
        self._api_url = api_url.rstrip("/")
        self._api_key = api_key
        self._source_id = source_id

    @property
    def source_id(self):
        return self._source_id

    @property
    def base_headers(self):
        return {"x-api-key": self._api_key}

    @property
    def base_url(self):
        return f"{self._api_url}/{self._source_id}"

    def call_api(
        self,
        method: str,
        endpoint: str,
        query_params: Optional[dict] = None,
        header_params: Optional[dict] = None,
        json: Optional[dict] = None,
        debug: Optional[bool] = False,
    ):
        url = "".join([self.base_url, "/", endpoint.lstrip("/")])
        headers = deepcopy(self.base_headers)
        if header_params is not None:
            headers.update(header_params)
        req = request(method, url, params=query_params, headers=headers, json=json)
        if debug:
            print(f"url: {req.request.url}")
            print(f"path: {req.request.path_url}")
            print(f"headers: {req.request.headers}")
            if hasattr(req.request, "body"):
                print(f"body: {req.request.body}")
        req.raise_for_status()
        return req.json()

    def get(self, endpoint: str, **kwargs):
        return self.call_api("GET", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs):
        return self.call_api("DELETE", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs):
        return self.call_api("POST", endpoint, **kwargs)
