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
    report: UploadReport = UploadReport.build_report(catalog, responses_with_errors)
    assert report.processed_content == expected_report.processed_content
    assert report.invalid_content == expected_report.invalid_content
    assert report.validation_errors == expected_report.validation_errors


def test_build_report_when_no_errors():
    expected_report = UploadReport({"1", "2", "3", "4"}, set(), [])
    report: UploadReport = UploadReport.build_report(catalog, responses_without_errors)
    assert report.processed_content == expected_report.processed_content
    assert report.invalid_content == expected_report.invalid_content
    assert report.validation_errors == expected_report.validation_errors


def test_build_report_when_subcontents_error():
    expected_validation_errors = [
        ValidationError(
            "ERROR_0204",
            "Content not Found: contentId does not exist.",
            "1",
            "RequestBodyValidation",
        ),
        ValidationError(
            "ERROR_0204",
            "Content not Found: contentId does not exist.",
            "2",
            "RequestBodyValidation",
        ),
    ]
    expected_report = UploadReport(set(), set(), expected_validation_errors)
    report: UploadReport = UploadReport.build_report(
        sub_contents, sub_content_responses
    )
    assert report.processed_content == expected_report.processed_content
    assert report.invalid_content == expected_report.invalid_content
    assert report.validation_errors == expected_report.validation_errors


def test_validation_error_eq():
    err1 = ValidationError(
        "ERROR_0204",
        "Content not Found: contentId does not exist.",
        "2",
        "RequestBodyValidation",
    )
    err2 = ValidationError(
        "ERROR_0204",
        "Content not Found: contentId does not exist.",
        "2",
        "RequestBodyValidation",
    )
    assert err1.__eq__(err2).__eq__(True)


sub_content_responses = [
    {
        "message": (
            "Request processed successfully, some content items were invalid and not"
            " processed"
        ),
        "validationErrors": [
            {
                "errorCode": "ERROR_0204",
                "message": "Content not Found: contentId does not exist.",
                "value": "1",
                "errorType": "RequestBodyValidation",
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
                "message": "Content not Found: contentId does not exist.",
                "value": "2",
                "errorType": "RequestBodyValidation",
            }
        ],
    },
]

responses_with_errors = [
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

responses_without_errors = [
    {
        "message": "Request processed successfully.",
        "validationErrors": [],
    },
    {
        "message": "Request processed successfully.",
        "validationErrors": [],
    },
]

catalog = [
    {"id": "1", "label": "label_1"},
    {"id": "2", "label": "label_2"},
    {"id": "3", "label": "label_3"},
    {"id": "4", "label": "label_4"},
]

sub_contents = [
    {"contentId": "1", "subContentIds": ["4", "5"]},
    {"contentId": "2", "subContentIds": ["6", "7"]},
]
