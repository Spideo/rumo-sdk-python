from copy import deepcopy
from json import JSONDecodeError
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
    def _base_headers(self):
        return {"x-api-key": self._api_key}

    @property
    def _base_url(self):
        return f"{self._api_url}/{self._source_id}"

    def _generate_url(self, endpoint):
        return "".join([self._base_url, "/", endpoint.lstrip("/")])

    def call_api(
        self,
        method: str,
        endpoint: str,
        query_params: Optional[dict] = None,
        header_params: Optional[dict] = None,
        json: Optional[dict] = None,
        debug: Optional[bool] = False,
    ):
        url = self._generate_url(endpoint)
        headers = deepcopy(self._base_headers)
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
        try:
            res = req.json()
        except JSONDecodeError:
            res = req.status_code
        return res

    def get(self, endpoint: str, **kwargs):
        return self.call_api("GET", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs):
        return self.call_api("DELETE", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs):
        return self.call_api("POST", endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs):
        return self.call_api("PUT", endpoint, **kwargs)
