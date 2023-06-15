items=[
    ("Product1",11),
    ("Product2",9),
    ("Product3",10),
]

filtred=list(filter(lambda item: item[1] >= 10, items))

print(filtred)