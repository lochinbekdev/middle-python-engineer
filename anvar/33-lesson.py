# Work with files

with open('data/pi.txt') as file:
    pi=file.read()
# print(type(pi))


pi=pi.rstrip()
pi=pi.replace('\n','')
pi=float(pi)
# print(type(pi))


with open('data/students.txt') as file:
    for talaba in file:
        result=talaba

with open('data/students.txt') as line:
    students=line.readlines()
    result=[student.rstrip() for student in students]
    print(result)
