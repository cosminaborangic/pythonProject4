from repository.lab_repo import LabRepository
from repository.student_repo import StudentRepository
from ui.ui import LabUI,LabController

repo_file_stud = StudentRepository('data/student.txt')
repo_file_lab = LabRepository('data/labs.txt')
c = LabController(repo_file_stud,repo_file_lab)
ui=LabUI(c)
ui.run()

