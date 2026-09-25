list = [10, 50, 90, 60]
number = int(input("Enter a number: "))
found = False

for num in range(len(list)):
    if number == list[num]:
        print("Found! At index: ", num)
        found = True
        break
    
if not found:
    print("Not found!")
