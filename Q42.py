def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1        

numbers = [10, 20, 30, 40, 50]

key = int(input("Enter number to search: "))

result = linear_search(numbers, key)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
