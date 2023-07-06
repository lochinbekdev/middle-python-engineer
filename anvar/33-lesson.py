# Work with files

with open('./pi.txt') as file:
    pi=file.read()
print(type(pi))


pi=pi.rstrip()
pi=pi.replace('\n','')
pi=float(pi)
print(type(pi))