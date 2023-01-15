#We start with and empty Data_list
Data_list=[]

#we define a helper function to check whether given input string is boolean   
def isboolean(x):
    if x=="True":
        return True
    elif x=="False":
        return False
    else:
        return -1
    
#we start with defining a function func_3 that deals with cases having 3 elements in set
#i.e. we deal with cases of form "x"=something
#here something can be integer, boolean or variable
def func_3(line):
    #first we run a loop to check if we already have a tuple for "x"
    n=len(Data_list)
    i=0
    #Initially set c to be -1
    c=-1
    while i<n:
        #first, check whether the element of the data list is a tuple or not
        if type(Data_list[i])==tuple:
            #if its a tuple check whether the first element is x
            if Data_list[i][0]==line[0]:
                #if we have a tuple for x at ith position that means i index
                c=i
                break
        #if i is found break otherwise continue the loop
        i+=1
    #now we take 3 cases
    #first case if "something" is an integer
    if line[2].isdigit():
        #now we check if that integer is already present in the list
        if int(line[2]) in Data_list:
            #if integer is present we find the index of that element
            index=Data_list.index(int(line[2]))          
        else:
            #otherwise, we first append that integer and then find the index
            Data_list.append(int(line[2]))
            index=Data_list.index(int(line[2]))
    
    #second case if "something" is boolean
    elif (isboolean(line[2])==True or isboolean(line[2])==False):
        #again we check if that's present in list or not and follow similar procedure
        if line[2] in Data_list:
            index=Data_list.index(isboolean(line[2]))
            
        else:
            Data_list.append(isboolean(line[2]))
            index=Data_list.index(isboolean(line[2]))        
    #third case if "something' is a variable eg x=y
    #here we need to find the tuple containing y and check for the index mentioned
    #then we go to that index element and find value of y
    else:
        i=0
        while i<n:
            if type(Data_list[i])==tuple:
                if Data_list[i][0]==line[2]:
                    index=Data_list[i][1]
            i+=1
    #if c=-1 i.e. initial case which means x is not found in any tuple
    #then we append a new tuple (x,index)
    if c==-1:
        Data_list.append((line[0],index))
    #otherwise we change the existing tuple to (x,index)
    else:
        Data_list[c]=(line[0],index)

#now we define a function func_4 that deals with cases having 4 elements in set
#i.e. we deal with cases of form "x"=(-)/not something
#here something can be integer, boolean or variable         
def func_4(line):
    #again same process to check whether x is present in a tuple or not
    n=len(Data_list)
    i=0
    c=-1
    while i<n:
        if type(Data_list[i])==tuple:
            if Data_list[i][0]==line[0]:
                c=i
                break
        i+=1
    #now we divide into 2 cases that 3rd element is "-" or "not"
    if line[2]=="not":
        #for "not" we further have 3 cases that sth is integer, boolean or variable
        #if its integer we call it a
        #we call b=not a
        #and follow similar process to check again if b is in list or not
        if line[3].isdigit():
            a=int(line[3])
            b=not(a)
            if b in Data_list:
                index=Data_list.index(b)
            else:
                Data_list.append(b)
                index=Data_list.index(b)
        #similarly for boolean we take 2 cases that sth is True o
        elif (isboolean(line[3])==True or isboolean(line[3])==False):
            if isboolean(line[3])==True:
                #x=False
                if False in Data_list:
                    index=Data_list.index(False)
                else:
                    Data_list.append(False)
                    index=Data_list.index(False) 
            else:
                #x=True
                if True in Data_list:
                    index=Data_list.index(True)
                else:
                    Data_list.append(True)
                    index=Data_list.index(True) 
        else:
            #x=not(y)
            i=0
            ind=-2
            while i<n:
                if type(Data_list[i])==tuple:
                    if Data_list[i][0]==line[3]:
                        ind=Data_list[i][1]
                        break
                i+=1
            if ind==-2:
                raise Exception('Error')
            else:
                x=Data_list[ind]
                if x.isdigit():
                    a=int(x)
                    b=not(a)
                    if b in Data_list:
                        index=Data_list.index(b)
                    else:
                        Data_list.append(b)
                        index=Data_list.index(b)
                elif (isboolean(x)==True or isboolean(x)==False):
                    if isboolean(x)==True:
                        #x=False
                        if False in Data_list:
                            index=Data_list.index(False)
                        else:
                            Data_list.append(False)
                            index=Data_list.index(False) 
                    else:
                        #x=True
                        if True in Data_list:
                            index=Data_list.index(True)
                        else:
                            Data_list.append(True)
                            index=Data_list.index(True) 
    elif line[2]=="-":
        if line[3].isdigit():
            if ((-1)*int(line[3])) in Data_list:
                index=Data_list.index(((-1)*int(line[3])))          
            else:
                Data_list.append(((-1)*int(line[3])))
                index=Data_list.index(((-1)*int(line[3])))
        else:
            i=0
            ind=-2
            while i<n:
                if type(Data_list[i])==tuple:
                    if Data_list[i][0]==line[3]:
                        ind=Data_list[i][1]
                        break
                i+=1
            if ind==-2:
                raise Exception("Error")
            else:
                x=Data_list[ind]
                if ((-1)*x) in Data_list:
                    index=Data_list.index((-1)*x)          
                else:
                    Data_list.append((-1)*x)
                    index=Data_list.index((-1)*x)   
    else:
        raise "Error"
    if c==-1:
        Data_list.append((line[0],index))
    else:
        Data_list[c]=(line[0],index)    
        
