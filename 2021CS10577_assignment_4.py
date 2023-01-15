#
# COL100 Assignment 4
#
# Note: In this code, sets are represented as lists, and thus the terms are treated as interchangeable
#
# Checks if an element is present in a sorted list using binary search
#
def BS(S,e,l,h):
#
# Input:
#   S: The list in which the search has to be performed
#   e: The element which is to be searched
#   l: lower limit of search
#   h: higher limit of search
#
# Output: boolean: False if the element is not in the list and true if the element is found
#
    if h>=l:# checking if there are any index left to search at
        m=(h+l)//2
        if S[m]==e:# checking if elementisat middle index
            return True
        elif S[m]>e:
            return BS(S,e,l,m - 1)# searching in the upper half
        else:
            return BS(S,e,m+1,h)# searching in the lower half
    else:
        return False
#
# Time complexity
#
# For each recursion the range of search is halved, therefore
# T(n)=T(n//2) + 5
# taking n=2^k we get,
# T(k)=T(k-1) + 5
# as T(0)=1
# by induction, T(k)= 5k + 1
# as k=log(n)/log(2)
# T(n)= 5log(n) + 1
# Thus, time complexity is O(log(n))
#
#
# Part 1
#
#
# Returns an empty list
#
def emptyset():
#
# Input: None
#
# Output: list : Empty list
#
    return []
#
# Time Complexity
#
# As there are no operations performed in this function
# T(n)=c (some time taken by the system)
# Thus, the time complexity is O(1)
#
#
# Checks if a give list is empty
#
def isEmpty(S):
#
# Input: list: the list that is to be checked
#
# Output: boolean: True if there are no elements in the list and False if the list is not empty
# 
    return (S==[])
#
# Time Complexity
#
# As the number of operations performed= 1
# T(n)=1
# Thus, the time complexity is O(1)
#
#
# Checks if an element is present in the list or not
#
def member(S,e):
#
# Input:
#   S: list: The list in which the search is to be performed
#   e: The element to be searched
#
# Output: boolean : True if the element is presaent in the list else False
    for el in S:
        if(el==e):
            return True
    return False
#
# Time Complexity
#
# Number of operations performed in each iteration= 1
# number of iterations=n
# therefore, T(n)= n
# Thus, the time complexity is O(n)
#
#
# Returns a singleton set with gien value as the only element
#
def singleton(x):
#
# Input: element of the singleton set
#
# Output: list: list with input as the only element in it
#
    A=emptyset()
    A.append(x)
    return A
#
# Time Complexity
#
# Number of operations performed=2
# Therefore, T(n)=2
# Thus, the time complexity is O(1)
#
#
# Checks if the first set is a subset of the second set
#
def isSubset(P,Q):
# Input
#   P: list : possible subset
#   Q: list : set which is to be checked for subset
#
# Output: boolean: True if P is a subset of Q else False
#
    c=True # stores if P is a subset or not, initially true for empty P
    for e in P:
        if(not member(Q,e)):# Checking if any element of P is not present in Q
            c=False
            break
    return c
#
# Time Complexity
#
# Number of operations performed in each iteration= 2 + T(member)(n)
# Number of iterations=m
# Therefore, T(m,n)=mn + 2m
# Thus, the time complexity is O(mn)
#
#
# Checks if two sets are equal
#
def setEqual(P,Q):
#
# Input:
#   P: list : First set
#   Q: list : Second set
#
# Output: boolean: True if Pand Q are equal else False
#
    m=len(P)
    n=len(Q)
    if(n==m):
        if(isSubset(P,Q)):
            return True
    return False
#
# Time Complexity
#
# Number of operations performed= 4+T(isSubset)(n,n)
# Therefore, T(n)= n^2+ 2n +4
# Thus, the time complexity is O(n^2)
#
#
# Computes the union of two sets
#
def union(P,Q):
#
# Input:
#   P: list : First set
#   Q: list : Second set
#
# Output: list: union set of P and Q
#
    for e in Q:
        if(not member(P,e)):# avoiding repetition
            P.append(e)
    return P
#
# Time Complexity
#
# Number of operations performed in each iteration= 3+T(member)(m)
# Number of iterations=n
# Therefore, T(m,n)= mn + 3n
# Thus, the time complexity is O(mn)
#
#
# Computes the intersection of two sets
#
def intersection(P,Q):
#
# Input:
#   P: list : First set
#   Q: list : Second set
#
# Output: list: the intersection of set P and Q
#
    c=emptyset()
    for e in Q:
        if(member(P,e)):# check if current element of Q is present in P
            c.append(e)
    return c
