from abc import ABC, abstractmethod
class IPayrollService(ABC):
    @abstractmethod
    def generate_payroll(self, employee_id, start_date, end_date):
        pass
    @abstractmethod
    def get_payroll_by_id(self, payroll_id):
        pass
    @abstractmethod
    def get_payrolls_for_employee(self, employee_id):
        pass
    @abstractmethod
    def get_payrolls_for_period(self, start_date, end_date):
        pass
class PayrollService():
    def __init__(self, conn):
        self.conn = conn

    def generate_payroll(self, payroll):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO Payroll (PayrollID, EmployeeID, PayPeriodStartDate, PayPeriodEndDate, BasicSalary, OvertimePay, Deductions, NetSalary)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (payroll.get_payrollID(), payroll.get_employeeID(), payroll.get_payPeriodStartDate(), payroll.get_payPeriodEndDate(),
              payroll.get_basicSalary(), payroll.get_overtimePay(), payroll.get_deductions(), payroll.get_netSalary()))
        self.conn.commit()

    def get_payroll_id(self, payroll_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Payroll WHERE PayrollID = %s", (payroll_id,))
        return cursor.fetchone()

    def get_payrolls_for_employee(self, employee_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Payroll WHERE EmployeeID = %s", (employee_id,))
        return cursor.fetchall()

    def get_payrolls_for_period(self, start_date, end_date):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Payroll WHERE PayPeriodStartDate >= %s AND PayPeriodEndDate <= %s", (start_date, end_date))
        return cursor.fetchall()