# COL100 Assignment 1
# Entry no. 2021CS10577
#
# Question 1
#
def add(a,b,c):
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
# Question 2
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
    t0=add(a0,b0,c)
    t1=add(a1,b1,t0[1])
    t2=add(a2,b2,t1[1])
    t3=add(a3,b3,t2[1])
    return(t0[0],t1[0],t2[0],t3[0],t3[1])
#
# Question 3
#
def cmp(a0,a1,a2,a3,b0,b1,b2,b3):
#
# Compares two 4-bit binary numbers
# Chechks if first number is less than or equal to the second number(a<=b)
#
# Parameters:
# ai(i=0,1,2,3): boolean -- first number in binary
# bi(i=0,1,2,3): boolean -- second number in binary
# 
# Returns: boolean -- true if a<=b otherwise false
    a=(a3 and b3) or (not (a3 or b3))# this statement is equivalent to a3==b3
    b=(a2 and b2) or (not (a2 or b2))
    c=(a1 and b1) or (not (a1 or b1))
    d=(a0 and b0) or (not (a0 or b0))
    e=a3 and (not a)
    f=a and(a2 and (not b))
    g=a and ( b and (a1 and (not c)))
    h=(a and b) and (c and (a0 and (not d)))
    i=(e or f) or (g or h)
    return not(i)
    
#
# Question 4
#
def sub(a,b,c):
# 1-bit subtractor
#
# Parameters:
# a: Boolean -- First bit
# b: Boolean -- Second bit
#
# Returns: tuple of 2 Boolean -- difference and carry
    s=(a or b) and (not (a and b))
    s_=(s or c) and (not (s and c))
    c=(b and (not (a and b)) or (c and (not s)))
    return (s_,c)

#
def sub4(a0,a1,a2,a3,b0,b1,b2,b3):
#
# Calculates difference of two 4-bit binary numbers in sign magnitude form
#
# Parameters:
# ai(i=0,1,2,3): boolean -- first number in binary
# bi(i=0,1,2,3): boolean -- second number in binary
# 
# Returns: tuple of 5 boolean values -- difference between a and b on sign magnitude form
#                                       0 to 3 index of tuple give the magnitude
#                                       index 4 gives sign
    a=(a0,a1,a2,a3)
    b=(b0,b1,b2,b3)
    s=False
    if cmp(a0,a1,a2,a3,b0,b1,b2,b3):
        c=a
        a=b
        b=c
        s=True
    d0=sub(a[0],b[0],False)
    d1=sub(a[1],b[1],d0[1])
    d2=sub(a[2],b[2],d1[1])
    d3=sub(a[3],b[3],d2[1])
    return (d0[0],d1[0],d2[0],d3[0],s)
#
# Question 5
#
def add8(a,b,c):
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
# Question 6
#
def mul4(a,b):
#
# Calculates product two 4-bit binary numbers through recursion
#
# Parameters:
# a : tuple of boolean -- first number in binary
# b : tuple of boolean -- second number in binary
#
# Returns: tuple with a boolean values -- product of the two numbers in 8 bit binary form
    if((b[0] or b[1]) or (b[2] or b[3])):
        b_=sub4(b[0],b[1],b[2],b[3],True,False,False,False)
        d=(b_[0],b_[1],b_[2],b_[3])
        return add8((a[0],a[1],a[2],a[3],False,False,False,False),(mul4(a,d)),False)[0]# equivalent to return a+mul4(a,b-1)
    else:
        return (False,False,False,False,False,False,False,False)
    
#
#
# End of assignment
#
# Extra code
#
# this is an alternate function for comparision using if-else

"""(You may delete this line to uncomment all functions below)

def cmp_alt(a0,a1,a2,a3,b0,b1,b2,b3):
   if((a3 and b3) or (not (a3 or b3))):
        if((a2 and b2) or (not (a2 or b2))):
            if((a1 and b1) or (not (a1 or b1))):
                if((a0 and b0) or (not (a0 or b0))):
                    r=True
                elif(a0):
                    r=False
                else:
                    r=True
            elif(a1):
                r=False
            else:
                r=True
        elif(a2):
            r=False
        else:
            r=True
   elif(a3):
        r=False
   else:
        r=True
   return r
        
"""

# these are alternate functions for subtraction

"""

def sub4_alt(a0,a1,a2,a3,b0,b1,b2,b3):
    a=(a0,a1,a2,a3)
    b=(b0,b1,b2,b3)
    s=False
    if cmp(a0,a1,a2,a3,b0,b1,b2,b3):
        c=a
        a=b
        b=c
        s=True
    b=(not b[0],not b[1],not b[2],not b[3])# equals 15-b
    ans=add4(a[0],a[1],a[2],a[3],b[0],b[1],b[2],b[3],True)# carry to make 16-b
    return (ans[0],ans[1],ans[2],ans[3],s)

def sub4_alt2(a0,a1,a2,a3,b0,b1,b2,b3):
# This function computes difference using only boolean alzebra   
    a_=(a0,a1,a2,a3)
    b_=(b0,b1,b2,b3)
    t4=cmp(a0,a1,a2,a3,b0,b1,b2,b3)
# The four lines below exchange a and b if a<=b
    a=((t4 and b_[0])or(not t4 and a_[0]),(t4 and b_[1])or(not t4 and a_[1]),\
       (t4 and b_[2])or(not t4 and a_[2]),(t4 and b_[3])or(not t4 and a_[3]))
    b=((t4 and a_[0])or(not t4 and b_[0]),(t4 and a_[1])or(not t4 and b_[1]),\
       (t4 and a_[2])or(not t4 and b_[2]),(t4 and a_[3])or(not t4 and b_[3]))
    c=False
    t0=(a[0] or b[0]) and (not (a[0] and b[0]))
    c=(b[0] and (not (a[0] and b[0])) or (c and (not t0)))
    t1_=(a[1] or b[1]) and (not (a[1] and b[1]))
    t1=(t1_ or c) and (not (t1_ and c))
    c=(b[1] and (not (a[1] and b[1])) or (c and (not t1_)))
    t2_=(a[2] or b[2]) and (not (a[2] and b[2]))
    t2=(t2_ or c) and (not (t2_ and c))
    c=(b[2] and (not (a[2] and b[2])) or (c and (not t2_)))
    t3=(a[3] or b[3]) and (not (a[3] and b[3]))
    t3=(t3 or c) and (not (t3 and c))
    return (t0,t1,t2,t3,t4)

"""