#
# Time Complexity
#
# Number of operations performed in each iteration= 2+T(member)(m)
# Number of iterations=n
# Therefore, T(m,n)= mn + 2n
# Thus, the time complexity is O(mn)
#
#
# Calculates the cartesian product of two sets
#
def cartesian(P,Q):
#
# Input:
#   P: First set
#   Q: Second set
#
# Output: list of tuples: {(a,b): a is an element of P and b is an element of Q}
#
    c=emptyset()
    for e in P:# going through all elements of P
        for el in Q:# going through all elements of Q
            c.append((e,el))
    return c
#
# Time Complexity
#
# Number of operations performed in each iteration of inner loop= 1
# Number of iterations of inner loop= n
# Therefore, number of operations performed in each iteration of outer loop= n
# Number of terations of outer loop= m
# Therefore, T(m,n)= mn
# Thus, the time complexity is O(mn) {or O(n^2)}
#
#
# Returns all possible subsets of a set
#
def power(P):
#
# Input: P: list: Set whose subsets are to be found
#
# Output: list:{x: x is a subset of P}
#
    if(isEmpty(P)):# checking if P is empty
        return singleton(emptyset())
    else:
        R=P[1:]# list containg all elements of a except that at index 0
        S=power(R) # list of subsets of P which do not contain element at index 0
        Q=emptyset() # contains all subsets of P( initially empty)
        T=power(R)# list of subsets of P which do not contain element at index 0
        Q=Q+T # adding subsets which do not contain first element
        for e in S: # adding subsets which contain first element
            e.append(P[0])
            Q.append(e)
        return Q
#
# Time Complexity
#
# As ther number of subsets of a set with n elements in it= 2^n
# For each recursion number of operations perfomed is the sum of:
#   2*T(n-1) ( computing S and T)
#   2^n {2^(n-1) iterations of the loop}
#   2^(n-1) {adding Q and T}
#   n-1 {for computing R}
#   1 {condition check}
# Therefore, T(n)= 2*T(n-1)+3*2^(n-1)+n
# As T(0)=1, by Induction
# T(n)= 3n*2^(n-1) + n(n+1)/2 + 1
# Thus, the time complexity is O(n*2^n)
#
#
# Part 2
#
#
# Returns an empty list
#
def emptyset_2():
#
# Input: None
#
# Output: list : Empty list
#
    return []
#
# Time Complexity
#
# As there are no operations performed in this function
# T(n)=c (some time taken by the system)
# Thus, the time complexity is O(1)
#
#
# Checks if a give list is empty
#
def isEmpty_2(S):
#
# Input: list: the list that is to be checked
#
# Output: boolean: True if there are no elements in the list and False if the list is not empty
# 
    return (S==[])
#
# Time Complexity
#
# As the number of operations performed= 1
# T(n)=1
# Thus, the time complexity is O(1)
#
#
# Checks if an element is present in the list or not
#
def member_2(S,e):
#
# Input:
#   S: list: The list in which the search is to be performed
#   e: The element to be searched
#
# Output: boolean : True if the element is presaent in the list else False
    n=len(S)-1 # calculating the highest index in the list
    return BS(S,e,0,n)
#
# Time Complexity
#
# Number of operations performed= 2+T(BS)(n)
# therefore, T(n)= 5log(n) + 3
# Thus, the time complexity is O(log(n))
#
#
# Returns a singleton set with gien value as the only element
#
def singleton_2(x):
#
# Input: element of the singleton set
#
# Output: list: list with input as the only element in it
#
    A=emptyset_2()
    A.append(x)
    return A
#
# Time Complexity
#
# Number of operations performed= 1 + T(emptyset_2)(n)
# Therefore, T(n)=2
# Thus, the time complexity is O(1)
#
#
# Checks if the first set is a subset of the second set and their elements follow the same order
#
def isSubset_2(P,Q):
# Input
#   P: list : possible subset
#   Q: list : set which is to be checked for subset
#
# Output: boolean: True if P is a subset and its elements are arranged in the same order of Q else False
#
     for e in P:
         if(not member_2(Q,e)):# Checking if any element of P is not present in Q
             return False
     return True
#
# Time Complexity
#
# Number of operations performed in each iteration= 2 + T(BS)(n)
# Number of iterations=m
# Therefore, T(m,n)=5mlog(n) + 3m
# Thus, the time complexity is O(mlog(n)) {or O(nlog(n))}   
#
#
# Checks if two sets are equal{have same elements in same order}
#
def setEqual_2(P,Q):
#
# Input:
#   P: list : First set
#   Q: list : Second set
#
# Output: boolean: True if Pand Q are equal else False
#
        m=len(P) # number of items in P
        n=len(Q) # number of items in Q
        if(n==m):
            for i in range(0,n):# Termination: i increases to n
                if(P[i]!=Q[i]):# checking if both contain the same element at the same index
                    return False
            return True
        else:
            return False
