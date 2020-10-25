#SYNTAX range(start,stop,increment) 
#stop value is not taken as i value & only that argument is mandatory


#get list of 30 numbers in fibonacci 
fib[0]=0
fib[1]=1
for i in range(2,29):
    fib[i]=fib[i-1]+fib[i-2]
print(fib)


#get upto 30 in fibona
a, b=0, 1
#a=0,b=1  is wrong 
print(a,end=' ')
while b<30:
    print(b, end=' ')
    a, b=b, a+b

# new method of for loop to access element in string or list/dictio. etc 
s=input('Enter string\n')
for c in s:
    print(c)
print(s)
    
## LIST COMPREHENSION
# the statement inside for is written before 
# Concl: for is evaluated one by one with function inside for loop & then complete result is transffered to outside function; useful more when array like thing is to form but can't stored

#Ex 1:
s=input()
print(any(c.isalnum() for c in s)) 
# Alternative: only integers can be stored not strings
s=input()
a=[]
a=zeros([len(s),1])
for i in range(len(s)):
    a[i]=s[i].isalnum()
print(any(a)) 

#Ex 2:
def times_tables():
    lst = []
    for i in range(10):
        for j in range (10):
            lst.append(i*j)
    return lst
# Alternative
times_tables = [j*i for i in range(10) for j in range(10)]

# Ex 3:
return("\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)]))   

###if else ladder
x=int(input('Enter an integer\n'))
if x<0:
    print('Be positive')
elif x==0:
    print('Zero')
elif x==1:
    print('Single')
else:
    print('More')

#squares of all odd no. below 10 not multiple of 3
for i in range(1,10,2):
    if i%3==0:
        continue
    print(i*i)
    
# 'continue' in loop skips the statements in loop after continue keyword & control goes over to next loop
#whereas 'break' terminates from loop
    
#pass command does nothing for that part of loop 
print('Odd no is:\n')
for i in range(5):
    if i%2==0:
        pass
    else:
        print(i,end=' ')
        


###Function
def pend_rhs(initial,t):
    theta=initial[0]
    omega=initial[1]
    g=9.81
    L=.2
    F=[omega, -(g/L)*sin(theta)]
    return F
from scipy.integrate import odeint
t=linspace(0,20,101)
initial= [10*pi/180, 0]
pend_sol=odeint(pend_rhs,initial,t)
#plotting tech
clf()
plot(t,pend_sol[:,0])
plot(t,pend_sol[:,1])
show()
xlabel('t')
legend(['theta','omega'])
title('Pendulum Soln')       
        

