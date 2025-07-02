from abc import ABC, abstractmethod
class ITaxService(ABC):
    @abstractmethod
    def calculateTax(self, employeeId, taxYear):
        pass
    def GetTaxById(self, taxId):
        pass
    def GetTaxesForEmployee(self, employeeId):
        pass
    def GetTaxesForYear(self, taxYear):
        pass

class TaxService():
    def __init__(self, conn):
        self.conn = conn

    def calculate_tax(self, tax):
        cursor = self.conn.cursor()

        # 20% flat tax calculation
        calculated_tax = tax.get_taxableincome() * 0.20
        tax.set_taxamount(calculated_tax)

        cursor.execute("""
                       INSERT INTO Tax (TaxID, EmployeeID, TaxYear, TaxableIncome, TaxAmount)
                       VALUES (%s, %s, %s, %s, %s)
                       """, (
                           tax.get_taxid(), tax.get_employeeid(), tax.get_taxyear(),
                           tax.get_taxableincome(), tax.get_taxamount()
                       ))
        self.conn.commit()


    def get_tax_by_id(self, tax_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Tax WHERE TaxID = %s", (tax_id,))
        return cursor.fetchone()

    def get_taxes_for_employee(self, employee_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Tax WHERE EmployeeID = %s", (employee_id,))
        return cursor.fetchall()

    def get_taxes_for_year(self, tax_year):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Tax WHERE TaxYear = %s", (tax_year,))
        return cursor.fetchall()