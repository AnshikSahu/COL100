#
# COL100 Assignment 3
#
# Question 1
#
# 1
# Taylor series computation of e^x upto n terms
#
def expn(x,n):
#
# Input:
#    x: float : the number whose image is to be calculated
#    n>0 : int : number of terms of taylor series upto which the output is to be calculated
#
# Output: float : e^x upto n terms of taylor series
#
# Initialisation
    i=1 # keeps track of number of term
    i_term=1 # stores the ith term
    ans=0 # stores the sum of first (i-1) terms
    # we start with i=1 for 1st term
    # i_term = first term = 1
    # ans = sum of (i-1)=0 terms =0
    # Invariant: i_term==(x^i)/x!
    # Invariant: ans==sum of first i-1 terms
    while(i<=n):# Termination: i increases n+1
        ans=ans+i_term # adding ith term to ans
        i_term=i_term*x/i # calculating next term
        i=i+1 # increasing the value of i
    return ans
    #
    # Time Complexity:
    #
    # for every iteration, 
    # number of arthematic operation performed is constant=5
    # total number of iterations = n
    # thus, time comlexity T(n)=5*n
    # therefore, time complexity is O(n)
#
# 2
#
# Taylor series computation of cos x upto n terms
def cosine(x,n):
#
# Input:
#    x: float : the number whose image is to be calculated
#    n>0 : int : number of terms of taylor series upto which the output is to be calculated
#
# Output: float : cos x upto n terms of taylor series
#
    i=1 # keeps track of number of term
    i_term=1 # stores the ith term
    ans=0 # stores the sum of first (i-1) terms
    # we start with i=1 for 1st term
    # i_term = first term = 1
    # ans = sum of (i-1)=0 terms =0
    # Invariant: i_term==(-1)^(i+1)*(x^(2i-2))/(2i-2)!
    # Invariant: ans==sum of first i-1 terms
    while(i<=n):# Termination: i increases n+1
        ans=ans+i_term # adding ith term to ans
        i_term=i_term*((-1)*x*x)/(2*i*(2*i-1)) # calculating next term
        i=i+1 # increasing the value of i
    return ans
    #
    # Time Complexity:
    #
    # for every iteration, 
    # number of arthematic operation performed is constant=11
    # total number of iterations = n
    # thus, time comlexity T(n)=11*n
    # therefore, time complexity is O(n)
#
# 3
# Taylor series computation of 1/(1-x) upto n terms for |x|<1
#
def inverse(x,n):
#
# Input:
#    x: float : the number whose image is to be calculated
#    n>0 : int : number of terms of taylor series upto which the output is to be calculated
#
# Output: float : 1/(1-x) upto n terms of taylor series
#
    if(abs(x)>=1):# Checking if input is valid
        return "Invalid Input"
    i=1 # keeps track of number of term
    i_term=1 # stores the ith term
    ans=0 # stores the sum of first (i-1) terms
    # we start with i=1 for 1st term
    # i_term = first term = 1
    # ans = sum of (i-1)=0 terms =0
    # Invariant: i_term==x^(i-1)
    # Invariant: ans==sum of first i-1 terms
    while(i<=n):# Termination: i increases n+1
        ans=ans+i_term # adding ith term to ans
        i_term=i_term*x # calculating next term
        i=i+1 # increasing the value of i
    return ans
    #
    # Time Complexity:
    #
    # for every iteration, 
    # number of arthematic operation performed is constant=4
    # total number of iterations = n
    # thus, time comlexity T(n)=4*n
    # therefore, time complexity is O(n)
#
# 4
# Taylor series computation of ln(1+x) upto n terms
#
def natural_log(x,n):
#
# Input:
#    x: float : the number whose image is to be calculated
#    n>0 : int : number of terms of taylor series upto which the output is to be calculated
#
# Output: float : ln(1+x) upto n terms of taylor series
#
    i=1 # keeps track of number of term
    i_term=x # stores the ith term
    ans=0 # stores the sum of first (i-1) terms
    # we start with i=1 for 1st term
    # i_term = first term = 1
    # ans = sum of (i-1)=0 terms =0
    # Invariant: i_term==(-1)^(i+1)*(x^i)/x
    # Invariant: ans==sum of first i-1 terms
    while(i<=n):# Termination: i increases n+1
        ans=ans+i_term # adding ith term to ans
        i_term=i_term*((-1)*x*i)/(i+1) # calculating next term
        i=i+1 # increasing the value of i
    return ans
    #
    # Time Complexity:
    #
    # for every iteration, 
    # number of arthematic operation performed is constant=8
    # total number of iterations = n
    # thus, time comlexity T(n)=8*n
    # therefore, time complexity is O(n)
