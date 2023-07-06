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
    # print(result)

#  Yangi fayl yaratadi agar bor bo'lsa o'chirib yuboradi va yangilaydi
filename="data/new_file.txt"
name="Xakimov Alibek"

with open(filename,'w') as file:
    result=file.write(name)
    # print(result)


# Mavjud fayl bo'lsa qo'shadi yoq bo'lsa yaratadi
filename="data/new_file.txt"
name="Xakimov Alibek Hacker bek"

with open(filename,'a') as file:
    result=file.write('\n' + name + '\n')
    # print(result)


import pickle

talaba1={'ism':'hack','lastnamhe':'bek'}
talaba2={'ism':'hackbek','lastnamhe':'Alibek'}

# with open('data/info','wb') as file:
#     pickle.dump(talaba1,file)
#     pickle.dump(talaba2,file)

with open('data/info','rb') as file:
    talaba1=pickle.load(file)
    talaba2=pickle.load(file)

print(talaba1, '\n', talaba2)