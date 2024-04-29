from rumo_sdk.upload_report import UploadReport, ValidationError


def test_build_report():
    expected_validation_errors = [
        ValidationError(
            "ERROR_0204",
            "Invalid JSON content: [1] Availability's 'start' value must be lower than"
            " 'end' value.",
            "1,1",
            "BadRequest",
        ),
        ValidationError(
            "ERROR_0204",
            "Invalid JSON content: [2] [ videogame] Keywords must not contain the"
            " characters '$' or '.', must not be longer than 128 characters and must"
            " not start or end with a whitespace",
            " videogame",
            "BadRequest",
        ),
        ValidationError(
            "ERROR_0204",
            "Invalid JSON content: [3] [ videogame] Keywords must not contain the"
            " characters '$' or '.', must not be longer than 128 characters and must"
            " not start or end with a whitespace",
            " videogame",
            "BadRequest",
        ),
        ValidationError(
            "ERROR_0204",
            "Invalid JSON content: [3] Availability's 'start' value must be lower than"
            " 'end' value.",
            "1,1",
            "BadRequest",
        ),
    ]
    expected_report = UploadReport(
        {"1", "2", "3", "4"}, {"1", "2", "3"}, expected_validation_errors
    )
    report: UploadReport = UploadReport.build_report(catalog, responses)
    assert report.processed_content == expected_report.processed_content
    assert report.invalid_content == expected_report.invalid_content
    assert report.validation_errors == expected_report.validation_errors


responses = [
    {
        "message": (
            "Request processed successfully, some content items were invalid and not"
            " processed"
        ),
        "validationErrors": [
            {
                "errorCode": "ERROR_0204",
                "message": (
                    "Invalid JSON content: [1] Availability's 'start' value must be"
                    " lower than 'end' value."
                ),
                "value": "1,1",
                "errorType": "BadRequest",
            },
            {
                "errorCode": "ERROR_0204",
                "message": (
                    "Invalid JSON content: [2] [ videogame] Keywords must not contain"
                    " the characters '$' or '.', must not be longer than 128 characters"
                    " and must not start or end with a whitespace"
                ),
                "value": " videogame",
                "errorType": "BadRequest",
            },
        ],
    },
    {
        "message": (
            "Request processed successfully, some content items were invalid and not"
            " processed"
        ),
        "validationErrors": [
            {
                "errorCode": "ERROR_0204",
                "message": (
                    "Invalid JSON content: [3] [ videogame] Keywords must not contain"
                    " the characters '$' or '.', must not be longer than 128 characters"
                    " and must not start or end with a whitespace"
                ),
                "value": " videogame",
                "errorType": "BadRequest",
            },
            {
                "errorCode": "ERROR_0204",
                "message": (
                    "Invalid JSON content: [3] Availability's 'start' value must be"
                    " lower than 'end' value."
                ),
                "value": "1,1",
                "errorType": "BadRequest",
            },
        ],
    },
]

catalog = [
    {"id": "1", "label": "label_1"},
    {"id": "2", "label": "label_2"},
    {"id": "3", "label": "label_3"},
    {"id": "4", "label": "label_4"},
]
