class FinancialRecord:
    def __init__(self, RecordID, EmployeeID, RecordDate, Description, Amount, RecordType):
        self.RecordID = RecordID
        self.EmployeeID = EmployeeID
        self.RecordDate = RecordDate
        self.Description = Description
        self.Amount = Amount
        self.RecordType = RecordType
    def get_recordID(self):
        return self.RecordID
    def set_recordID(self,recordID):
        self.RecordID = recordID
    def get_employeeID(self):
        return self.EmployeeID
    def set_employeeID(self,employeeID):
        self.EmployeeID = employeeID
    def get_recordDate(self):
        return self.RecordDate
    def set_recordDate(self,recordDate):
        self.RecordDate = recordDate
    def get_description(self):
        return self.Description
    def set_description(self,description):
        self.Description = description
    def get_amount(self):
        return self.Amount
    def set_amount(self,amount):
        self.Amount = amount
    def get_record_type(self):
        return self.RecordType
    def set_record_type(self,record_type):
        self.RecordType = record_type

