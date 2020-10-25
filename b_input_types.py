### input()
var=input('The character input will always be a string')
int_var=int(input('Input will only be a single integer variable'))  #typecasted

# any size of array input
Co=zeros([2,2,2])
for i in range(2):
    for j in range(2):
        for k in range(2):
            print('Enter coordinates of',k+1,'nodes of element',i+1,'along',j+1,'direction')
            Co[j,k,i]=input()

# taking input in  list WITHOUT DEFINING list size
t=[]
n=int(input())
for i in range(n):
    N=int(input())
    t.append(N)
print(t)

#integer input with spaces to form list & then converted into array      
a=list(map(int, input().split())) 
print(a*2)
b=array([a]) #typecasting to array
print(b*2)
#Input Ex:
# 2 3 5 4

#filling rows/columns of arrays
a=zeros([2,2])
a[0]=array(list(map(int, input().split())))
a[1]=array(list(map(int, input().split())))
      
#character input with spaces
i,c=input().split()
#integer input with spaces
i,c=map(int, input().split())

#assigning variable        
x,y =1, 1.234 

# Forming DICTIONARY: Storing string or integers in array form corresponding to PARTICULAR index like name here
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
        
comnd, *line = input().split()
a, b = list(map(int, line))