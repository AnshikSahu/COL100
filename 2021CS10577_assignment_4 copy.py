def BS(S,e,l,h):
    if h>=l:
        m=(h+l)//2
        if S[m]==e:
            return True
        elif S[m]>e:
            return BS(S,e,l,m - 1)
        else:
            return BS(S,e,m+1,h)
    else:
        return False
def emptyset():
    return []
def isEmpty(S):
    return (S==[])
def member(S,e):
    n=len(S)-1
    return BS(S,e,0,n)
def singleton(x):
    return [x]
def isSubset(P,Q):
    c=True
    n=len(P)-1
    for e in P:
        if(not BS(Q,e,0,n)):
            c=False
            break
    return c
def setEqual(P,Q):
    n=len(P)
    m=len(Q)
    c=True
    if(n==m):
        P.sort()
        Q.sort()
        for i in range(0,n):
            if(P[i]!=Q[i]):
                c=False
                break
    else:
        c=False
    return c
def union(P,Q):
    n=len(P)-1
    for e in Q:
        if(not BS(P,e,0,n)):
            P.append(e)
    return P
def intersection(P,Q):
    c=emptyset()
    n=len(P)-1
    for e in Q:
        if(BS(P,e,0,n)):
            c.append(e)
    return c
def cartesian(P,Q):
    c=emptyset()
    for e in P:
        for el in Q:
            c.appens(e,el)
    return c
def power(P):
    if(len(P)==0):
        return [emptyset()]
    else:
        R=P[1:]
        S=power(R)
        Q=emptyset()
        T=power(R)
        Q=Q+T
        for e in S:
            e.append(P[0])
            Q.append(e)
        return Q
def emptyset_2():
    return []
def isEmpty_2(S):
    return (S==[])
def member_2(S,e):
    n=len(S)-1
    return BS(S,e,0,n)
def singleton_2(x):
    return [x]
def isSubset_2(P,Q):
    c=True
    n=len(P)-1
    for e in P:
        if(not BS(Q,e,0,n)):
            c=False
            break
    return c
def setEqual_2(P,Q):
    n=len(P)
    m=len(Q)
    c=True
    if(n==m):
        for i in range(0,n):
            if(P[i]!=Q[i]):
                c=False
                break
    else:
        c=False
    return c
def union_2(P,Q):
    n=len(P)
    m=len(Q)
    R=emptyset()
    i=0
    j=0
    while i<n and j<m:
        if P[i]<Q[j]:
            R.append(P[i])
            i += 1
        else:
            if(P[i]==Q[j]):
                i+=1
            R.append(Q[j])
            j += 1
    R=R+P[i:]+Q[j:]
    return R
def intersection_2(P,Q):
    c=emptyset()
    n=len(P)-1
    for e in Q:
        if(BS(P,e,0,n)):
            c.append(e)
def cartesian_2(P,Q):
    c=emptyset()
    for e in P:
        for el in Q:
            c.appens(e,el)
    return c
def power_2(P):
    if(len(P)==1):
        return([[],P])
    else:
        T=power_2(P[1:])
        R=power_2(P[1:])
        Q=[[]]
        for e in T:
            e=[P[0]]+e
            Q.append(e)
        Q=Q+R[1:]
        return Q