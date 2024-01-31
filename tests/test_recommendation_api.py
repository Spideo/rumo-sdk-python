from rumo_sdk.recommendation_api import RecommendationApi


def test_similar(api_mock):
    reco_api = RecommendationApi(api_mock)
    reco_api.get_similar("content_id")
    api_mock.call_api.assert_called_once_with(
        "GET", "/content/content_id/similar", query_params={"algo": "cosine"}
    )


def test_similar_with_filters(api_mock):
    reco_api = RecommendationApi(api_mock)
    filters = {"f_a": ["v_a", "v_b"], "f_b": ["v_c"]}
    reco_api.get_similar("content_id", filters=filters)
    api_mock.call_api.assert_called_once_with(
        "GET",
        "/content/content_id/similar",
        query_params={
            "algo": "cosine",
            "filters": ["f_a:v_a,v_b", "f_b:v_c"],
            "filterOperator": "OR",
        },
    )


def test_explain(api_mock):
    reco_api = RecommendationApi(api_mock)
    reco_api.explain_similar("content_a", "content_b")
    api_mock.call_api.assert_called_once_with(
        "GET", "/content/content_a/similar/content_b/explain"
    )


def test_user_reco(api_mock):
    reco_api = RecommendationApi(api_mock)
    reco_api.get_user_recommendation("user_id")
    api_mock.call_api.assert_called_once_with(
        "GET", "/users/user_id/recommendation", query_params={"algo": "cosine"}
    )


def test_user_reco_with_filters(api_mock):
    reco_api = RecommendationApi(api_mock)
    filters = {"f_a": ["v_a", "v_b"], "f_b": ["v_c"]}
    reco_api.get_user_recommendation("user_id", filters=filters)
    api_mock.call_api.assert_called_once_with(
        "GET",
        "/users/user_id/recommendation",
        query_params={
            "algo": "cosine",
            "filters": ["f_a:v_a,v_b", "f_b:v_c"],
            "filterOperator": "OR",
        },
    )


def test_user_profile(api_mock):
    reco_api = RecommendationApi(api_mock)
    reco_api.get_user_profile("user_id")
    api_mock.call_api.assert_called_once_with(
        "GET", "/users/user_id/recommendation/profile"
    )
