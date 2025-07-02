from Exception.employeenotfoundexception import EmployeeNotFoundException
from abc import ABC, abstractmethod
class IEmployeeService(ABC):
    @abstractmethod
    def GetEmployeeById(self,employeeId):
        pass
    @abstractmethod
    def GetAllEmployees(self):
        pass
    @abstractmethod
    def AddEmployee(self,employeeData):
        pass
    @abstractmethod
    def UpdateEmployee(self,employeeData):
        pass
    @abstractmethod
    def RemoveEmployee(self,employeeId):
        pass

class EmployeeService:
    def __init__(self, conn):
        self.conn = conn

    def get_employee_by_id(self, employee_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Employee WHERE EmployeeID = %s", (employee_id,))
        result = cursor.fetchone()

        if not result:
            raise EmployeeNotFoundException(f"Invalid Employee ID: {employee_id}")

        return result

    def get_all_employees(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Employee")
        return cursor.fetchall()

    def add_employee(self, employee):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO Employee (EmployeeID, FirstName, LastName, DateOfBirth, Gender, Email, PhoneNumber, Address, Position, JoiningDate)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            employee.get_employee_id(), employee.get_firstName(), employee.get_lastName(),
            employee.get_birthDate(), employee.get_gender(), employee.get_email(),
            employee.get_phoneNumber(), employee.get_address(), employee.get_position(),
            employee.get_joiningDate()
        ))
        self.conn.commit()

    def update_employee(self, employee):
        cursor = self.conn.cursor()
        cursor.execute("""
                       UPDATE Employee
                       SET FirstName=%s,
                           LastName=%s,
                           DateOfBirth=%s,
                           Gender=%s,
                           Email=%s,
                           PhoneNumber=%s,
                           Address=%s,
                           Position=%s,
                           JoiningDate=%s
                       WHERE EmployeeID = %s
                       """, (
                           employee.get_firstName(), employee.get_lastName(),
                           employee.get_birthDate(), employee.get_gender(), employee.get_email(),
                           employee.get_phoneNumber(), employee.get_address(), employee.get_position(),
                           employee.get_joiningDate(), employee.get_employee_id()
                       ))
        self.conn.commit()

    def remove_employee(self, employee_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Employee WHERE EmployeeID = %s", (employee_id,))
        result = cursor.fetchone()
        if not result:
            raise EmployeeNotFoundException(f"Invalid Employee ID: {employee_id}")


        cursor.execute("DELETE FROM Employee WHERE EmployeeID = %s", (employee_id,))
        self.conn.commit()




