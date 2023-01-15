# 
# Assignment 5
#
data=[]# stores all data
used=[]# will store indices of used values at the end
garbage=[]# will store garbage values at the end
#
# computes the index at which a variable is stored
#
def index_of_variable(x):
#
# Input: x: string: a variable whose index is to be found
#
# Output: int: index at which x is stored in data and -1 if x is not present
#
    c=-1
    # Invariant: c=-1 until variable is found
    for i in range(0,len(data)):# Termination: i increases to len(data)
        if(type(data[i])==tuple):# searching for tuples as variables are stored as tuples
            if(data[i][0]==x):# checking if the variable name is same
                c=i
                break
    return c# -1 is returned if x is not present
#
#
# computes the index at which a value is stored in data
#
def index_of_value(x):
#
# Input: x: the value whose index is to be found
#
# Output: int: the index of x in data if present and -1 if not present
#
    c=-1
    # Invariant: c=-1 until the value is found
    for i in range(0,len(data)):# Termination: i increases to len(data)
        if(type(data[i])!=tuple):# checking if currend element is a value
            if(type(data[i])== bool or type(x)== bool):
                if(data[i]==x and type(data[i])==type(x)):
                    c=i
                    break
            elif(data[i] == x):# checking if the value is same
                c=i
                break
    return c# -1 is returned if x is not present
#
#
# Inserts a value in data if not present already
#
def insert(x):
    if(index_of_value(x)==-1):# checking if not present
        data.append(x)
#
#
# Returns the value represented by a string; if the string represents a variable name, then
# the value stored for the variable
#
def value(x):
#
# Input: x : string: the value or variable name as string
# 
# Output: tuple of two values: the value associated with the string and its data type 
#   
    if(x.strip("-").isdigit()):#checking if it is integer
        insert(int(x))# inserting value in data if not present
        return (int(x),"int")
    elif(x.replace(".","",1).strip("-").isdigit()):#checking if it is fraction
        insert(float(x))# inserting value in data if not present
        return (float(x),"float")
    elif(x=="True"):#checking if it is True
        insert(True)# inserting value in data if not present
        return (True,"boolean")
    elif(x=="False"):#checking if it is False
        insert(False)# inserting value in data if not present
        return (False,"boolean")
    else:# else it is a variable name
        i=index_of_variable(x)
        if(i<0):# checking if the varrible is not present in the list
            raise Exception("variable "+x+" not initialised")
        return value(str(data[data[i][1]]))
#
#
# evaluates the equations of type variable = term
#
def assign(a,b):
# 
# Input:
#   a: string: Name of variable to which value is to be assigned
#   b: string: the value or the variable whose value is to be assigned to a
#
    if(a.replace(".","",1).strip("-").isdigit() or a=="True" or a=="False"):
        # checking validity of the variable name
        raise Exception("Invalid variable name: "+a)
    x=value(b)[0]# the value to be assigned
    y=index_of_value(x)# index at which the value is stored
    if(y==-1):# checking if value is not present in data
        data.append(x)
        y=len(data)-1
    p=index_of_variable(a)# index at which the variable exists
    if(p==-1):# checking if the variable name is not present in data
        data.append((a,y))
    else:
        data[p]=(a,y)# updating the refrence
#
#
# evaluates the equations of the form: (unary operator) term
#
def unary(a,b):
#
# Input:
#   a: string: The unary operator("-" or "not")
#   b: string: The value or variable on which operator a has to operate
#
# Output: string: the value obtained after evaluation of the equation
#
    if(a=="-"):# checking if the operator is a "-"
        return str(-(value(b)[0]))
    elif(a=="not"):# checking if the operator is a "not"
        return str(not(value(b)[0]))
    else:# unrecognised operator
        raise Exception("Invalid unary operator: "+a)
#
#
# checks if a variable is a member of a given list
#
def member(L,x):
#
# Input:
#   x: the variable that has to be searched for
#   L: the list that is to be searched for x
#
# Output: int: the index of x in L if found else -1
#
    c=-1
    # Invariant: c=-1 until x is found
    for i in range(0,len(L)):# Termination: i increases to len(L)
        if(L[i]==x):# checking if x is present
            c=i
            break
    return c# -1 is returned if not found
