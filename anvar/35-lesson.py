# try except

age = input("Enter your age:  ")

try:
    age=int(age)    
except:
    print(f"Siz noto'g'ri qiymat kiritdingiz")
else: 
    print(f"Siz {2023-age} yilda tug'ilgansiz ")