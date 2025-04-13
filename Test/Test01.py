A=[]
for i in range (9):
    A.append (int(input("Enter the marks for student: ")))
    
print("Unsorted Array:",A)

def selectionSort(A):
    n=len(A)
    for j in range (0,n-1):
        smallest=j
        for i in range (j+1,n):
            if A[i]<A[smallest]:
                smallest = i
        A[j],A[smallest] = A[smallest],A[j]
        
selectionSort(A)



def calculateMedian(arr):
    n=len(arr)
    if n%2 == 0:
        mid1 = n//2
        mid2 = mid -1
        median = (arr[mid1]+arr[mid2]/2)
    else:
        median = arr[n//2]
    return median



def calculateRange(arr):
    return max(arr)-min(arr)

median = calculateMedian(A)
range_val = calculateRange(A)

print("Sorted Array: ",A)
print(" Median: ",median)
print("Range: ",range_val)