#
#
# evaluates the equations of the form: term (binary operator) term......
#
def binary(L):
#
# Input: L: List representing the expression to be evaluated
#
# Output: string: the value computed by evaluating the expression
#
    if(len(L)==1):
        return L[0]
    x=value(L[0])[0]# the value of first operand
    y=value(binary(L[2:]))[0]# the value of second operand
    b=L[1]
    if(b=="+"):# checking if the operator is a "+"
        r=x+y
    elif(b=="-"):# checking if the operator is a "-"
        r=x-y
    elif(b=="*"):# checking if the operator is a "*"
        r=x*y
    elif(b=="/"):# checking if the operator is a "/"
        r=x/y
    elif(b==">"):# checking if the operator is a ">"
        r=x>y
    elif(b=="<"):# checking if the operator is a "<"
        r=x<y
    elif(b=="<="):# checking if the operator is a "<="
        r=x<=y
    elif(b==">="):# checking if the operator is a ">="
        r=x>=y
    elif(b=="=="):# checking if the operator is a "=="
        r=x==y
    elif(b=="!="):# checking if the operator is a "!="
        r=x!=y
    elif(b=="and"):# checking if the operator is a "and"
        r=x and y
    elif(b=="or"):# checking if the operator is a "or"
        r=x or y
    elif(b=="%"):# checking if the operator is a "%"
        r=x%y
    else:# unrecognised operator
        raise Exception("Invalid binary operator: "+b)
    return str(r)
#
#
# evaluates conditional(if-else) statements
#
def conditional(L):# not a part of the assignment
#
# Input: L: list: the list representing the statement containing the conditional expression
#
    i=member(L,"=>")# index of "=>"
    j=member(L,"|")# index of "|"
    r="False"# initially the condition is considered false
    if(i==1):# checking the type of condition
        r=str(value(L[0])[0])
    elif(i==2):# checking the type of condition
        r=unary(L[0],L[1])
    elif(i==3):# checking the type of condition
        r=binary(L[0:3])
    else:# unrecognised condition type
        raise Exception("Invalid condition")
    if(r=="True"):# evaluation the if block
        if(j>4):
            evaluate(L[i+1:j])
        else:
            evaluate(L[i+1:])
    elif(r=="False"):# evaluating the else block
        if(j<5 and len(L)>9):
            raise Exception("Invalid statement")
        if(j>4):
            evaluate(L[j+1:])
    else:# condition not valid
        raise Exception("Invalid condition")
#
#
# evaluates print statements
#
def output(L):# not a part of the assignment
#
# Input: L: list: the list representing the statement containing the conditional expression
#
    j=member(L,"@")# index of "@"
    if(j==-1):# checking if variable name is not present
        print(L[6:])
    else:# variable name present
        x=value(L[j+2:])[0]# value of variable
        print(L[6:j-1]+str(x))
#
#
# decides the type of equation and allocates it to respective functions
#
def evaluate(L):
#
# Input: L: list: the statement represented as a list
#
    x=len(L)
    c=0# becomes 1 if assignment is required at the end
    if(x==3 and L[1]=="="):# checking if the statement is an assignment equation
        r=L[2]
        c=1
    elif(x==4 and L[1]=="="):# checking if the statement is an unary equation
        r=unary(L[2],L[3])
        c=1
    elif(L[1]=="=" and x==5):# checking if the statement is an binary equation
        r=binary(L[2:])
        c=1
#    elif(member(L,"=>")>0 and member(L,"=>")<4 and x>4):# checking if the statement is an conditional equation
#        conditional(L)
    else:# unrecognised equation type
        raise Exception("Invalid statement: ",L)
    if(c==1):
        assign(L[0],r)# assigning the result to the variable
#
#
# Prints the values of all variables and also keeps track of the value references in use 
#
def value_of_variables():
    c=0# remains 0 if no variables are present
    print("Values of variables are:")
    # Invarriant: c=0 if no variable found
    for i in range(0,len(data)):# Termination: i increases to len(data)
        if(type(data[i])==tuple):# checkinh for variables
            print(data[i][0]+"="+str(data[data[i][1]]))
            c=1
            used.append(data[i][1])# adding the refrence to the used list
    if(c==0):# checking if no variables are present
        print("No variables present")
#
#
# checks if a given index is being used or not
#
def index_in_use(a):
#
# Input: a: int: the index that is to be searched for
#
# Output: boolean: True if a is present in used else False
#
    c=False
    # Invarriant: c remains False until a is found
    for e in used:
        if(e==a):
            c=True
            break
    return c
#
#
# Adds the unused values to the garbage list
#
def unused():
    for i in range(0,len(data)):# Termination: i increases to len(data)
        if(not(type(data[i])==tuple)):# checking for values
            if(not(index_in_use(i))):# checking if the value is not in use
                garbage.append(data[i])
#
#
lines = [] # initalise to empty list
with open('input_file.txt') as f:
    lines = f.readlines() # read all lines into a list of strings
for statement in lines: # each statement is on a separate line
#    if(statement[0]!="#"):# checking if the statement is a not a comment
#        if(statement[0:5]=="print"):# checking if the statement is a print statement
#            output(statement)
#        else:
    token_list = statement.split() # split a statement into a list of tokens
    evaluate(token_list)# now process each statement
value_of_variables()# printing the values of variables
unused()# adding the garbage values to garbage list
if(len(garbage)):# checking if garbage is present or not
    print("Garbage values: ",garbage)
else:
    print("No garbage")
#