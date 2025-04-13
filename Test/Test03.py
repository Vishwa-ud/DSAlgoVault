def selectionSort(arr):
    n = len(arr)
    for j in range(0, n - 1):
        smallest = j
        for i in range(j + 1, n):
            if arr[i] < arr[smallest]:
                smallest = i
        arr[j], arr[smallest] = arr[smallest], arr[j]

def calculate_quartiles(arr):
    n = len(arr)
    middle = n // 2

    if n % 2 == 0:
        lower_half = arr[:middle]
        upper_half = arr[middle:]
    else:
        lower_half = arr[:middle]
        upper_half = arr[middle + 1:]

    lower_quartile = (lower_half[len(lower_half) // 2 - 1] + lower_half[len(lower_half) // 2]) / 2
    upper_quartile = (upper_half[len(upper_half) // 2 - 1] + upper_half[len(upper_half) // 2]) / 2

    return lower_quartile, upper_quartile

# Input heights for 7 students
heights = []
for i in range(7):
    height = float(input(f"Enter the height (in meters) for student {i + 1}: "))
    heights.append(height)

# Sort the heights using Selection Sort
selectionSort(heights)

# Calculate and print the lower and upper quartiles
lower_quartile, upper_quartile = calculate_quartiles(heights)

print(f"Sorted Heights: {heights}")
print(f"Lower Quartile (Q1): {lower_quartile} meters")
print(f"Upper Quartile (Q3): {upper_quartile} meters")
