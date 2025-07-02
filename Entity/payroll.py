class payroll:
    def __init__(self,payrollID,employeeID, payPeriodStartDate, payPeriodEndDate,basicSalary,overtimePay,deductions,netSalary):
        if not payrollID or payrollID.strip() == "":
            raise ValueError("Payroll ID is required.")
        if basicSalary < 0:
            raise ValueError("Salary must be non-negative.")

        self.__payrollID=payrollID
        self.__employeeID=employeeID
        self.__payPeriodStartDate=payPeriodStartDate
        self.__payPeriodEndDate=payPeriodEndDate
        self.__basicSalary=basicSalary
        self.__overtimePay=overtimePay
        self.__deductions=deductions
        self.__netSalary=netSalary
    def get_payrollID(self):
        return self.__payrollID
    def set_payrollID(self,payrollID):
        self.__payrollID=payrollID
    def get_employeeID(self):
        return self.__employeeID
    def set_employeeID(self,employeeID):
        self.__employeeID=employeeID
    def get_payPeriodStartDate(self):
        return self.__payPeriodStartDate
    def set_payPeriodStartDate(self,payPeriodStartDate):
        self.__payPeriodStartDate=payPeriodStartDate
    def get_payPeriodEndDate(self):
        return self.__payPeriodEndDate
    def set_payPeriodEndDate(self,payPeriodEndDate):
        self.__payPeriodEndDate=payPeriodEndDate
    def get_basicSalary(self):
        return self.__basicSalary
    def set_basicSalary(self,basicSalary):
        self.__basicSalary=basicSalary
    def get_overtimePay(self):
        return self.__overtimePay
    def set_overtimePay(self,overtimePay):
        self.__overtimePay=overtimePay
    def get_deductions(self):
        return self.__deductions
    def set_deductions(self,deductions):
        self.__deductions=deductions
    def get_netSalary(self):
        return self.__netSalary
    def set_netSalary(self,netSalary):
        self.__netSalary=netSalary




