class EmployeeNotFoundException(Exception):
    def __init__(self, message="Employee not found."):
        super().__init__(message)
