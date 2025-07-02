from datetime import date
class Employees:
    def __init__(self,employeeID,firstName, lastName, birthDate, gender, email, phoneNumber, address, position, joiningDate):
        if not employeeID or employeeID.strip() == "":
            raise ValueError("Employee ID is required.")
        if not firstName or firstName.strip() == "":
            raise ValueError("Employee name is required.")

        self.__employeeID = employeeID
        self.__firstName = firstName
        self.__lastName = lastName
        self.__birthDate = birthDate
        self.__gender = gender
        self.__email = email
        self.__phoneNumber = phoneNumber
        self.__address = address
        self.__position = position
        self.__joiningDate = joiningDate

    def calculate_age(self):
        from datetime import date
        return date.today().year - self.__dob.year

    def get_employee_id(self):
        return self.__employeeID
    def set_employeeID(self,employeeID):
        self.__employeeID = employeeID
    def get_firstName(self):
        return self.__firstName
    def set_firstName(self,firstName):
        self.__firstName = firstName
    def get_lastName(self):
        return self.__lastName
    def set_lastName(self,lastName):
        self.__lastName = lastName
    def get_birthDate(self):
        return self.__birthDate
    def set_birthDate(self,birthDate):
        self.__birthDate = birthDate
    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        self.__gender = gender
    def get_email(self):
        return self.__email
    def set_email(self,email):
        self.__email = email
    def get_phoneNumber(self):
        return self.__phoneNumber
    def set_phoneNumber(self,phoneNumber):
        self.__phoneNumber = phoneNumber
    def get_address(self):
        return self.__address
    def set_address(self,address):
        self.__address = address
    def get_position(self):
        return self.__position
    def set_position(self,position):
        self.__position = position
    def get_joiningDate(self):
        return self.__joiningDate
    def set_joiningDate(self,joiningDate):
        self.__joiningDate = joiningDate








