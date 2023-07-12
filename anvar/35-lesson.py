# try except

# age = input("Enter your age: ")

# try:
#     age=int(age)    
# except ValueError:
#     print(f"Siz noto'g'ri qiymat kiritdingiz")
# else: 
#     print(f"Siz {2023-age} yilda tug'ilgansiz ")


# Error types


# ZeroDivisionError

# x,y=5,10

# try: 
#     y/(x-5)
# except  ZeroDivisionError:
#     print(("0ga bo'linmaydi"))





# IndexError

# fruits=['banana','poteto','tometo']

# try:
#     print(fruits[45])
# except IndexError:
#     print(f"Ro'yxatda {len(fruits)} ta meva bor xolos")



# KeyError

# user = {
#     "username" : "occupytheweb",
#     "status" : "active",
#     "email" : "admin@gmail.com",
#     "phone" : "+9989334523",
# }

# key="email"

# try:
#     print(f"Foydalanuvchi:{user[key]}")
# except KeyError:
#     print("Bunday qiymat mavjud emas")


filename = "data.txt"

try:
    with open(filename) as f:
        text=f.read()
except FileNotFoundError:
    print(f"{filename} bunday fayl mavjud emas")
