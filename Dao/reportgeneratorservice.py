class ReportGenerator:
    def __init__(self, conn):
        self.conn = conn

    def generate_income_report_by_employee(self, employee_id):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT e.EmployeeID, e.FirstName, e.LastName,
                   p.PayPeriodStartDate, p.PayPeriodEndDate,
                   p.BasicSalary, p.OvertimePay, p.Deductions, p.NetSalary
            FROM Payroll p
            JOIN Employee e ON p.EmployeeID = e.EmployeeID
            WHERE e.EmployeeID = %s
            ORDER BY p.PayPeriodEndDate DESC
        """, (employee_id,))
        return cursor.fetchall()

    def generate_tax_report_by_employee(self, employee_id):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT e.EmployeeID, e.FirstName, e.LastName,
                   t.TaxYear, t.TaxableIncome, t.TaxAmount
            FROM Tax t
            JOIN Employee e ON t.EmployeeID = e.EmployeeID
            WHERE e.EmployeeID = %s
            ORDER BY t.TaxYear DESC
        """, (employee_id,))
        return cursor.fetchall()

    def generate_financial_record_by_employee(self, employee_id):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT e.EmployeeID, e.FirstName, e.LastName,
                   f.RecordDate, f.Description, f.Amount, f.RecordType
            FROM FinancialRecord f
            JOIN Employee e ON f.EmployeeID = e.EmployeeID
            WHERE e.EmployeeID = %s
            ORDER BY f.RecordDate DESC
        """, (employee_id,))
        return cursor.fetchall()