#
# 5
# Taylor series computation of tan inverse of x upto n terms
#
def tan_inv(x,n):
#
# Input:
#    x: float : the number whose image is to be calculated
#    n>0 : int : number of terms of taylor series upto which the output is to be calculated
#
# Output: float : tan inverse x upto n terms of taylor series
#
    i=1 # keeps track of number of term
    i_term=1 # stores the ith term
    ans=0 # stores the sum of first (i-1) terms
    # we start with i=1 for 1st term
    # i_term = first term = 1
    # ans = sum of (i-1)=0 terms =0
    # Invariant: i_term==(-1)^(i+1)*(x^(2i-1))/(2i-1)
    # Invariant: ans==sum of first i-1 terms
    while(i<=n):# Termination: i increases n+1
        ans=ans+i_term # adding ith term to ans
        i_term=i_term*((-1)*x*x*(2*i-1))/(2*i+1) # calculating next term
        i=i+1 # increasing the value of i
    return ans
    #
    # Time Complexity:
    #
    # for every iteration, 
    # number of arthematic operation performed is constant=12
    # total number of iterations = n
    # thus, time comlexity T(n)=12*n
    # therefore, time complexity is O(n)
#
# Question 2
#
# Calculates root of a function f(x) in a given interval correct to the given tolerance
# here it is assumed that the function f(x) is continous and there is a root between the two values
#
def bisect(a,b,eps):
#
# Input:
#    a: float : lower limit of interval
#    b: float : upper limit of interval
#    eps: float : tolerance
#
# Input conditions:
#    a<b
#    eps>0
#    f(a)*f(b)<0
#
# Output: tuple : (Found,mid,list)
#    Found: boolean : True is a root is found
#    mid: float : the root
#    list: list of float : series of approximate results converging to mid
#
    if(not(f(a)*f(b)<0 and (a<b and eps>0))):# checking constraints
        return "Invalid Input"
# Initialisation
    mid=(a+b)/2 # stores the mid point of the interval
    Found=False # stores weather a root is found or not
    Inter_list=[] # stores list of approximate results
    # Invariant: f(a)f(b)<0
    # found == True implies |f(mid)| ≤ eps
    # and f has one root in interval [a,b]
    while((not(Found))and a<b):# Termination: a root is found or b-a decreases to tol(defined in question) as search interval halves after each iteration
        Inter_list.append(mid)# adding current approximation to list 
        if(abs(f(mid))<=eps):# checking if the current approximation is acceptable
            Found=True
        if(f(a)*f(mid)<0):# checking if the root is in the lower halve of interval
            b=mid
        if((f(b)*f(mid))<0):# checking if the root is in the upper halve of interval
            a=mid
        # the range of search becomes halve
        mid=(a+b)/2 # updating the value of mid
    return (Found,mid,Inter_list)
#
# the function whose root is to be approximated{ e^-x - sinx in this case}
#
import math
def f(x):
    return (math.exp(-1*x)-math.sin(x))
#
# Time Complexity:
#
# time complexcity of f(x) = 4(considering all operations take constant time)
# thus time complexity of f(x) is O(1)
#
# Time complexity of bisect(a,b,eps):
#    as given in question, it is assumed that the length of search interval is always greater than tol
#    as with each iteration the length of search interval is halved
#    the maximum number of iterations of the while loop= log(|b-a|/tol)/log2
#    the maximum number of operations that can performed in each iteration is 12+3c=z
#    where c is thge time complexity of f(x), here taken as 4
#    thus T(a,b)=z(log(|b-a|/tol))+1 (+1 from initilisation) 
#    T(a,b)=zlog|b-a|/log2 + k
#    thus the time complexity is O(log(b-a))
#
#
# Question 3
#
# 1
# Computation of coefficient of nth power of x in the Taylor series of e^x
#
def expn_coeff(n):
#
# Input:
#   n: int : the power of x whose coefficient is to be calculated
#
# Output: float : the coefficient of nth power of x in the Taylor series of e^x
#
    term=1 # coefficient of 0th power of x
    # Invariant: term= 1/i!
    for i in range(0,n): # Termination: i increases to n
        term/=(i+1) # (i+1)!=(i+1)*i!
    return term
