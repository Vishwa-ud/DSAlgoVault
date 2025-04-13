#insetionSort
A=[]
n = 9

for i in range(0,n):
    number = int(input("Enter a nuber: "))
    if (number > 10 and number < 20):#limitation
        A.append(number)#store all in A array
    else:
        print("Invalid Number: ")
    i=i+1

print(A)

def insetionSort(A):
    for i in range(1,len(A)):#traverse the length of the array
        key = A[i]
        j = i - 1
        while j >= 0 and key < A[j]:
            A[j+1]=A[j]
            j = j -1
        A[j+1] = key
        
insetionSort(A)
print("Sorted Array:", A)
        
            
