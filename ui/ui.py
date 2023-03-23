from repository.lab_repo import LabRepository
from random import seed
from random import randint
import random, string
from domain.entities import Lab
class LabUI:
    def __init__(self, c):
        self.__c=c
    def __showStudentLabs(self):
        studentid=input("Id-ul studentului este:")
        all_l=self.__c.getLabsByStudentid(int(studentid))
        for l in all_l:
            print("Id-ul studentului: " +str(l.getstudentid())+ " Numarul lab-ului: "+ str(l.getlabNumber())+" Numarul problemei: "+l.getproblemNumber()+'\n')
    def __addStudentLab(self):
        #try:
            studentid = input('Introduceti id_ul studentului:')
            labNumber=input('Introduceti numarul laboratorului:')
            problemNumber = input('Introduceti numarul problemei:')
            self.__c.addLab(int(studentid),int(labNumber), problemNumber)
        #except:
           # all_l=self.__c_lab.getLabsByStudentid(studentid)
            #for l in all_l:
                #if l.getlabNumber()==labNumber:
    def __searchstudent(self):
        studentid=input("Id-ul studentului:")
        stud=self.__c.getStudentByid(studentid)
        print("ID: "+str(stud.getId())+" Nume: "+str(stud.getNume()))
    def __List_of_students(self):
        all=self.__c.get_all()
        for s in all:
            print("ID: "+str(s.getId())+" Nume: "+str(s.getNume())+'\n')
    def __amestec(self):
        number=input("Numar: ")
        all=self.__c.getLabsByNumber(int(number))
        for p in all:
            print("ID: "+str(p.getstudentid())+" Nume: "+self.__c.getStudentByid(p.getstudentid()).getNume()+ " Numarul lab-ului: "+ str(p.getlabNumber())+" Numarul problemei: "+p.getproblemNumber()+'\n')
    def __deletebyid(self):
        id=input("ID: ")
        s=self.__c.deleted(int(id))
        print(s)
        #for s in all:
        #print("Id-ul studentului: " +str(s.getstudentid())+ " Numarul lab-ului: "+ str(s.getlabNumber())+" Numarul problemei: "+s.getproblemNumber()+'\n')
    def __undo_ui(self):
        self.__c.undo_c()


    def run(self):
        while True:
            cmd = input('Comanda este:')
            cmd = cmd.lower().strip()
            if cmd == 'lista_stud':
                self.__List_of_students()
            if cmd == 'caut_stud':
                self.__searchstudent()
            if cmd == 'add':
                self.__addStudentLab()
            if cmd=='toate':
                self.__showStudentLabs()
            if cmd == 'numar':
                self.__amestec()
            if cmd == 'sterge':
                self.__deletebyid()
            if cmd == 'undo':
                self.__undo_ui()







class LabController:
    def __init__(self, repo_stud, repo_lab):
        self.__repo_stud=repo_stud
        self.__repo_lab = repo_lab
    def addLab(self,studentid,labNumber,problemNumber):
        l=Lab(studentid,labNumber,problemNumber)
        self.__repo_lab.add(l)
    def getStudentByid(self,studentid):
        return self.__repo_stud.findByid(studentid)
    def getLabsByStudentid(self,studentid):
        labs=[]
        lb=self.__repo_lab.all_labs()
        for l in lb:
            if l.getstudentid()==studentid:
                labs.append(l)
        return labs
    def getLabsByNumber(self,number):
        labs=[]
        lb=self.__repo_lab.all_labs()
        for l in lb:
            if l.getlabNumber()==number:
                labs.append(l)
        return labs
    def get_all(self):
        return self.__repo_stud.all_stud()
    def deleted(self, id):
        return self.__repo_lab.delete(id)
    def undo_c(self):
        self.__repo_lab.undo()

    def __load_from_file(self):
        try:
            f = open(self.__filename, 'r')
        except IOError:
            return
        lines = f.readlines()
        all_labs = []
        for line in lines:
            studentid, labNumber, problemNumber = [token.strip() for token in line.split(';')]
            l = Lab(int(studentid), int(labNumber), problemNumber)
            all_labs.append(l)
        f.close()
        return all_labs

    def __save_to_file(self, all_l):
        with open(self.__filename, 'w') as f:
            for l in all_l:
                l_string = str(l.getstudentid()) + ';' + str(l.getlabNumber()) + ';' + str(l.getproblemNumber()) + '\n'
                f.write(l_string)
    def __load_from_file(self):
        try:
            f = open(self.__filename, 'r')
        except IOError:
            return
        lines = f.readlines()
        all_labs = []
        for line in lines:
            studentid, labNumber, problemNumber = [token.strip() for token in line.split(';')]
            l = Lab(int(studentid), int(labNumber), problemNumber)
            all_labs.append(l)
        f.close()
        return all_labs

    def __save_to_file(self, all_l):
        with open(self.__filename, 'w') as f:
            for l in all_l:
                l_string = str(l.getstudentid()) + ';' + str(l.getlabNumber()) + ';' + str(l.getproblemNumber()) + '\n'
                f.write(l_string)








