import json
from typing import Optional

from openapi_core.validation.request.exceptions import InvalidRequestBody

from rumo_sdk import api_client
from rumo_sdk.upload_report import UploadReport
from rumo_sdk.utils import FilterOperatorType, RumoFilters, batched


class ContentApi:
    def __init__(self, rumo_client: api_client.RumoClient):
        self._rumo_client = rumo_client

    def get_items(
        self,
        skip: Optional[int] = 0,
        limit: Optional[int] = 10,
        filters: Optional[RumoFilters.FilterType] = None,
        filter_operator: Optional[FilterOperatorType] = FilterOperatorType.OR,
    ) -> dict:
        """https://apidoc.rumo.co/#get-/content"""
        endpoint = "/content"
        params = {"skip": skip, "limit": limit}
        if filters is not None:
            rumo_filters = RumoFilters(filters, filter_operator)
            params.update(rumo_filters.format_filters_to_query_params())
        return self._rumo_client.get(endpoint, query_params=params)

    def get_items_id(self, **kwargs) -> dict:
        """https://apidoc.rumo.co/#get-/ids"""
        endpoint = "/ids"
        return self._rumo_client.get(endpoint, **kwargs)

    def get_item_by_id(self, content_id: str) -> dict:
        """https://apidoc.rumo.co/#get-/content/-contentId-"""
        endpoint = f"/content/{content_id}"
        return self._rumo_client.get(endpoint)

    def delete_item_by_id(self, content_id: str) -> dict:
        """https://apidoc.rumo.co/#delete-/content/-contentId-"""
        endpoint = f"/content/{content_id}"
        return self._rumo_client.delete(endpoint)

    def _delete_items_by_id(self, contents_id: list[str], **kwargs) -> dict:
        """delete less than 10 contents"""
        endpoint = "/content"
        params = {"id": contents_id}
        return self._rumo_client.delete(endpoint, query_params=params, **kwargs)

    def delete_items_by_id(
        self, catalog: list[dict], batch_size: Optional[int] = 10, **kwargs
    ):
        """https://apidoc.rumo.co/#delete-/content"""
        for batch in batched(catalog, batch_size):
            print(f"\nDeleting batch of {len(batch)} contents")
            self._delete_items_by_id(list(batch), **kwargs)
        print("\nFinished deleting contents.")

    def _delete_all(self) -> dict:
        """https://apidoc.rumo.co/#delete-/content"""
        endpoint = "/content"
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

    def _post_catalog(self, catalog: list[dict], **kwargs) -> dict:
        """send less than 500 contents to Rumo"""
        endpoint = "/content"
        return self._rumo_client.post(endpoint, json=catalog, **kwargs)

    def post_catalog(
        self,
        catalog: list[dict],
        batch_size: Optional[int] = 100,
        report: Optional[bool] = False,
        **kwargs,
    ) -> Optional[UploadReport]:
        """https://apidoc.rumo.co/#post-/content"""
        responses = []
        for batch in batched(catalog, batch_size):
            print(f"\nSending batch of {len(batch)} contents to Rumo API.")
            responses.append(self._post_catalog(list(batch), **kwargs))
        print("\nFinished uploading catalog.")
        if report:
            return UploadReport.build_report(catalog, responses)

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
