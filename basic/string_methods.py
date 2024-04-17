devknowledgezone = 'Personal blog'

devknowledgezone.capitalize() 
''' This return data with uppercase first literal'''

devknowledgezone.casefold()
''' This convert all upper literal to lowercase  '''

devknowledgezone.center(20,"*")
''' This method put data between the character, first arg is length of character second one is symbol to fill ''' 

devknowledgezone.count('blog') # it is output: 1
''' The number of occurrences of a substring in a given string  '''

devknowledgezone.encode('utf-8')
''' Method is encoded via utf-8,  ''' #But i have not understand purpose of method

devknowledgezone.endswith('g')
''' Return bolean value true or fale if string end with given value it return true otherwise false '''

devknowledgezone.expandtabs(5)
''' Replace with \t given in string argument is marked free space between words '''

devknowledgezone.find('P')
''' Return index of literal given in a string first come , if not include given data return -1 '''

formated_string="My channel name {}. That is most popular around developer".format(devknowledgezone)
''' Format method insert data to string given in variable '''

person = {'name':'John','age':20}
formated_map_string ="My friend name {name} , He is {age} yeard old".format_map(person)
''' It return data which is given in dictonary '''

devknowledgezone.index('P')
''' It is similar to find method but it return Value Error find method return -1 '''

devknowledgezone.isalnum()
''' This method check all character given string alphanumeric or not '''

devknowledgezone.isalpha()
''' If all character must be alphabet it return true '''

devknowledgezone.join('a')
''' It add charcter to string '''

devknowledgezone[::-1]
''' This is return reverce given data ''' 



print(devknowledgezone[::-1])