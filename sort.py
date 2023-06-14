items=[
    ("Product1",11),
    ("Product2",9),
    ("Product3",10),
]

# result=list(map(lambda item:item[1] ,items))
items.sort(key=lambda item:item[1])
print(items)