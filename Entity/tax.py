class tax:
    def __init__(self,taxid,employeeid,taxyear,taxableincome,taxamount=None):
        self.__taxid = taxid
        self.__employeeid = employeeid
        self.__taxyear = taxyear
        self.__taxableincome = taxableincome
        self.__taxamount = taxamount
    def get_taxid(self):
        return self.__taxid
    def set_taxid(self,taxid):
        self.__taxid = taxid
    def get_employeeid(self):
        return self.__employeeid
    def set_employeeid(self,employeeid):
        self.__employeeid = employeeid
    def get_taxyear(self):
        return self.__taxyear
    def set_taxyear(self, taxyear):
        self.__taxyear = taxyear
    def get_taxableincome(self):
        return self.__taxableincome
    def set_taxableincome(self,taxableincome):
        self.__taxableincome = taxableincome
    def get_taxamount(self):
        return self.__taxamount
    def set_taxamount(self,taxamount):
        self.__taxamount = taxamount

