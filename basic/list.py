''' Python List data type '''

list_number = ['olma',12,'quyosh']

list_number.index('olma')
''' Index method return index , which is given data '''

list_number.copy()
''' Copy new list data '''

list_number.append('samsung')
''' Add new item to list to last '''

list_number.insert(-1,'lochin')
''' Insert method given two argument first is index item in list second one is given value  '''

list_number.remove(12)
''' Remove method given one argument it return only ValueError '''

list_number.pop(1)
''' Remove by default last item in list if given id item cut by id '''

list_number.count('quyosh')
''' this  method calculate count of item given value '''

new_list_reverse=[1,2,3,4,5]

new_list_reverse.reverse()
''' This method used return reverse given data it not crate new element it only modified index in list '''


print(new_list_reverse)