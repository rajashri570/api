from enum import Enum
class ResponseEnum(Enum):
    Success = 1
    Failed = 2

class Response:
    def __init__(self, status, message=None,data=None):
        self.status = status
        self.message = message
        self.data = data

    def __str__(self):
        return f"Status: {self.status.name}, Message: {self.message}"
    