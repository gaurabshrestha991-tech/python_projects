def firstOccurance(main_string, search_string):
    for i in range(len(main_string) - len(search_string) + 1):
        if main_string[i:i + len(search_string)] == search_string:
            return i
        
    return -1

main_string = input("Enter the main string: ")
search_string = input("Enter the string to search: ")

result = firstOccurance(main_string, search_string)

print("Index of first occurance: ", result)