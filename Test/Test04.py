A=[]
for v in range(10):
    A.append(int(input(f"Enter a number {v+1} : ")))
print("Unsorted array: ",A)

#def bubbleSort(A):
#    n=len(A)
#    for i in range(1,n):
#        for j in range (1,n - i + 1):
#            if A[j] < A[j - 1]:
#                A[j],A[j-1] = A[j-1],A[j]
#bubbleSort(A)
#print("Sorted Array: ",A)
    
def insetionSort(A):
    for i in range(1,len(A)):
        key=A[i]
        j = i-1
        while j>=0 and key < A[j]:
            A[j+1]= A[j]
            j=j-1
        A[j+1] = key
        
insetionSort(A)
print("Sorted array: ",A)

#def selectionSort(A):
#    n=len(A)
#    for j in range (0,n-1):
#        smallest = j
#        for i in range(j+1,n):
#            if A[i] < A[smallest]:
#                smallest = i
#        A[j],A[smallest] = A[smallest],A[j]
        
#selectionSort(A)
#print("Sorted Array: ",A)
        
        
