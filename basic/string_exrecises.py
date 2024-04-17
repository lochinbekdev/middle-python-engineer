#Calculate average data given an array
 
def calculate_average(listdata):
    result=0
    for i in listdata:
        result += i
    return result / len(listdata)
    
numbers=calculate_average([4,5,7,8])


#Reverse given string

def reverse_string(word):
    return word[::-1]

reverse_data=reverse_string('Lochinbek')



#Factorial programs 

def factorial(n):
    if n < 0:
        raise ValueError('Qiymat noldan katta bo\'lishi kerak')
    elif n == 0:
        return 1
    else:
        return n * factorial(n -1)

number=factorial(5)


#Palindrome retrun similar word default statement and reverce statement . That function return only boolean data 

def is_palindrome(word):
    word_lower=word.lower()
    reverse_word=word_lower[::-1]
    return word_lower == reverse_word

palindrome=is_palindrome('Madam')


# Fibonacce sequences  

def fibonace(n):
    fib_sequnce=[0,1]
    while len(fib_sequnce) < n:
        fib_sequnce.append(fib_sequnce[-1] + fib_sequnce[-2])
    return fib_sequnce
    

fibonace_result=fibonace(3)
