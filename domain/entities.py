class Student:
    def __init__(self, id, nume):
        self.__id=id
        self.__nume=nume
    def getId(self):
        return self.__id
    def getNume(self):
        return self.__nume
    def setId(self,value):
        self.__id=value
    def setNume(self,value):
        self.__nume=value
    def __eq__(self,other):
        if self.__id==other.getID(): #self.__id=other.__id
            return True
        return False
    def __str__(self):
        return "ID-ul studentului: "+str(self.getId())+" Numele studentului: "+self.getNume()

class Lab:
    def __init__(self,studentid, labNumber, problemNumber):
        self.__studentid=studentid
        self.__labNumber=labNumber
        self.__problemNumber = problemNumber
    def getstudentid(self):
        return self.__studentid
    def getlabNumber(self):
        return self.__labNumber
    def getproblemNumber(self):
        return self.__problemNumber
    def setstudentid(self,value):
        self.__studentid=value
    def setlabNumber(self,value):
        self.__labNumber=value
    def setproblemNumber(self,value):
        self.__problemNumber=value
    def __eq__(self, other):
        if self.__studentid==other.__studentid:
            return True
        return False
    def __str__(self):
        return "ID-ul studentului: "+str(self.getstudentid())+" Numarul laboratorului: "+str(self.getlabNumber())+" Numarul problemei: "+self.getproblemNumber()

