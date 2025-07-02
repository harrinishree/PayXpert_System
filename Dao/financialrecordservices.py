from abc import ABC, abstractmethod
class IFinancialRecord(ABC):
    @abstractmethod
    def GetFinancialRecordById(self,employeeId,amount,recordType):
        pass
    def GetFinancialRecordsForEmployee(self,employeeId):
        pass
    def GetFinancialRecordsForDate(self,recordDate):
        pass
    def GetFinancialRecordsByDate(self,recordDate):
        pass

class FinancialRecordService():
    def __init__(self, conn):
        self.conn = conn

    def add_financial_record(self, record):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO FinancialRecord (RecordID, EmployeeID, RecordDate, Description, Amount, RecordType)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (record.get_recordID(), record.get_employeeID(), record.get_recordDate(), record.get_description(), record.get_amount(), record.get_record_type()))
        self.conn.commit()

    def get_financial_record_by_id(self, record_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM FinancialRecord WHERE RecordID = %s", (record_id,))
        return cursor.fetchone()

    def get_financial_records_for_employee(self, employee_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM FinancialRecord WHERE EmployeeID = %s", (employee_id,))
        return cursor.fetchall()

    def get_financial_records_for_date(self, record_date):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM FinancialRecord WHERE RecordDate = %s", (record_date,))
        return cursor.fetchall()