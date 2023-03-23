from domain.entities import Student
class StudentRepository:
    def __init__(self,filename):
        self.__filename=filename
    def size(self):
        return len(self.__load_from_file())
    def __load_from_file(self):
        try:
            f=open(self.__filename,'r')
        except IOError:
            return
        lines=f.readlines()
        all_students=[]
        for line in lines:
            id, nume=[token.strip() for token in line.split(';')]
            s=Student(int(id),nume)
            all_students.append(s)
        f.close()
        return all_students
    def __save_to_file(self):
        all_s=self.all_stud()
        with open(self.__filename,'w') as f:
            for s in all_s:
                s_string=str(s.getId())+';'+str(s.getNume())+'\n'
                f.write(s_string)
    def findByid(self,id):
        all_stud=self.__load_from_file()
        for stud in all_stud:
            if stud.getId()==int(id):
                return stud
        return None
    def all_stud(self):
        return self.__load_from_file()


