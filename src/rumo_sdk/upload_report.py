import re


class ValidationError:
    def __init__(self, errorCode: str, message: str, value: str, errorType: str):
        self.errorCode = errorCode
        self.message = message
        self.value = value
        self.errorType = errorType


class UploadReport:
    def __init__(
        self,
        processed_content: list[str],
        invalid_content: list[str],
        validation_errors: list[ValidationError],
    ):
        self.processed_content = processed_content
        self.invalid_content = invalid_content
        self.validation_errors = validation_errors

    @classmethod
    def build_report(cls, catalog, upload_responses):
        processed_content = cls.get_processed_content_ids(catalog)
        validation_errors = cls.get_validation_errors(cls, upload_responses)
        invalid_content = cls.get_invalid_content(cls, validation_errors)
        return cls.__init__(cls, processed_content, invalid_content, validation_errors)

    def get_processed_content_ids(catalog) -> list[str]:
        processed_content_ids = []
        for content in catalog:
            if content["id"]:
                processed_content_ids.append(content["id"])
        return processed_content_ids

    def get_validation_errors(cls, upload_responses) -> list[ValidationError]:
        validation_errors = []
        for response in upload_responses:
            cls.build_validation_errors(response, validation_errors)
        return validation_errors

    def build_validation_errors(response, validation_errors) -> ValidationError:
        if response["validationErrors"] and len(response["validationErrors"]) != 0:
            for error in response["validationErrors"]:
                errorCode = error["errorCode"]
                message = error["message"]
                value = error["value"]
                errorType = error["errorType"]
                validation_errors.append(
                    ValidationError(errorCode, message, value, errorType)
                )

    def get_invalid_content(cls, validation_errors: list[ValidationError]) -> list[str]:
        invalid_content = []
        for error in validation_errors:
            content_id = cls.parse_id_from_error_message(error.message)
            invalid_content.append(content_id)
        return invalid_content

    def parse_id_from_error_message(message: str) -> str:
        return re.findall(r"\[(\d+)\]", message)
