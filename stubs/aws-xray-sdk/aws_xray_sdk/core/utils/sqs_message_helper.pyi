SQS_XRAY_HEADER: str

class SqsMessageHelper:
    @staticmethod
    def isSampled(sqs_message: dict) -> bool: ...
