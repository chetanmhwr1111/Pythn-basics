#array with 5 pts from 0 to 2pi
t=linspace(0,2*pi,5)

## range & indexing behaves in same way
#gives list of no. from 'start' (by default its 0)value and doesn't give stop value  
t=range(start, stop, step length) 
#p[initial no. index:  final no. index obtained+1  :step length(by default 1)]  
p[0::2]                               
# for 100 loops get time required to run each loop
%%timeit -n 100



##plotting ex
L=[.2,.3,.4,.5,.6,.7,.8]
t=[.9,1.19,1.30,1.47,1.58,1.77,1.83]
tsq=[]
for time in t:              #syntax for loop
    tsq.append(time*time)
plot(L,tsq)
show()
t=array(t)  #converting list into aray
tsq= t*t   
print(tsq)
plot(L,tsq)


### Operations

# Boolean operns
a=False
b=True
c=True
d=(a and b) or c   #to get output you have to type variable explicitly 
#!= in python

#Binary
# to find exponent  use a**b  or pow(a,b)    
# float is always in form of decimal but not integer
#'%' gives remainder
# '//' floor division, returns only integer value of quotient
#'/' returns float value of quotient 
# '%' & // can be used to extract no. from fig
c=3+4j  
c.imag, c.real #are attributes
c.conjugate()# are functions
abs(c)


## diff b/w list & Numpy array
#list
a=[2,3,7,5]
a[1]=4
print(a*2)
b=array([a])   # list converted into array
print(b*2)

#array                              #numpy as np is always used as np.(any function)
b=array([[2,5,4],[5,7,8]])
b[1,2]=4
print(b)
a=array([[11,12,13],[21,22,23],[31,32,33]]) 
a.shape        #size of array in form of tuple
#for assigning array as below, initialisation before is necessary to make it understand data type
a=zeros([5,3])  4,5,6,
a[r,:]=array([1,5,4]) 


## SLICING 
p=array([[2,5,4])
p[0]  #first index of list
p[-1]  #last index of list

p[0:3:2]  #p[initial no. index:final no. index+1:step length]                         
p[0:-1]         #output will not contain value of last index due above reason
p[1:]           #output will contain value of last index since no end index defined                    
                            
# Array SLICING               
a[1,2]          #accesing an element of array just like C
a[0:2,:]       # all columns & starting 2 rows(0 & 1)


##Array Operatin
# converting row vector(n) into matrix 
n = arange(0, 12, 2) # gives array from 0 to 10 only with increment of 2
N = n.reshape(3,2 ) 

print(x * y) # elementwise multiplication
print(x / y) # elementwise divison
print(x**2)     # elementwise power 
print(x.dot(y)) # Matrix multip
print(x.T)    #to get the transpose.