#
# Time Complexity
#
# Number of operations performed in each iteration= 2
# Number of iterations=n
# Therefore, T(n)= 2n + 2
# Thus, the time complexity is O(n)
#
#
# Computes the union of two sets while maintaining the order of elements
#
def union_2(P,Q):
#
# Input:
#   P: list : First set
#   Q: list : Second set
#
# Output: list: union set of P and Q
#
     m=len(P)# number of items in P
     n=len(Q)# number of items in Q
     R=emptyset_2()# stores union, initially empty
     i=0
     j=0
     while i<n and j<m:# Termination i increases to m or j increases to n
         if P[i]<Q[j]:# checking if ith element of P is to be added
             R.append(P[i])# adding ith element of P to R
             i += 1# updating the value of i
         else:# checking if jth element of Q is to be added
             if(P[i]==Q[j]):# adding jth element of Q to R
                 i+=1# updating the value of i
             R.append(Q[j])
             j += 1# updating the value of j
     R=R+P[i:]+Q[j:]# adding the remaining elements of both lists
     return R
#
# Time Complexity
#
# Number of operations performed in each iterations=7 (at max)
# Number of iterations=2min(m,n)
# Therefore, T(m,n)= 14min(m,n)+1 + m+n <= 8(m+n) + 1
# Thus, the time complexity is O(m+n) {or O(n) where n is max(m,n)}
#
#
# Computes the intersection of two sets and returns set with elements in order
#
def intersection_2(P,Q):
#
# Input:
#   P: list : First set
#   Q: list : Second set
#
# Output: list: the intersection of set P and Q
#
    c=emptyset()
    for e in Q:
        if(member_2(P,e)):# check if current element of Q is present in P
            c.append(e)
    return c
#
# Time Complexity
#
# Number of operations performed= 2+T(member_2)(m)
# Number of iterations=n
# Therefore, T(m,n)= 5nlog(m) + 3n
# Thus, the time complexity is O(nlog(m)) {or O(nlog(n))}
#
#
# Calculates the cartesian product of two ordered sets
#
def cartesian_2(P,Q):
#
# Input:
#   P: First set
#   Q: Second set
#
# Output: list of tuples: {(a,b): a is an element of P and b is an element of Q}
#
    c=emptyset_2()
    for e in P:# going through all elements of P
        for el in Q:# going through all elements of Q
            c.append((e,el))
    return c
#
# Time Complexity
#
# Number of operations performed in each iteration of inner loop= 1
# Number of iterations of inner loop= n
# Therefore, number of operations performed in each iteration of outer loop= n
# Number of terations of outer loop= m
# Therefore, T(m,n)= mn
# Thus, the time complexity is O(mn) {or O(n^2)}
#
#
# helper function for power_2(returns subsets with elements of subsets in reverse order)
#
def power_(P):
#
# Input: P: list: Set whose subsets are to be found
#
# Output: list:{rev(x): x is a subset of P with and x!=[]}
#
    if(isEmpty_2(P)):# checking if P is empty
        return [[]]
    else:
        S=P[1:]
        T=power_(S)# list of subsets of P which do not contain element at index 0 and []
        R=power_(S)# list of subsets of P which do not contain element at index 0
        Q=singleton_2(emptyset_2()) # contains all subsets of P initially empty
        for e in T: # adding subsets which contain first element to Q
            e.append(P[0])
            Q.append(e)
        Q=Q+R[1:] # adding subsets that do not contain the first element to Q
        return Q
#
# Time Complexity
#
# As ther number of subsets of a set with n elements in it= 2^n
# For each recursion number of operations perfomed is the sum of:
#   2*T(n-1) ( computing R and T)
#   2^n {2^(n-1) iterations of the loop}
#   2^(n-1) {computing R[1:]}
#   2^n {adding Q and R[1:]}
#   n-1 {computing S}
#   2 {condition check+ initialising Q}
# Therefore, T(n)= 2*T(n-1)+5*2^(n-1)+n-3
# As T(1)=1, by Induction
# T(n)= 5n*2^(n-1) + n(n-5)/2 + 3
# Thus, the time complexity is O(n*2^n)
#
#
# helper function for power_2(reverses the elements of a given list)
#
def rev(l):
    Q=[]
    n=len(l)
    i=1
    while(i<=n):
        Q.append(l[n-i])
        i+=1
    return Q
#
# Time Complexity
#
# number of operations in each iterations=3
# number of iterations=n
# therefore T(n)=3n+1
# Thus, Time complexity is O(n)
#
#
# Computes subsets of ordered list and arranges them in order
#
def power_2(P):
    R=power_(P)
    Q=[]
    for e in R:
        Q.append(rev(e))
    return Q
#
# Time complexity
#
# for the loop,
#   number of operations in each iterations=T(rev)(len(e))
#   number of iterations=2^n
# Thus time taken by loop=n*2^(n-1)
# T(n)=T(power_)(n) + T(loop)(n)
# Therefore, T(n)=3n*2^n + n(n-5)/2 + 3
# Thus time complexity is O(n*2^n)
#
#