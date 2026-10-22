def delete_duplicates(person):
    seen = set()
    result = []
    
    for row in sorted(person,key=lambda x: x["id"]):
        if row["email"] not in seen:
            seen.add(row["email"])
            result.append(row)
            
    return result

person = [
    {"id": 1, "email": "ram@gmail.com"},
    {"id": 2, "email": "shyam@gmail.com"},
    {"id": 3, "email": "ram@gmail.com"},
]

print(delete_duplicates(person))

