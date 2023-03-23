from domain.entities import Lab
class LabRepository:
    def __init__(self,filename):
        self.__undo=[]
        self.__labs =[]
        self.__filename=filename
    def size(self):
        return len(self.__load_from_file())
    def __load_from_file(self):
        try:
            f=open(self.__filename,'r')
        except IOError:
            return
        lines=f.readlines()
        all_labs=[]
        for line in lines:
            studentid,labNumber, problemNumber=[token.strip() for token in line.split(';')]
            l=Lab(int(studentid), int(labNumber), problemNumber)
            all_labs.append(l)
        f.close()
        return all_labs
    def __save_to_file(self,all_l):
        with open(self.__filename,'w') as f:
            for l in all_l:
                l_string=str(l.getstudentid())+';'+str(l.getlabNumber())+';'+str(l.getproblemNumber())+'\n'
                f.write(l_string)
    def findByStudentid(self,studentid):
        all_labs=self.__load_from_file()
        for lab in all_labs:
            if lab.getstudentid()==studentid:
                return lab
        return None
    def __load_from_file(self):
        try:
            f=open(self.__filename,'r')
        except IOError:
            return
        lines=f.readlines()
        all_labs=[]
        for line in lines:
            studentid,labNumber, problemNumber=[token.strip() for token in line.split(';')]
            l=Lab(int(studentid), int(labNumber), problemNumber)
            all_labs.append(l)
        f.close()
        return all_labs
    def __save_to_file(self,all_l):
        with open(self.__filename,'w') as f:
            for l in all_l:
                l_string=str(l.getstudentid())+';'+str(l.getlabNumber())+';'+str(l.getproblemNumber())+'\n'
                f.write(l_string)
    def add(self,lab):
        self.__undo=self.__load_from_file()
        self.__labs.append(lab)
        self.__save_to_file(self.all_lab())
    def all_lab(self):
        toate=self.__load_from_file()
        for d in toate:
            self.__labs.append(d)
        return self.__labs
    def all_labs(self):
        return self.__load_from_file()
    def __find_index(self,all, id):
        index=[]
        for d in range(len(all)):
            if all[d].getstudentid()==id:
                index.append(d)
        return index
    def delete(self,id):
        self.__undo= self.__load_from_file()
        all=self.__load_from_file()
        for l in all:
            if l.getstudentid() == id:
                all.remove(l)
        self.__save_to_file(all)

        return all
    def undo(self):
        self.__save_to_file(self.__undo)


