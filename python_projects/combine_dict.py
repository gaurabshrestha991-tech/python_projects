# Combine two different dictionaries

dict1 = {
    "apple" : 10,
    "banana" : 30,
    "orange" : 40,
    "cherry" : 20,
    "pineapple" : 30
}

dict2 = {
    'mango' : 50,
    'grapes' : 60,
    'apple' : 40,
    'pineapple' : 30
}

result = dict1.copy()

for key, value in dict2.items():
    if key in result:
        result[key] += value
    else:
        result[key] = value
print(result)