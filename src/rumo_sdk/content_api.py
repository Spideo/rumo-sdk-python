from typing import Optional

from rumo_sdk import api_client


class ContentApi:
    def __init__(self, rumo_client: api_client.RumoClient):
        self._rumo_client = rumo_client

    def get_items(self, skip: Optional[int] = 0, limit: Optional[int] = 10) -> dict:
        """https://apidoc.rumo.co/#get-/content"""
        endpoint = "/content"
        params = {"skip": skip, "limit": limit}
        return self._rumo_client.get(endpoint, query_params=params)

    def get_item_by_id(self, content_id: str) -> dict:
        """https://apidoc.rumo.co/#get-/content/-contentId-"""
        endpoint = f"/content/{content_id}"
        return self._rumo_client.get(endpoint)

    def delete_item_by_id(self, content_id: str) -> dict:
        """https://apidoc.rumo.co/#delete-/content/-contentId-"""
        endpoint = f"/content/{content_id}"
        return self._rumo_client.delete(endpoint)

    def get_item_count(self) -> int:
        """https://apidoc.rumo.co/#get-/count-content"""
        endpoint = "/content-count"
        response = self._rumo_client.get(endpoint)
        return response["count"]
