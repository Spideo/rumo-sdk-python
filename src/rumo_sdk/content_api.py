import json
from typing import Optional

from openapi_core.validation.request.exceptions import InvalidRequestBody

from rumo_sdk import api_client
from rumo_sdk.utils import batched


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

    def post_content(self, content: dict) -> dict:
        """https://apidoc.rumo.co/#post-/content"""
        endpoint = "/content"
        return self._rumo_client.post(endpoint, json=[content])

    def _post_catalog(self, catalog: list[dict]) -> dict:
        """send less than 500 contents to Rumo"""
        endpoint = "/content"
        return self._rumo_client.post(endpoint, json=catalog)

    def post_catalog(self, catalog: list[dict], batch_size: Optional[int] = 100):
        """https://apidoc.rumo.co/#post-/content"""
        for batch in batched(catalog, batch_size):
            print(f"\nSending batch of {len(batch)} contents to Rumo API.")
            self._post_catalog(list(batch))
        print("\nFinished uploading catalog.")

    def validate_content(self, content: dict) -> bool:
        endpoint = "/content"
        try:
            self._rumo_client.post(endpoint, json=[content], dry_run=True)
        except InvalidRequestBody as e:
            print(f"Invalid content with ID: {content.get('id')}")
            print(f"Validation error: {e.__cause__}\n")
            return False
        else:
            return True

    def validate_catalog(self, catalog: list[dict]) -> bool:
        validated = [self.validate_content(content) for content in catalog]
        if all(validated):
            print("All contents in catalog appear to be valid.")
        else:
            print("There are errors in the catalog.")
            total_errors = len(validated) - sum(validated)
            print(f"{total_errors} out of {len(catalog)} content items are in error.")
        return all(validated)

    def upload_from_file(
        self,
        filename: str,
        batch_size: Optional[int] = 100,
        validate: Optional[bool] = True,
    ):
        with open(filename, "r") as f:
            catalog = json.load(f)
        print(f"\nRead {len(catalog)} contents.")
        if validate:
            print("\nValidating catalog contents.")
            if not self.validate_catalog(catalog):
                return
        print(f"\nRead {len(catalog)} contents, now validating content.")
        return self.post_catalog(catalog, batch_size=batch_size)
