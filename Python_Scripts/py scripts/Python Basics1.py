# -*- coding: utf-8 -*-

"""
            ############## DATA TYPES in PYTHON ######################33
                        1) Integer
                        2) Float 
                        3)String/Character
                        4)Boolean5
                        5) Complex Numbers
                        6)None 

"""

#Integer class int
a=2
print(a)
print(type(a))

#Integer class int
b = 937562846589286823621 #21 digits long
print(b)
print(type(b))

#float class float
c=3.145
print(c)
print(type(c))

#float class float
d=3.1234567891113151719 # 19digits long but can store till 15th digit precision
print(d)
print(type(d))

#string class str
ch= 's'
str1 ='this is string'
print(ch)
print(type(ch))
print(str1)
print(type(str1))

#Boolean - class bool
istrue=True
print(istrue)
print(type(istrue))

#Complex numbers
a = 2 + 1j
b = 100 + 10j


# Empty value or null data type
x = None
print(x)
print(type(x))


## Multiple variables in single line of code

a,b,c= 1,3,'shafi'
print(a,b,c)

a,b= 1,3,'shafi'
print(a,b)

a,b,_= 1,3,'shafi'
print(a,b)
 
a,b,_= 1,3,'shafi', 'mohiddin'
print(a,b)

a,b,_,_= 1,3,'shafi', 'mohiddin'
print(a,b,_,_)  #o/p: 1 3 mohiddin mohiddin




def f(m):
    m.append(3) # adds a number to the list. This is a mutation.
x = [1, 2]
f(x)
x


for i in range(1,25,3):
    if i%2==0:
        print(i, " Is even number")
    else:
        print(i, " Is odd number")