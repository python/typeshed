from typing import Any

SQS_XRAY_HEADER: str

class SqsMessageHelper:
    @staticmethod
    def isSampled(sqs_message: dict[Any, Any]) -> bool: ...