def func_5(line):
    #x=sth op sth
    n=len(Data_list)
    if line[2].isdigit():
        a=int(line[2])
        if a in Data_list:
            index=Data_list.index(a)
        else:
            Data_list.append(a)
    elif (isboolean(line[2])==True or isboolean(line[2])==False):
        a=isboolean(line[2])
        if a in Data_list:
            index=Data_list.index(a)
        else:
            Data_list.append(a)
    else:
        i=0
        while i<n:
            if type(Data_list[i])==tuple:
                if Data_list[i][0]==line[2]:
                    index=Data_list[i][1]
                    break
            i+=1
        a=Data_list[index]
        if a in Data_list:
            index=Data_list.index(a)
        else:
            Data_list.append(a)
    if line[4].isdigit():
        b=int(line[4])
        if b in Data_list:
            index=Data_list.index(b)
        else:
            Data_list.append(b)
    elif (isboolean(line[4])==True or isboolean(line[4])==False):
        b=isboolean(line[4])
        if b in Data_list:
            index=Data_list.index(b)
        else:
            Data_list.append(b)
    else:
        i=0
        while i<n:
            if type(Data_list[i])==tuple:
                if Data_list[i][0]==line[4]:
                    index=Data_list[i][1]
                    break
            i+=1
        b=Data_list[index]
        if b in Data_list:
            index=Data_list.index(b)
        else:
            Data_list.append(b)
    if line[3]=="+":
        y=a+b
    elif line[3]=="-":
        y=a-b
    elif line[3]=="*":
        y=a*b
    elif line[3]=="/":
        y=a//b
    elif line[3]==">":
        y=a>b
    elif line[3]=="<":
        y=a<b
    elif line[3]==">=":
        y=a>=b
    elif line[3]=="<=":
        y=a<=b
    elif line[3]=="==":
        y=a==b
    elif line[3]=="!=":
        y=a!=b
    elif line[3]=="and":
        y=(a and b)
    elif line[3]=="or":
        y=(a or b)
    else:
        raise Exception("Error")
    line_1=[line[0],"=",str(y)]
    func_3(line_1)
                    
def func(line):
    if len(line)==3:
        func_3(line)
#func_3  handles eqn of form x=value/variable
    elif len(line)==4:
        func_4(line)
#func_4 handles eqn of form x=(-)/not(value/variable)
    elif len(line)==5:
        func_5(line)
#func_5 handles eqn of form x=sth operator sth
    else:
        raise "Error"
            
lines = [] # initalise to empty list
with open('a.txt') as f:
    lines = f.readlines() # read all lines into a list of strings
for statement in lines: # each statement is on a separate line
    token_list = statement.split() # split a statement into a list of tokens
# now process each statement
    func(token_list)
    
print("The value of variables is found to be")   
n=len(Data_list)
i=0
while i<n:
    if type(Data_list[i])==tuple:
        index=Data_list[i][1]
        print(Data_list[i][0],"=",Data_list[index])
    i+=1

print("Garbage Values are")
L=[]
n=len(Data_list)
i=0
while i<n:
    if type(Data_list[i])==tuple:
        index=Data_list[i][1]
        L.append(Data_list[i])
        L.append(Data_list[index])
    i+=1    
S=set(Data_list)-set(L) 
print(list(S))
        


        



