from rumo_sdk import api_client


class UsersApi:
    def __init__(self, api_client: api_client.RumoClient):
        self._api_client = api_client

    def get_user_tracking_choice(self, user_id: str) -> dict:
        """https://apidoc.rumo.co/#get-/users/-userId-"""
        endpoint = f"/users/{user_id}"
        return self._api_client.get(endpoint)

    def set_user_tracking_choice(self, user_id: str, tracked: bool) -> dict:
        """https://apidoc.rumo.co/#put-/users/-userId-"""
        endpoint = f"/users/{user_id}"
        return self._api_client.put(
            endpoint, query_params={"tracked": str(tracked).lower()}
        )

    def delete_user_history(self, user_id: str) -> dict:
        """https://apidoc.rumo.co/#delete-/users/-userId-"""
        endpoint = f"/users/{user_id}"
        return self._api_client.delete(endpoint)