#
# Time Complexity:
#
# Number of operations performed in each iteration= 3 (including increament and condition check)
# Total number of iterations= n
# Therefore Time complexity= 3n
# Thus the time complexity is O(n)
#
#
# 2
# Computation of coefficient of nth power of x in the Taylor series of cos x
#
def cosine_coeff(n):
#
# Input:
#   n: int : the power of x whose coefficient is to be calculated
#
# Output: float : the coefficient of nth power of x in the Taylor series of cos x
#
    if(n%2==0): #coefficient is non zero for even values of n 
        term=1 # coefficient of 0th power of x
        # Invariant: term=(-1)^(i+1)/2i!
        for i in range(0,(n//2)): # Termination: i increases to n/2
            term=term*(-1)/((2*i+1)*(2*i+2)) # (2(i+1))!=(2i+2)(2i+1)*(2i)!
        return term
    else: # coefficient is zero for odd values of n
        return 0
#
# Time Complexity:
#
# For maximum time taken we consider n even
# Number of operations performed in each iteration= 10 (including increament and condition check)
# Total number of iterations= n/2
# Therefore Time complexity= 5n + 1(for checking even or odd)
# Thus the time complexity is O(n)
#
#
# 3
# Computation of coefficient of nth power of x in the Taylor series of 1/(1-x) for |x|<1
#
def inverse_coeff(n):
#
# Input:
#   n: int : the power of x whose coefficient is to be calculated
#
# Output: float : the coefficient of nth power of x in the Taylor series of 1/(1-x)
#
    return 1 # coefficient is constant for all values of n
#
# Time Complexity:
#
# Number of operations performed=0
# Therefore Time complexity= some constant taken to return( Taken as 1 here)
# Thus the time complexity is O(1)
#
#
# 4
# Computation of coefficient of nth power of x in the Taylor series of ln x
#
def natural_log_coeff(n):
#
# Input:
#   n: int : the power of x whose coefficient is to be calculated
#
# Output: float : the coefficient of nth power of x in the Taylor series of ln x
#
    if(n%2==0): # coefficient is -1/n for even values
        return (-1)/n
    else:
        return 1/n # coefficient is 1/n for odd values
#
# Time Complexity:
#
# Number of operations performed=3
# therefore time complexity= 3
# Thus, time complexity is O(1)
#
#
# 5
# Computation of coefficient of nth power of x in the Taylor series of tan inverse x
#
def tan_inv_coeff(n):
#
# Input:
#   n: int : the power of x whose coefficient is to be calculated
#
# Output: float : the coefficient of nth power of x in the Taylor series of tan inv x
#
    if(n%2==0): # coefficient is 0 for even values of n
        return 0
    elif(((n-1)/2)%2==0):
        return 1/n # coefficient is 1/n when value of n is of the form 4k-3
    else:
        return (-1)/n # coefficient is -1/n when value of n is of the form 4k-1
#
# Time Complexity:
#
# For maximum time taken we take n=4k-3
# Number of operations performed=5
# therefore time complexity= 5
# Thus, time complexity is O(1)
#
#
# Question 4
#
# 1
# Computes the sum of Taylor series of e^x up to to nth power of x
#
def expn_t(x,n):
#
# Input:
#   x: float : the value whose image in the function is to be calculated
#   n: int : the power of x upto which the sum of Taylor series is to be calculated
#
# Output: float : the sum of Taylor series of e^x up to to nth power of x
#
    sum=0# stores sum initially 0
    t=1# x^0 initially
    # Invariant: sum=sum of Taylor series upto (i-1)th power of x
    # t=x^i
    for i in range(0,n+1): # Termination: i increases to n+1
        sum+=t*expn_coeff(i) # adding the ith term to sum
        t*=x # updating the value of t
    return sum
#
# Time Complexity:
#
# Time taken for each iteration= 5+T(expn_coeff)(i) = 5 + 3i
# As i varries from 0 to n,
# Time complexity= 5(n+1) + 3n(n+1)/2 = (3n+10)(n+1)/2
# Thus, Time complexity is O(n^2)
#
#
# 2
# Computes the sum of Taylor series of cos x up to to nth power of x
#
def cosine_t(x,n):
#
# Input:
#   x: float : the value whose image in the function is to be calculated
#   n: int : the power of x upto which the sum of Taylor series is to be calculated
#
# Output: float : the sum of Taylor series of cos x up to to nth power of x
#
    sum=0 # stores sum initially 0
    t=1 # x^0 initially
    # Invariant: sum= sum of taylor series upto (i-1)th power of x
    # Invariant: t=x^2i
    for i in range(0,n//2+1): # Termination: i increases to n//2+1
        sum+=t*cosine_coeff(2*i) # adding the term with x^2i
        t*=x*x # increasing the exponent by 2 as coefficient of odd powers is 0
    return sum
#
# Time Complexity:
#
# Time taken for each iteration= 7+T(cosine_coeff)(i) = 8+ 10i
# As i varries from 0 to n//2,(n//2 <= n/2)
# Time complexity= 4(n+2) + 5n(n+2)/4 = (5n/4+4)(n+2) +2
# Thus, Time complexity is O(n^2)
#
#
# 3
# Computes the sum of Taylor series of 1/(1-x) up to to nth power of x
#
def inverse_t(x,n):
#
# Input:
#   x: float : the value whose image in the function is to be calculated
#   n: int : the power of x upto which the sum of Taylor series is to be calculated
#
# Output: float : the sum of Taylor series of 1/(1-x) up to to nth power of x
#
    sum=0 # stores sum initially 0
    t=1 # x^0 initially
    # Invariant: sum= sum of taylor series upto(i-1)th power of x
    # Invariant: t=x^i
    for i in range(0,n+1): # Termination: i increases to n+1
        sum+=t*inverse_coeff(i)# Adding the ith power of x
        t*=x # updating the value of t
    return sum
#
# Time Complexity:
#
# Time taken for each iteration= 5+T(inverse_coeff)(i) = 6
# As i varries from 0 to n,
# Time complexity= 6(n+1) +1
# Thus, Time complexity is O(n)
#
#
# 4
# Computes the sum of Taylor series of ln x up to to nth power of x
# 
def natural_log_t(x,n):
#
# Input:
#   x: float : the value whose image in the function is to be calculated
#   n: int : the power of x upto which the sum of Taylor series is to be calculated
#
# Output: float : the sum of Taylor series of ln x up to to nth power of x
#
    sum=0 # stores sum initially 0
    t=x # initially x^1
    # Invariant: sum= sum of taylor series upto (i-1)th power of x
    # Invariant: t=x^i
    for i in range(1,n+1): # Termination: i increases to n+1
        sum+=t*natural_log_coeff(i) # adding the ith power to sum
        t*=x # updating the value of t
    return sum
#
# Time Complexity:
#
# Time taken for each iteration= 5+T(latural_log_coeff)(i) = 8
# As i varries from 1 to n,
# Time complexity= 8n +1
# Thus, Time complexity is O(n)
#
#
# 5
# Computes the sum of Taylor series of tan inv x up to to nth power of x
#
def tan_inv_t(x,n):
#
# Input:
#   x: float : the value whose image in the function is to be calculated
#   n: int : the power of x upto which the sum of Taylor series is to be calculated
#
# Output: float : the sum of Taylor series of tan inv x up to to nth power of x
#
    sum=0 # stores sum initially 0
    t=x # x^i initially
    # Invariant: sum= sum of taylor series upto(i-1)th power of x
    # Invariant: t=x^i
    for i in range(1,n+1): # Termination: i increases to n+1
        sum+=t*tan_inv_coeff(i) # Adding the ith power of x
        t*=x # updating the value of t
    return sum
#
# Time Complexity:
#
# Time taken for each iteration= 5+T(tan_inv_coeff)(i) = 10
# As i varries from 1 to n,
# Time complexity= 10n +1
# Thus, Time complexity is O(n)
#
#
#
# Question 5
#
# Here: f(x)= e^(-x)
#       g(x)= sin x
#
# a
# Computes the coefficient of nth power of x in the Taylor series of f(x)+g(x)
#
def add_coeff(n):
#
# Input:
# n: int : power of x whoese coefficient is calculated
#
# Output: float : coefficient of nth power of x in the Taylor series of f(x)+g(x)
#
    if(n%2==0): # for even values of n, coefficient of nth power of x are same for e^x and e^-x
        return expn_coeff(n)+inverse_coeff(n)
    else: # for odd values of n, coefficient of nth power of x for e^-x is negative of that for e^x
        return inverse_coeff(n)-expn_coeff(n)
#
# Time Complexity:
#
# Number of operations performed= 3 + T(expn_coeff)(n) + T(inverse_coeff)(n)
# Therefore, time complexity= 4 + 3n
# Thus, Time complexity is O(n)
#
#
# b
# Computes the coefficient of nth power of x in the Taylor series of f(x)*g(x)
#
def mul_coeff(n):
#
# Input:
# n: int : power of x whoese coefficient is calculated
#
# Output: float : coefficient of nth power of x in the Taylor series of f(x)*g(x)
#
    sum=0 # stores sum initally 0
    # Invariant sum= sum of coefficients of x^n in expn_t(x,j)*inverse_t(x,n-j) for 0<=j<i
    for i in range(0,n+1): # Termination: i increases to n+1
        if(i%2==0): # for even values of n, coefficient of nth power of x are same for e^x and e^-x
            sum+=(expn_coeff(i)*inverse_coeff(n-i))
        else: # for odd values of n, coefficient of nth power of x for e^-x is negative of that for e^x
            sum-=(expn_coeff(i)*inverse_coeff(n-i))
    return sum
#
# Time Complexity:
#
# Time taken for each iteration= 6+T(expn_coeff)(i)+T(inverse_coeff)(i) = 7+3i
# As i varries from 0 to n,
# Time complexity= 7(n+1) + 3n(n+1)/2 = (3n/2+7)(n+1)
# Thus, Time complexity is O(n^2)
#
#
# c
# Computes the coefficient of nth power of x in the Taylor series of d.f(x)/dx
#
def dif_coeff(n):
#
# Input:
# n: int : power of x whoese coefficient is calculated
#
# Output: float : coefficient of nth power of x in the Taylor series of d.f(x)/dx
#
    if(n%2==0): # for even values of n, coefficient of nth power of x for d.e^-x/dx is negative of that for e^x
        return (-1)*expn_coeff(n)
    else: # for odd values of n, coefficient of nth power of x are same for e^x and d.e^-x/dx
        return expn_coeff(n)
#
# Time Complexity:
#
# Number of operations performed= 3 + T(expn_coeff)(n) = 3 +3n
# Therefore time complexity= 3(n+1)
# Thus, time complexity is O(n)
#
#
# Question 6
#
# Computes the first order differential of a function fx(x) using the first principle
# upto a given tolerance eps
#
def limit_diff(x,eps):
#
# Input:
#   x: float : the value at which the differential is to be calculated
#   eps: float : tolerance upto which the differential is to be estimated
#
# Output: float : first order differential of fx(x) at x
#
    diff=fx(x+eps)-fx(x)
    return diff/eps # first principle
#
# Time Complexity:
#
# Number of operations performed= 3+T(fx)(x)
# Therefore, time complexity= k (where k is a constant)
# Thus, time complexity is O(1)
#
#
# The function whose first order differentila is to be calculated sinx * e^-x
#
def fx(x):
#
# Input:
#   x: float : value whose image in fx(x) is to be calculated
#
# Output: float : the image of x in fx(x)
    return expn(-1*x,20)*sine(x,20) # Taking upto 20 terms of each taylor series
#
# Time Complexity:
#
# Number of operations performed= 2+T(expn)(20) + T(sine)(20)
# Therefore, time complexity= k (where k is a constant)
# Thus, time complexity is O(1)
#
#
# Taylor series computation of sin x upto n terms
#
def sine(x,n):
#
# Input:
#    x: float : the number whose image is to be calculated
#    n>0 : int : number of terms of taylor series upto which the output is to be calculated
#
# Output: sin x upto n terms of taylor series
#
    i=1 # keeps track of number of term
    i_term=x # stores the ith term
    ans=0 # stores the sum of first (i-1) terms
    # we start with i=1 for 1st term
    # i_term = first term = x
    # ans = sum of (i-1)=0 terms =0
    while(i<=n):# Termination: i increases n+1
    # Invariant: i_term==(-1)^(i+1)*(x^(2i-1))/(2i-1)!
    # Invariant: ans==sum of first i-1 terms
        ans=ans+i_term # adding ith term to ans
        i_term=i_term*((-1)*x*x)/(2*i*(2*i+1)) # calculating next term
        i=i+1 # increasing the value of i
    return ans
    #
    # Time Complexity:
    #
    # for every iteration, 
    # number of arthematic operation performed is constant=11
    # total number of iterations = n
    # thus, time comlexity T(n)=11*n
    # therefore, time complexity is O(n)
#
#