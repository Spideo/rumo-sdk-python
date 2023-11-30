from enum import Enum
from typing import Optional

from rumo_sdk import api_client


class RecoAlgo(Enum):
    COSINE = "cosine"
    JACCARD = "jaccard"


class RecommendationApi:
    def __init__(self, rumo_client: api_client.RumoClient):
        self._rumo_client = rumo_client

    def get_similar(self, content_id: str, algo: Optional[RecoAlgo] = RecoAlgo.COSINE):
        """https://apidoc.rumo.co/#get-/content/-contentId-/similar"""
        endpoint = f"/content/{content_id}/similar"
        params = {"algo": algo.value if algo is not None else None}
        return self._rumo_client.get(endpoint, query_params=params)

    def explain_similar(self, base_content: str, reco_content: str) -> dict:
        """https://apidoc.rumo.co/#get-/content/-contentId-/similar/-contentId-/explain"""  # noqa
        endpoint = f"/content/{base_content}/similar/{reco_content}/explain"
        return self._rumo_client.get(endpoint)

    def get_user_recommendation(
        self, user_id: str, algo: Optional[RecoAlgo] = RecoAlgo.COSINE
    ) -> dict:
        """https://apidoc.rumo.co/#get-/users/-userId-/recommendation"""
        endpoint = f"/users/{user_id}/recommendation"
        params = {"algo": algo.value if algo is not None else None}
        return self._rumo_client.get(endpoint, query_params=params)

    def get_user_profile(self, user_id: str) -> dict:
        """https://apidoc.rumo.co/#get-/users/-userId-/recommendation/profile"""
        endpoint = f"/users/{user_id}/recommendation/profile"
        return self._rumo_client.get(endpoint)
