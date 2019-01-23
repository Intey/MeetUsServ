class OperationException(BaseException):
    def __init__(self, message, *args, **kwargs):
        BaseException.__init__(self, *args, **kwargs)
        self.message = message

    def __str__(self):
        return self.message

    def __repr__(self):
        return f"OperationException: {self.message}"
