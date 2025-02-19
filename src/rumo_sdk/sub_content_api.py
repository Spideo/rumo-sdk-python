from typing import Optional, TypedDict

from rumo_sdk.content_api import ContentApi
from rumo_sdk.upload_report import UploadReport
from rumo_sdk.utils import batched


class SubContents(TypedDict):
    contentId: str
    subContentIds: list[str]


class SubContentApi(ContentApi):
    def get_sub_contents(
        self,
        content_id: str,
    ) -> dict:
        """https://apidoc.rumo.co/#get-/content/-contentId-/sub-contents"""
        endpoint = f"/content/{content_id}/sub-contents"
        return self._rumo_client.get(endpoint)

    def get_all_sub_contents(
        self,
        skip: Optional[int] = 0,
        limit: Optional[int] = 10,
    ) -> dict:
        """https://api-doc.rumo.co/#get-/content/sub-contents"""
        endpoint = "/content/sub-contents"
        params = {"skip": skip, "limit": limit}
        return self._rumo_client.get(endpoint, query_params=params)

    def _add_sub_contents(self, list_of_relations: list[SubContents], **kwargs) -> dict:
        """https://apidoc.rumo.co/#post-/content/sub-contents"""
        endpoint = "/content/sub-contents"
        return self._rumo_client.post(endpoint, json=list_of_relations, **kwargs)

    def add_sub_contents(
        self,
        list_of_relations: list[SubContents],
        batch_size: Optional[int] = 100,
        report: Optional[bool] = False,
        **kwargs,
    ):
        """https://apidoc.rumo.co/#post-/content/sub-contents"""
        responses = []
        for batch in batched(list_of_relations, batch_size):
            print(f"\nSending batch of {len(batch)} sub-content relations to Rumo API.")
            responses.append(self._add_sub_contents(batch, **kwargs))
        print("\nFinished uploading sub-contents.")
        if report:
            return UploadReport.build_report(list_of_relations, responses)

    def delete_sub_contents(self, content_id: str) -> dict:
        """https://apidoc.rumo.co/#get-/content/-contentId-/sub-contents"""
        endpoint = f"/content/{content_id}/sub-contents"
        return self._rumo_client.delete(endpoint)
