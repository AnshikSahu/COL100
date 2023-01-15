#
# COL100 Assignment 2
#
# Question 3
#
# Note : The functions here may have some additional changes to the algorithm in question 1
# to cope up with the non-flexible inputs(4-bit) and output(8-bit)
#
def mul4(a,b):
#
# returns the products of numbers represented by binary numerals a and b
# the product is computed by recursion
# converts 4-bit input to 8-bit binary numerals and then forwards them to mul(a,b) to compute the result
#
# Parameters:
#
# a: tuple of 4 boolean values -- first number
# b: tuple of 4 boolean values -- second number
#
# returns: tuple of 8 boolean values representing product of a and b in binary
#
    a2=(a[0],a[1],a[2],a[3],False,False,False,False)
    b2=(b[0],b[1],b[2],b[3],False,False,False,False)
    return mul(a2,b2) # calling the mul function to compute result and returning the product
#
#
def mul(a,b):
#
# returns the product of two numbers represented by two binary numerals
# uses recursion to compute the product
#
# Parameters:
#
# a: tuple of 8 boolean values -- first number
# b: tuple of 8 boolean values -- second number
#
# returns: tuple of 8 boolean values representing product of a and b in binary
#
    if(b==(False,False,False,False,False,False,False,False)):# this statements ends the recursion when b becomes 0
        return (False,False,False,False,False,False,False,False)
    # the higher(b) function is used to decrease value of b
    elif(lowest(b)):# adding a if bit at unit's place is 1/False
        return add(a,mul(join(a,0),higher(b)),False)[0]
    else:
        return mul(join(a,0),higher(b))# updating withou adding anything if bit at unit's place is 0/False
#
#
# Question 5
#
#
def mul4i(a,b):
#
# returns the products of numbers represented by binary numerals a and b
# the product is computed by iteration
# converts 4-bit input to 8-bit binary numerals and then forwards them to mul(a,b) to compute the result
#
# Parameters:
#
# a: tuple of 4 boolean values -- first number
# b: tuple of 4 boolean values -- second number
#
# returns: tuple of 8 boolean values representing product of a and b in binary
#
    a2=(a[0],a[1],a[2],a[3],False,False,False,False)
    b2=(b[0],b[1],b[2],b[3],False,False,False,False)
    s=(False,False,False,False,False,False,False,False)
    return muli(a2,b2,s) # calling the mul function to compute result and returning the product
#
#
def muli(a,b,s):
#
# returns the product of two numbers represented by two binary numerals
# uses iteration to compute the product
#
# Parameters:
#
# a: tuple of 8 boolean values -- first number
# b: tuple of 8 boolean values -- second number
# s: tuple of 8 boolean values -- stores sum of all intermediate products before current step
#
# returns: tuple of 8 boolean values representing product of a and b in binary
#
    if(b==(False,False,False,False,False,False,False,False)):# this statements ends the recursion when b becomes 0
        return s
    # the higher(b) function is used to decrease value of b
    elif(lowest(b)):
        s2=add(a,s,False)[0]# adding a if bit at unit's place is 1/True
        return muli(join(a,0),higher(b),s2)
    else:
        return muli(join(a,0),higher(b),s)# updating withou adding anything if bit at unit's place is 0/False
#
#
# Helper Functions
#
#
def lowest(a):
#
# Parameters:
#
# a: tuple of 8 boolean values -- a binary numeral
#
# returns: boolean -- the lowest/least significant bit of the binary numeral a
    return a[0]
#
#
def higher(a):
#
# Drops the last bit of binary numeral and returns the higher bits after filling the blank spaces with False
# This is equivalent to the quotient of division of a by 2
#
# Parameters:
#
# a: tuple of 8 boolean values -- a binary numeral
#
# returns: tuple of 8 boolean values -- the higher bits of numeral a
    return (False or a[1],False or a[2],False or a[3],False or a[4],False or a[5],False or a[6],False or a[7],False)
