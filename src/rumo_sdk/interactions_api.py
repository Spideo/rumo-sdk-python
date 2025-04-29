from enum import Enum
from typing import Optional

from rumo_sdk import api_client


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


class TargetType(Enum):
    CONTENT = "content"
    KEYWORD = "keyword"


class InteractionsApi:
    """https://apidoc.rumo.co/#post-/users/-userId-/interactions/-interactionType-/content/-contentId-"""  # noqa

    def __init__(self, rumo_client: api_client.RumoClient):
        self._rumo_client = rumo_client

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
        return self._rumo_client.post(endpoint)

    def delete_interaction(
        self, user_id: str, interaction_type: InteractionType, content_id: str
    ) -> dict:
        _type = interaction_type.value
        endpoint = f"/users/{user_id}/interactions/{_type}/content/{content_id}"
        return self._rumo_client.delete(endpoint)

    def post_interaction_on_keyword(
        self,
        user_id: str,
        interaction_type: InteractionType,
        category: str,
        keyword: str,
    ) -> dict:
        """https://apidoc.rumo.co/#post-/users/-userId-/interactions/-interactionType-/category/-category-/keyword/-keyword-"""  # noqa
        endpoint = "".join(
            [
                f"/users/{user_id}",
                f"/interactions/{interaction_type.value}",
                f"/category/{category}",
                f"/keyword/{keyword}",
            ]
        )
        return self._rumo_client.post(endpoint)

    def delete_interaction_on_keyword(
        self,
        user_id: str,
        interaction_type: InteractionType,
        category: str,
        keyword: str,
    ) -> dict:
        """https://apidoc.rumo.co/#delete-/users/-userId-/interactions/-interactionType-/category/-category-/keyword/-keyword-"""  # noqa
        endpoint = "".join(
            [
                f"/users/{user_id}",
                f"/interactions/{interaction_type.value}",
                f"/category/{category}",
                f"/keyword/{keyword}",
            ]
        )
        return self._rumo_client.delete(endpoint)

    def get_interactions(
        self,
        user_id: str,
        interaction_type: Optional[InteractionType] = None,
        target_type: Optional[TargetType] = None,
        content_id: Optional[str] = None,
        skip: Optional[int] = 0,
        limit: Optional[int] = 10,
    ) -> dict:
        endpoint = f"/users/{user_id}/interactions"
        params = {
            "type": interaction_type.value if interaction_type is not None else None,
            "contentId": content_id,
            "targetType": target_type.value if target_type is not None else None,
            "skip": skip,
            "limit": limit,
        }
        return self._rumo_client.get(endpoint, query_params=params)

    for interaction_type in InteractionType:
        exec(
            """def {name}(self, user_id: str, content_id: str) -> dict:
                    return self._post_interaction(
                        user_id,
                        {interaction_type},
                        content_id)
            """.format(
                name=interaction_type.value, interaction_type=interaction_type
            )
        )
