import unittest

from Dao.taxservices import TaxService
from Entity.tax import tax
from tests.test_payroll_service import carconn


class TestTaxService(unittest.TestCase):

    def setUp(self):
        self.conn = carconn()
        self.service = TaxService(self.conn)

    def test_tax_for_high_income(self):
        high_income = 2000000  # 20 lakh
        tax_obj = tax("T001", "E003", 2025, high_income)
        tax_amount = high_income * 0.10
        self.assertEqual(tax_obj.get_taxableincome() * 0.10, 200000.0)
