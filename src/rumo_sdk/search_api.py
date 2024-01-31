from typing import Optional

from rumo_sdk import api_client
from rumo_sdk.utils import FilterOperatorType, RumoFilters


class SearchApi:
    """https://apidoc.rumo.co/#post-/search/advanced"""

    def __init__(self, rumo_client: api_client.RumoClient):
        self._rumo_client = rumo_client

    def _advanced_search(
        self,
        search_parameter: dict,
        skip: Optional[int] = 0,
        limit: Optional[int] = 10,
        details: Optional[bool] = False,
        filters: Optional[RumoFilters.FilterType] = None,
        filter_operator: Optional[FilterOperatorType] = FilterOperatorType.OR,
    ) -> dict:
        endpoint = "/search/advanced"
        params = {"skip": skip, "limit": limit, "details": str(details).lower()}
        if filters is not None:
            rumo_filters = RumoFilters(filters, filter_operator)
            params.update(rumo_filters.format_filters_to_query_params())
        headers = {"Content-Type": "application/json"}
        return self._rumo_client.post(
            endpoint, header_params=headers, query_params=params, json=search_parameter
        )

    def search_by_keyword(self, keyword: str, **kwargs) -> dict:
        search_parameter = {
            "searchParameter": {
                "field": "categoriesFull.keyword",
                "comparator": "EQ",
                "value": keyword,
            }
        }
        return self._advanced_search(search_parameter, **kwargs)

    def search_by_keyword_in_category(
        self, keyword: str, category: str, **kwargs
    ) -> dict:
        search_parameter = {
            "searchParameter": {
                "field": f"categories.{category}.keyword",
                "comparator": "EQ",
                "value": keyword,
            }
        }
        return self._advanced_search(search_parameter, **kwargs)

    def search_label_exact(self, label: str, **kwargs) -> dict:
        search_parameter = {
            "searchParameter": {
                "field": "label",
                "comparator": "EQ",
                "value": label,
            }
        }
        return self._advanced_search(search_parameter, **kwargs)

    def search_label_contains(self, label: str, **kwargs) -> dict:
        search_parameter = {
            "searchParameter": {
                "field": "label.text",
                "comparator": "CONTAINS",
                "value": label,
            }
        }
        return self._advanced_search(search_parameter, **kwargs)

    def search_label_fuzzy(self, label: str, **kwargs) -> dict:
        search_parameter = {
            "searchParameter": {
                "field": "label.text",
                "comparator": "LIKE",
                "value": label,
            }
        }
        return self._advanced_search(search_parameter, **kwargs)
