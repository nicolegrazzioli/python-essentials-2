"""
Prof. Jekyll conducts classes with students and regularly makes notes in a text file. Each line of the file contains three elements: the student's first name, the student's last name, and the number of points the student received during certain classes.

The elements are separated with white spaces. Each student may appear more than once inside Prof. Jekyll's file.

The file may look as follows:

John     Smith    5
Anna     Boleyn   4.5
John     Smith    2
Anna     Boleyn   11
Andrew   Cox      1.5
samplefile.txt
Your task is to write a program which:

asks the user for Prof. Jekyll's file name;
reads the file contents and counts the sum of the received points for each student;
prints a simple (but sorted) report, just like this one:
Output
Andrew   Cox      1.5
Anna     Boleyn   15.5
John     Smith    7.0

Note:

your program must be fully protected against all possible failures: the file's non-existence, the file's emptiness, or any input data failures; encountering any data error should cause immediate program termination, and the error should be presented to the user;
implement and use your own exceptions hierarchy – we've presented it in the editor; the second exception should be raised when a wrong line is detected, and the third when the source file exists but is empty.
Tip: Use a dictionary to store the students' data.
"""

from os import strerror

class StudentsDataException(Exception):
    def __init__(self, student='unknown', msg=''):
        Exception.__init__(self, msg)
        self.student = student

class BadLine(StudentsDataException):
    # linha errada detectada
    def __init__(self, student='unknown', badline='True', msg=''):
        StudentsDataException.__init__(self, student, msg)
        self.badline = badline

class FileEmpty(StudentsDataException):
    # arquivo existe mas eh vazio
    def __init__(self, student='unknown', fileempty='True', msg=''):
        StudentsDataException.__init__(self, student, msg)
        self.fileempty = fileempty

students = {}
f = input("Name of the file (files/prof-jekyll.txt): ")
try:
    file = open(f, 'rt')
    
    for linha in file:
        # stream = file.readline()
        line = linha.split()
        if not line: #se tiver uma linha vazia
            continue

        try:
            name = line[0] + '\t' + line[1]

            if name in students:
                students[name] += float(line[2])
            else:
                students[name] = float(line[2])

        except ValueError:
            raise BadLine(student=line[0] + ' ' + line[1], msg="Invalid format line", badline=linha)
    
    if not students:
        raise FileEmpty()
    
    for name in sorted(students):
        print(name, '\t', students[name])


except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

except FileEmpty as fe:
    print(f"Error in student {fe.student}: empty file!")

except BadLine as bl:
    print(f"Error in line [{bl.badline}]: {bl.args[0]}")

# except StudentsDataException as e:
#     print("Error: ", e)