#
#
def join(a,d):
#
# Adds a 0/False to the end of a binary numeral
# this is equivalent to multiplication by 2
#
# Parameters:
#
# a: tuple of 8 boolean values -- a binary numeral
#
# returns: tuple of 8 boolean values -- the binary numeral after adding a False bit at the end
    return (d,a[0],a[1],a[2],a[3],a[4],a[5],a[6])
#
#
# this is code for the add8(a,b) function from assignment 1 in replacement for add(a,b)
# as the add(a,b) could not be created without tuple functions which are restricted   
#
#   
def add1(a,b,c):
#
# Calculates sum of three bits.
#
# Parameters:
#
# a: boolean -- first bit
# b: boolean -- second bit
# c: boolean -- third bit
#
# Returns: tuple of 2 boolean values -- sum of the bits in binary 
    b0=(a or b) and not (a and b)
    b1=a and b
    b2=(c or b0) and not (c and b0)
    b3=(c and b0) or b1
    return (b2,b3)
#
#
def add4(a0,a1,a2,a3,b0,b1,b2,b3,c):
#
# Calculates sum of two 4-bit binary numbers and a carry
#
# Parameters:
# ai(i=0,1,2,3): boolean -- first number in binary
# bi(i=0,1,2,3): boolean -- second number in binary
# c : boolean -- carry
# 
# Returns: tuple of 5 boolean values -- sum of the numbers and carry in binary
    t0=add1(a0,b0,c)
    t1=add1(a1,b1,t0[1])
    t2=add1(a2,b2,t1[1])
    t3=add1(a3,b3,t2[1])
    return(t0[0],t1[0],t2[0],t3[0],t3[1])
#
#
def add(a,b,c):
#
# Calculates sum of two 8-bit binary numbers and carry
#
# Parameters:
# a : tuple of boolean -- first number in binary
# b : tuple of boolean -- second number in binary
# c : boolean -- carry
# 
# Returns: tuple with boolean values-- tuple at index 0 is the sum of the numbers and carry in 8-bit
#                                      index 1 contains the carry from addition  
    r=add4(a[0],a[1],a[2],a[3],b[0],b[1],b[2],b[3],c)
    t=add4(a[4],a[5],a[6],a[7],b[4],b[5],b[6],b[7],r[4])
    return ((r[0],r[1],r[2],r[3],t[0],t[1],t[2],t[3]),t[4])
#
#
# The code below can be used to test all the functions in this code
# by uncommenting it and then calling the test() function
#
"""

def a(a):
    if(a==1):
        return True
    else:
        return False
    
def con_to_binary(n):
    t0=a(n%2)
    n=n//2
    t1=a(n%2)
    n=n//2
    t2=a(n%2)
    n=n//2
    t3=a(n%2)
    n=n//2
    t4=a(n%2)
    n=n//2
    t5=a(n%2)
    n=n//2
    t6=a(n%2)
    n=n//2
    t7=a(n%2)
    n=n//2
    t8=a(n%2)
    return (t0,t1,t2,t3,t4,t5,t6,t7,t8)

def con_to_decimal(a0,a1,a2,a3,a4,a5,a6,a7,c):
    n=1*a0+2*a1+4*a2+8*a3+16*a4+32*a5+64*a6+128*a7
    if(c):
        n=-1*n
    return n

def test():
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    a_=con_to_binary(a)
    b_=con_to_binary(b)
    mt=mul4(a_,b_)
    e=con_to_decimal(mt[0],mt[1],mt[2],mt[3],mt[4],mt[5],mt[6],mt[7],False)
    print("mul4 gives: ",e)
    mti=mul4i(a_,b_)
    e=con_to_decimal(mti[0],mti[1],mti[2],mti[3],mti[4],mti[5],mti[6],mti[7],False)
    print("mul4i gives: ",e)
#"""