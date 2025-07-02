import unittest
import datetime
from Entity.employees import Employees

class TestInvalidEmployeeData(unittest.TestCase):

    def setUp(self):
        self.valid_data = {
            "employee_id": "E001",
            "first_name": "John",
            "last_name": "Doe",
            "dob": datetime.date(1990, 1, 1),
            "gender": "M",
            "email": "john@example.com",
            "phone": "9999999999",
            "address": "123 Street",
            "position": "Manager",
            "joining_date": datetime.date(2022, 1, 1),
            "termination_date": None
        }

    def test_missing_first_name_should_raise(self):
        data = self.valid_data.copy()
        data["first_name"] = ""
        with self.assertRaises(ValueError) as context:
            Employees(**data)
        self.assertIn("Employee name is required", str(context.exception))

    def test_missing_employee_id_should_raise(self):
        data = self.valid_data.copy()
        data["employee_id"] = ""
        with self.assertRaises(ValueError) as context:
            Employees(**data)
        self.assertIn("Employee ID is required", str(context.exception))

    def test_valid_employee_should_not_raise(self):
        try:
            emp = Employees(**self.valid_data)
        except Exception:
            self.fail("Valid employee creation should not raise exception.")

if __name__ == "__main__":
    unittest.main()