# these are alternate functions for multliplication

"""
def mul4_alt(a,b):
# This function computes product through recursion without using conditional statements
    t=(b[0] or b[1]) or (b[2] or b[3])
    b_=sub4(b[0],b[1],b[2],b[3],True,False,False,False)
    d=(b_[0],b_[1],b_[2],b_[3])
# the lines below return: (False,False,False,False,False,False,False,False) if t=False
    return t and add8((a[0],a[1],a[2],a[3],False,False,False,False),(mul4(a,d)),False)[0][0],\
        t and add8((a[0],a[1],a[2],a[3],False,False,False,False),(mul4(a,d)),False)[0][1],\
            t and add8((a[0],a[1],a[2],a[3],False,False,False,False),(mul4(a,d)),False)[0][2],\
                t and add8((a[0],a[1],a[2],a[3],False,False,False,False),(mul4(a,d)),False)[0][3],\
                    t and add8((a[0],a[1],a[2],a[3],False,False,False,False),(mul4(a,d)),False)[0][4],\
                        t and add8((a[0],a[1],a[2],a[3],False,False,False,False),(mul4(a,d)),False)[0][5],\
                            t and add8((a[0],a[1],a[2],a[3],False,False,False,False),(mul4(a,d)),False)[0][6],\
                                t and add8((a[0],a[1],a[2],a[3],False,False,False,False),(mul4(a,d)),False)[0][7]

def mul4_alt2(a,b):
    r=(False,False,False,False,False,False,False,False)
    if(b[0]):
        r=add8(r,(a[0],a[1],a[2],a[3],False,False,False,False),False)[0]
    if(b[1]):
        r=add8(r,(False,a[0],a[1],a[2],a[3],False,False,False),False)[0]
    if(b[2]):
        r=add8(r,(False,False,a[0],a[1],a[2],a[3],False,False),False)[0]
    if(b[3]):
        r=add8(r,(False,False,False,a[0],a[1],a[2],a[3],False),False)[0]
    return r

"""
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
    c=cmp(a_[0],a_[1],a_[2],a_[3],b_[0],b_[1],b_[2],b_[3],)
    print("cmp gives ",c)
    c_=cmp_alt(a_[0],a_[1],a_[2],a_[3],b_[0],b_[1],b_[2],b_[3],)
    print("cmp_alt gives ",c_)
    ad=add4(a_[0],a_[1],a_[2],a_[3],b_[0],b_[1],b_[2],b_[3],False)
    sb=sub4(a_[0],a_[1],a_[2],a_[3],b_[0],b_[1],b_[2],b_[3])
    print("add4 gives: ",con_to_decimal(ad[0],ad[1],ad[2],ad[3],ad[4],False,\
                                        False,False,False))
    print("sub4 gives: ",con_to_decimal(sb[0],sb[1],sb[2],sb[3],False,False,\
                                        False,False,sb[4]))
    sb=sub4_alt(a_[0],a_[1],a_[2],a_[3],b_[0],b_[1],b_[2],b_[3])
    print("sub4_alt gives: ",con_to_decimal(sb[0],sb[1],sb[2],sb[3],False,False,\
                                        False,False,sb[4]))
    sb=sub4_alt2(a_[0],a_[1],a_[2],a_[3],b_[0],b_[1],b_[2],b_[3])
    print("sub4_alt2 gives: ",con_to_decimal(sb[0],sb[1],sb[2],sb[3],False,False,\
                                        False,False,sb[4]))
    ad=add8(a_,b_,False)
    d=con_to_decimal(ad[0][0],ad[0][1],ad[0][2],ad[0][3],ad[0][4],ad[0][5],\
                     ad[0][6],ad[0][7],ad[1])
    print("add8 gives: ",d)
    mt=mul4(a_,b_)
    e=con_to_decimal(mt[0],mt[1],mt[2],mt[3],mt[4],mt[5],mt[6],mt[7],False)
    print("mul4 gives: ",e)
    mt=mul4_alt(a_,b_)
    e=con_to_decimal(mt[0],mt[1],mt[2],mt[3],mt[4],mt[5],mt[6],mt[7],False)
    print("mul4_alt gives: ",e)
    mt=mul4_alt2(a_,b_)
    e=con_to_decimal(mt[0],mt[1],mt[2],mt[3],mt[4],mt[5],mt[6],mt[7],False)
    print("mul4_alt2 gives: ",e)

#"""