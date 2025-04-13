# Input marks for 9 students
marks = []
for i in range(9):
    mark = int(input(f"Enter the marks for student {i + 1}: "))
    marks.append(mark)
    
def selectionSort(A):
    n = len(A)
    for j in range(0, n - 1):
        smallest = j
        for i in range(j + 1, n):
            if A[i] < A[smallest]:
                smallest = i
        A[j], A[smallest] = A[smallest], A[j]

# Sort the marks using Selection Sort
selectionSort(marks)

# Calculate and print the median and range
def calculate_median(arr):
    n = len(arr)
    if n % 2 == 0:
        mid1 = n // 2
        mid2 = mid1 - 1
        median = (arr[mid1] + arr[mid2]) / 2
    else:
        median = arr[n // 2]
    return median

def calculate_range(arr):
    return max(arr) - min(arr)

median = calculate_median(marks)
range_value = calculate_range(marks)

print(f"Sorted Marks: {marks}")
print(f"Median: {median}")
print(f"Range: {range_value}")
