import unittest
from Entity.payroll import payroll
from Dao.payrollservices import PayrollService

class carconn:
    def cursor(self):
        return self
    def execute(self, q, p):
        self.last_query = q
        self.last_params = p
    def commit(self):
        pass
    def rollback(self):
        pass

class TestPayrollService(unittest.TestCase):

    def setUp(self):
        self.conn = carconn()
        self.service = PayrollService(self.conn)

    def test_calculate_gross_salary(self):
        p = payroll("P001", "E001", "2025-06-01", "2025-06-30", 50000, 5000, 0, 55000)
        self.assertEqual(p.get_basicSalary() + p.get_overtimePay(), 55000)

    def test_calculate_net_salary_after_deductions(self):
        p = payroll("P002", "E002", "2025-06-01", "2025-06-30", 50000, 5000, 5000, 50000)
        net = p.get_basicSalary() + p.get_overtimePay() - p.get_deductions()
        self.assertEqual(net, p.get_netSalary())


