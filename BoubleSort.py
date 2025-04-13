#pseudo code bubblesort

#BUBBLESORT(A)
#for i = 1 to A.length-1
#    for j = A.length downto i + 1
#        if A[j]<A[j-1]
#            exchange A[j] with A[j-1]
 
A=[]

for v in range(1,8):
    A.append(int(input('Enter a number:')))
print(A)

def bubbleSort(A):
    n = len(A)#this is not compalsory
    for i in range (1,n):
        for j in range (1,n-i+1):
            if A[j] < A[j-1]:
                A[j],A[j-1] = A[j-1],A[j]#constant
bubbleSort(A)
print('Sorted Array:')
print(A)
