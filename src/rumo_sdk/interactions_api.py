from enum import Enum
from typing import Optional


class InteractionType(Enum):
    CLICK = "click"
    PURCHASE = "purchase"
    BOOKMARK = "bookmark"
    LIKE = "like"
    DISLIKE = "dislike"
    MOREINFO = "moreInfo"
    START = "start"
    COMPLETE = "complete"
    ADDTOLIST = "addToList"
    SHARE = "share"


class InteractionsApi:
    """https://apidoc.rumo.co/#post-/users/-userId-/interactions/-interactionType-/content/-contentId-"""  # noqa

    def __init__(self, api_client):
        self._api_client = api_client

    def _post_interaction(
        self, user_id: str, interaction_type: InteractionType, content_id: str
    ) -> dict:
        endpoint = "".join(
            [
                f"/users/{user_id}",
                f"/interactions/{interaction_type.value}",
                f"/content/{content_id}",
            ]
        )
        return self._api_client.post(endpoint)

    def delete_interaction(
        self, user_id: str, interaction_type: str, content_id: str
    ) -> dict:
        endpoint = (
            f"/user/{user_id}/interactions/{interaction_type}/content/{content_id}"
        )
        return self._api_client.delete(endpoint)

    def get_interactions(
        self,
        user_id: str,
        interaction_type: Optional[str] = None,
        content_id: Optional[str] = None,
        skip: Optional[int] = 0,
        limit: Optional[int] = 10,
    ) -> dict:
        endpoint = f"/users/{user_id}/interactions"
        params = {
            "type": interaction_type,
            "contentId": content_id,
            "skip": skip,
            "limit": limit,
        }
        return self._api_client.get(endpoint, query_params=params)

    def click(self, user_id: str, content_id: str) -> dict:
        return self._post_interaction(user_id, InteractionType.CLICK, content_id)

    def purchase(self, user_id: str, content_id: str) -> dict:
        return self._post_interaction(user_id, InteractionType.PURCHASE, content_id)

    def bookmark(self, user_id: str, content_id: str) -> dict:
        return self._post_interaction(user_id, InteractionType.BOOKMARK, content_id)

    def like(self, user_id: str, content_id: str) -> dict:
        return self._post_interaction(user_id, InteractionType.LIKE, content_id)

    def dislike(self, user_id: str, content_id: str) -> dict:
        return self._post_interaction(user_id, InteractionType.DISLIKE, content_id)

    def more_info(self, user_id: str, content_id: str) -> dict:
        return self._post_interaction(user_id, InteractionType.MOREINFO, content_id)

    def start(self, user_id: str, content_id: str) -> dict:
        return self._post_interaction(user_id, InteractionType.START, content_id)

    def complete(self, user_id: str, content_id: str) -> dict:
        return self._post_interaction(user_id, InteractionType.COMPLETE, content_id)

    def add_to_list(self, user_id: str, content_id: str) -> dict:
        return self._post_interaction(user_id, InteractionType.ADDTOLIST, content_id)

    def share(self, user_id: str, content_id: str) -> dict:
        return self._post_interaction(user_id, InteractionType.SHARE, content_id)
