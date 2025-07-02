class FinancialRecordException(Exception):
    def __init__(self, message="Financial record operation failed."):
        super().__init__(message)
