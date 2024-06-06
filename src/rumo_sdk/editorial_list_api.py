from rumo_sdk import api_client


class EditorialListApi:
    def __init__(self, rumo_client: api_client.RumoClient):
        self._rumo_client = rumo_client

    def get_lists(self) -> dict:
        """https://apidoc.rumo.co/#get-/list"""
        endpoint = "/list"
        return self._rumo_client.get(endpoint)

    def get_list_by_id(self, list_id: str) -> dict:
        """https://apidoc.rumo.co/#get-/list/-listId-"""
        endpoint = f"/list/{list_id}"
        return self._rumo_client.get(endpoint)

    def delete_list_by_id(self, list_id: str) -> dict:
        """https://apidoc.rumo.co/#delete-/list/-listId-"""
        endpoint = f"/list/{list_id}"
        return self._rumo_client.delete(endpoint)

    def post_list(self, list: dict) -> dict:
        """https://apidoc.rumo.co/#post-/list"""
        endpoint = "/list"
        return self._rumo_client.post(endpoint, json=list)
