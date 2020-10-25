clear
clear all
#only single line comment 


### print()
Supressing value: #Storing value in a variable supresses value 
#in editor & even in pane window & 
#in pane window writing variable'var' gives output
#but in editor print(var) used to get output
#print() automatically checks for logical & give Boolean as True or False
print('adfa \n fsfsafa') #to change to a new line
print() # leaves a line & change to new
end=' ' avoids change of line in print()
#to restrict float values of 'a' to 2 decimal pts
print("{0:.2f}".format(a))


# Variables which store any type of data is called Object
# and the attributes  or functionapplied on that object is called Method
# Different objects of particular data type is called instances like that of 'p & s' of type str or CLASS objects

### Data types- int, float, str
#to find data type of a
type(a) 
# explicitly cast
no=int(a)
a=str(no)
#compares datatype of input to a desired datatype
a=input()
isinstance(a,str)

                                                    #Note: slicing & indexing are valid same as that of numpy
### String-  a data type
#strings in 1 line requires 1 quotes apart from quotes itself 
' "the wick over well" ' 
 s='Hello'
 p='World'
 len(a)  #get length of string
 # Addition & multiplication on strings only
 a=s+p    #Concatenate Strings only not any data type
 b=s*4 #just like s+s+s+s
                                                #Note: all below functions hold for strings which can or cannot be inside tuple or list
 a.startswith('Hell'), a.endswith('ld')
 a[i].islower() #checking for single character of string
 a.upper(), a.lower()
 a.isalpha()  # checks whether string is only alphabetical or not
 a.isalnum()   #both alpha & numeric present
 a.isnumeric()      #checks whether string 'a' is integer or not
 a.swapcase()
 
                                                # NOte: don't apply to single characters of strings
 a.replace('Hello','Goodbye')
a.remove('letter or no. to be removed') 
a.index('ll')   # gives index of  part of string present  
a.split(' ')    # only seperates numbers in particular string with spaces
a.split(',')
alp=', '.join(['a','b','c']) # joins elements of list with commas
a.sort() #sorting in ascending or descending
'Hell' in a #for finding substring in particular string

#string formatting
x,y =1, 1.234
print('x is %s ,y is %s')    #just like C declaring variables & string printing 



### Compound data types

#list & tuples(t=() ) is never initialised with its size & generally also its unknown
# & is an advantage too but for array its necessary to initialize (array is always numpy array)
t=[], t=()

##TUPELS () - Whose elements can't be changed once its created (difference comes in use of brackets)
a=('apple',2,'Mango')
a[0]='berries' 
a=(2, 9, 7, (8, 10),[4,7]) #nested tuple
a[4][1] #accessing nested tuple

## LIST []- whose elements can be changed by assigning
a=['apple',2,'Mango']
a[0]='berries' 
a.append([8,10]) or a.append((8,10)) #adds only one element to list
a.extend([8,10]) #adds 2 element to list

del(a[4])
a.remove(2)
a=[2, 9, 7, [8, 10]] #contains only 4 elements
print(a[3][1]) #Accesing Nested list

##SET - contains only one element & doesn't allow duplication- not much useful
A={ 1,'asd','Thriller bleack',254, 'asd'}
B=A.add('fdasf')

## DICTIONARY {} & format()- to assign values in a general statement - single element of data frame
sales_rec={'price': 3.24,
            'num_items':4,
             'person':'Chetan'}
             
sales_statement='{} bought {} items at price of {} for a total of {}'
print(sales_statement.format(sales_rec['person'],
                              sales_rec['num_items'],
                              sales_rec['price'],
                              sales_rec['price']*sales_rec['num_items']))


    
##  Use of split & list manipulation
fruits=input('Enter list of fruits seperated by comma\n')
print(fruits) 
fruits=fruits.split(',') 
print(fruits)   
fruits[1][1]    
for fruit in fruits:    
      print(fruit)    

firstname = 'Christopher Arthur Hansen Brooks'.split(' ')[0] # [0] selects the first element of the list
lastname = 'Christopher Arthur Hansen Brooks'.split(' ')[-1] # [-1] selects the last element of the list
print(firstname)
print(lastname)


