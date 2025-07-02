class ValidationService:
    def __init__(self):
        pass

    def validate_required(self, value, field_name):
        if value is None or (isinstance(value, str) and value.strip() == ""):
            raise ValueError(f"{field_name} is required.")

    def validate_positive_number(self, value, field_name):
        if value is None or value < 0:
            raise ValueError(f"{field_name} must be a positive number.")

    def validate_date_order(self, start_date, end_date):
        if start_date > end_date:
            raise ValueError("Start date must be before end date.")
