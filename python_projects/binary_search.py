def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)
    
print("----------Binary Search Project-----------")

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

numbers.sort()

print("Sorted list: ", numbers)

target = int(input("Enter the number to search: "))

print("\nChoose Search Method:")
print("1. Iterative Binary Search")
print("2. Recursive Binary Search")

choice = int(input("Enter your choice: "))

if choice == 1:
    result = binary_search_iterative(numbers, target)
elif choice == 2:
    result = binary_search_recursive(numbers, target, 0, len(numbers) - 1)
else:
    print("Invalid choice!")
    result = -1
    
if result != -1:
    print(f"\n{target} found at index {result}.")
else:
    print(f"\n{target} was not found in the list.")
    