A=[]
for i in range(9):
    A.append(int(input(f"Enter a nubmer{i+1}: ")))

print("Unsorted Array: ",A)

def bubbleSort(A):
    n = len(A)
    for i in range(1,n):
        for i in range(1,n-i+1):
            if A[j] < A[j-1]:
                A[j],A[j-1] = A[j-1],A[j]
                
bubbleSort(A)
print('Sorted Array:',A)

