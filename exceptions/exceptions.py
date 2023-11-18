

class InvalidModelTypeException(Exception):
    def __init__(self, message="Invalid model type specified"):
        super().__init__(message)


class EmptyResponseException(Exception):
    def __init__(self, message="Received an empty response"):
        super().__init__(message)