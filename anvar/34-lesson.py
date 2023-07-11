# Json

import json

x=10 
x_json=json.dumps(x)
 

number=(12,23,45,46)
number_json=json.dumps(number)

# print(type(number_json))


ill =  {
    "name" : "Alex Sandres",
    "age" : 30,
    "familiy" : True,
    "child" : ("Azle","Xazr"),
    "allergiya" : None,
    "hub" : [
        {"name": "Analgin","count":0.53},
        {"name": "Panadol","count":0.53}
    ]
}


# with open('ill.json','w') as f:
#     json.dump(ill,f)

ill_json=json.dumps(ill, indent=4)
decode =json.loads(ill_json)
print(type(decode))
# print(ill.keys())