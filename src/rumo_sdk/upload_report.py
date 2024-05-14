import re
from typing import Optional


class ValidationError:
    def __init__(self, errorCode: str, message: str, value: str, errorType: str):
        self.errorCode = errorCode
        self.message = message
        self.value = value
        self.errorType = errorType

    def to_dict(self):
        return {
            "errorCode": self.errorCode,
            "message": self.message,
            "value": self.value,
            "errorType": self.errorType
        }

    def __eq__(self, other):
        if isinstance(other, ValidationError):
            return (
                self.errorCode == other.errorCode
                and self.message == other.message
                and self.value == other.value
                and self.errorType == other.errorType
            )
        return False

    def parse_id_from_error_message(self) -> Optional[str]:
        matches = re.findall(r"\[(.*?)\]", self.message)
        if matches:
            return matches[0]
        else:
            None


class UploadReport:
    def __init__(
        self,
        processed_content: set[str],
        invalid_content: set[str],
        validation_errors: list[ValidationError],
    ):
        self.processed_content = processed_content
        self.invalid_content = invalid_content
        self.validation_errors = validation_errors

    def to_dict(self):
        return {
            "invalid_content": list(self.invalid_content),
            "validation_errors": [error.to_dict() for error in self.validation_errors]
        }

    @classmethod
    def build_report(
        cls, catalog: list[dict], upload_responses: list[dict]
    ) -> "UploadReport":
        processed_content = cls.get_processed_content_ids(catalog)
        validation_errors = cls.get_validation_errors(upload_responses)
        invalid_content = cls.get_invalid_content(validation_errors)
        return cls(processed_content, invalid_content, validation_errors)

    @staticmethod
    def get_processed_content_ids(catalog: list[dict]) -> set[str]:
        processed_content_ids: set[str] = set()
        for content in catalog:
            if "id" in content:
                processed_content_ids.add(content["id"])
        return processed_content_ids

    @classmethod
    def get_validation_errors(
        cls, upload_responses: list[dict]
    ) -> list[ValidationError]:
        validation_errors: list[ValidationError] = []
        for response in upload_responses:
            errors = cls.build_validation_errors(response)
            validation_errors.extend(errors)
        return validation_errors

    @staticmethod
    def build_validation_errors(response: dict) -> list[ValidationError]:
        validation_errors: list[ValidationError] = []
        if response["validationErrors"] and len(response["validationErrors"]) != 0:
            for error in response["validationErrors"]:
                errorCode = error["errorCode"]
                message = error["message"]
                value = error["value"]
                errorType = error["errorType"]
                validation_errors.append(
                    ValidationError(errorCode, message, value, errorType)
                )
        return validation_errors

    @staticmethod
    def get_invalid_content(validation_errors: list[ValidationError]) -> set[str]:
        invalid_content: set[str] = set()
        for error in validation_errors:
            content_id = error.parse_id_from_error_message()
            if content_id is not None:
                invalid_content.add(content_id)
        return invalid_content
