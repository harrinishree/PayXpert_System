class PayrollGenerationException(Exception):
    def __init__(self, message="Payroll generation failed."):
        super().__init__(message)
