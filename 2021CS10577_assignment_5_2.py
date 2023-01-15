import sys
data=[]# stores all data
instructions=[]# stores the instructions
branch=[]# stores the index at which open loops are present
used=[]# will store indices of used values at the end
garbage=[]# will store garbage values at the end
#
class Instructions:# each object of the class represents an equivalent instruction
    #
    #
    instruction=[]# stores the instruction
    #
    #
    # computes the index at which a variable is stored
    #
    def index_of_variable(self,x):
    #
    # Input: 
    #   x: string: a variable whose index is to be found
    #   self: object: reference of the current object
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
    # Time complexity
    # Number of iterations of loop = n = len(data)
    # thus time complexity is T(n)=3n+2
    # therefore time complexity is O(n)
    #
    #
    # computes the index at which a value is stored in data
    #
    def index_of_value(self,x):
    #
    # Input: 
    #    x: the value whose index is to be found
    #   self: object : refrence of current object
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
    # Time complexity
    # Number of iterations of loop = n = len(data)
    # thus time complexity is T(n)=3n+2
    # therefore time complexity is O(n)
    #
    #
    # Inserts a value in data if not present already
    #
    def insert(self,x):
    #
    # Input:
    #   self: object: reference of the current object
    #   x: the value to be searched in data
    #
        if(self.index_of_value(x)==-1):# checking if not present
            data.append(x)
    #
    #
    # Time complexity
    # if n = len(data)
    # thus time complexity is T(n)=3n+4
    # therefore time complexity is O(n)
    #
    #
    # Returns the value represented by a string; if the string represents a variable name, then
    # the value stored for the variable
    #
    def value(self,x):
    #
    # Input: 
    #   x : string: the value or variable name as string
    #   self: object: reference of the current object
    # 
    # Output: tuple of two values: the value associated with the string and its data type 
    #   
        
        if(x.strip("-").isdigit()):#checking if it is integer
            self.insert(int(x))# inserting value in data if not present
            return (int(x),"int")
        elif(x.replace(".","",1).strip("-").isdigit()):#checking if it is fraction
            self.insert(float(x))# inserting value in data if not present
            return (float(x),"float")
        elif(x=="True"):#checking if it is True
            self.insert(True)# inserting value in data if not present
            return (True,"boolean")
        elif(x=="False"):#checking if it is False
            self.insert(False)# inserting value in data if not present
            return (False,"boolean")
        else:# else it is a variable name
            i=self.index_of_variable(x)
            if(i<0):# checking if the varrible is not present in the list
                print("variable "+x+" not initialised")
                sys.exit()
            return self.value(str(data[data[i][1]]))
    #
    #
    # Time complexity
    # if n = len(data)
    # maximum time complexity is T(n)=4n+10
    # therefore time complexity is O(n)
    #
    #
    # evaluates the equations of type variable = term
    #
    def assign(self,a,b):
    # 
    # Input:
    #   a: string: Name of variable to which value is to be assigned
    #   b: string: the value or the variable whose value is to be assigned to a
    #   self: object: reference of the current object
    #
        
        if(a.replace(".","",1).strip("-").isdigit() or a=="True" or a=="False"):
            # checking validity of the variable name
            print("Invalid variable name: "+a)
            sys.exit()
        x=self.value(b)[0]# the value to be assigned
        y=self.index_of_value(x)# index at which the value is stored
        if(y==-1):# checking if value is not present in data
            data.append(x)
            y=len(data)-1
        p=self.index_of_variable(a)# index at which the variable exists
        if(p==-1):# checking if the variable name is not present in data
            data.append((a,y))
        else:
            data[p]=(a,y)# updating the refrence
    #
    #
    # Time complexity
    # if n = len(data)
    # tmaximum time complexity is T(n)=10n+25
    # therefore time complexity is O(n)
    # therefore time complexity is O(n)
    #
    #
    # evaluates the equations of the form: (unary operator) term
    #
    def unary(self,a,b):
    #
    # Input:
    #   a: string: The unary operator("-" or "not")
    #   b: string: The value or variable on which operator a has to operate
    #   self: object : refrence of current object
    #
    # Output: string: the value obtained after evaluation of the equation
    #
        if(a=="-"):# checking if the operator is a "-"
            return str(-(self.value(b)[0]))
        elif(a=="not"):# checking if the operator is a "not"
            return str(not(self.value(b)[0]))
        else:# unrecognised operator
            print("Invalid unary operator: "+a)
            sys.exit()
    #
    #
    # Time complexity
    # if n = len(data)
    # thus time complexity is T(n)=3n+4
    # therefore time complexity is O(n)
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
    # Time complexity
    # Number of iterations of loop = n = len(data)
    # thus time complexity is T(n)=3n+5
    # therefore time complexity is O(n)
    #
    #
    # evaluates an expression
    #
    def expression(self,L):
    #
    # Input:
    #   L: List representing the expression to be evaluated
    #   self: object: reference of the current object
    #
    # Output: string: the value computed by evaluating the expression
    #
        if(len(L)==1):# cheking if there is no operation to perform
            return L[0]
        if(len(L)==2):# checking if the expression is unary
            return self.unary(L[0],L[1])
        x=self.value(L[0])[0]# the value of first operand
        y=self.value(self.expression(L[2:]))[0]# the value of second operand
        b=L[1]
        if(b=="+"):# checking if the operator is a "+"
            r=x+y
        elif(b=="-" or b=="−"):# checking if the operator is a "-"
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
            print("Invalid binary operator: "+b)
            sys.exit()
        return str(r)
    #
    #
    # Time complexity
    # tmaximum time complexity is T(n)= 6n+30
    # therefore time complexity is O(n)
    #
    # evaluates an equation
    #
    def equation(self,L):
    #
    # Input:
    #   L: list: the statement represented as a list
    #   self: object: reference of the current object
    #
        x=len(L)
        if(x<6 and L[1]=="="):
            r=self.expression(L[2:])
        else:# unrecognised equation type
            print("Invalid statement: ",L)
            sys.exit()
        self.assign(L[0],r)# assigning the result to the variable
    #
    #
    # Time complexity
    # Number of iterations of loop = n = len(data)
    # maximum time complexity is T(n)=16n+58
    # therefore time complexity is O(n)
    #
    #
    # Converts input parameters into instruction
    #
    def backward(self):
    #
    # Input: self: object: the current object
    #
    # Output: list: the equivalent instruction
    #
        if(self.type=="Equation"):
            if(self.sign==None):
                return [self.address,"=",self.a]
            elif(self.a==None):
                return [self.address,"=",self.sign,self.b]
            else:
                return [self.address,"=",self.a,self.sign,self.b]
        elif(self.type=="branch"):
            return [self.type,self.address]
        else:# the instruction defines a loop
            return [self.type,self.a,self.b,self.address]
    #
    #
    # Time Complexity:
    # Time complexity = maximum number of operations performed= 4
    # Thus, time complexity is O(1)
    #
    #
    # Constructor for class initialises lines and tabs
    #
    def __init__(self,type="Equation",a=0,operator="+",b="0",address=None):
    #
    # Input: 
    #   self: object: reference of the current object
    #   lines: list of strings: the list containing each line
    #   tabs: list of integers: a list containing the number of tabs before each line
    #
        self.type=type
        self.a=a
        self.b=b
        self.sign=operator
        self.address=address
        self.instruction=self.backward()# converting input parameters to instruction
    #
    #
    # Time Complexity:
    # Time complexity = number of operations performed= 6 + T(backward) = 10
    # Thus, time complexity is O(1)
    #
    #
    # executed the instructions
    #
    def execute(self,i):
    #
    # Input: self: object: reference of the current object
    #
    # Output: int: the index of the next instruction to be executed
    #
        command=self.instruction# the current instruction
        if(command[0]=="BLE"):# checking for loop definition with not(<=)
            if("True"==(self.expression([command[1],"<=",command[2]]))):
                i=command[3]# skiping the loop if condition in instruction is true
            else:
                i=i+1# updating the value of i
        elif(command[0]=="BL"):# checking for loop definition with not(<)
            if("True"==(self.expression([command[1],"<",command[2]]))):
                i=command[3]# skiping the loop if condition in instruction is true
            else:
                i=i+1# updating the value of i
        elif(command[0]=="BE"):# checking for loop definition with not(==)
            if("True"==(self.expression([command[1],"==",command[2]]))):
                i=command[3]# skiping the loop if condition in instruction is true
            else:
                i=i+1# updating the value of i
        elif(command[0]=="branch"):# checking for loop definition representing end of branch
            i=command[1]# going back to the begining of the loop
        else:# the instruction represents an equation
            self.equation(command)# executiong the equation
            i=i+1# updating the value of i
        return i
    #
    #
    # Time complexity
    # time complexity = maximum number of operations performed
    # therefore T(n)= 5 + T(equation)(n)= 16n+53
    # thus time complexity is O(n)
#
#
# Prints the values of all variables and also keeps track of the value references in use 
#
def value_of_variables():
#
#
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
# Time complexity
# Number of iterations of loop = n = len(data)
# thus time complexity is T(n)=3n+8
# therefore time complexity is O(n)
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
# Time complexity
# maximum number of iterations of loop =max(len(used))= n = len(data)
# thus time complexity is T(n)=3n+3
# therefore time complexity is O(n)
#
#
# Adds the unused values to the garbage list
#
def unused():
#
#
    for i in range(0,len(data)):# Termination: i increases to len(data)
        if(not(type(data[i])==tuple)):# checking for values
            if(not(index_in_use(i))):# checking if the value is not in use
                garbage.append(data[i])
#
#
# Time complexity
# Number of iterations of loop = n = len(data)
# maximum number of operations performed in each iteration= 3n+8
# thus time complexity is T(n)=3n*n +8n+1
# therefore time complexity is O(n^2)
#
#
# Prints value of each value and garbage values
#
def output():
#
#
    value_of_variables()# printing the values of variables
    unused()# adding the garbage values to garbage list
    if(len(garbage)):# checking if garbage is present or not
        print("Garbage values: ",garbage)
    else:
        print("No garbage")
#
#
# Time complexity
# maximum time complexity is T(n)=3n*n+11n+8
# therefore time complexity is O(n^2)
#
#
# Converts equations with less than five terms to equations with five terms
#
def assignment(L):
    if(len(L)==3):# x = y type equation
        return L+[None,None]
    elif(len(L)==4):# x = operator y type equation
        return L[:2]+[None]+L[2:]
    elif(len(L)==5):# x = y operator z type equation
        return L
    else:
        print("Invalid statement")
        sys.exit()
#
#
# Time complexity
# Time complexity = maximum number of operations performed = 4 +2*len(L) = 14
# thus, time complexity is O(1)
#
#
# Converts loop definition to instructions
#
def conditional(a,b,sign):
#
# Input:
#   a: String: First operand
#   sign: String: Operator
#   b: String: Second operand
#
# Output: list: list representing the equivalent instruction
#
    if(sign==">"):# a>b is equivalent to not(a<=b)
        statement=["BLE",a,b]
    elif(sign=="<"):# a<b is equivalent to not(b<=a)
        statement=["BLE",b,a]
    elif(sign=="!="):# a!=b is equivalent to not(a==b)
        statement=["BE",a,b]
    elif(sign=="<="):# a<=b is equivalent to not(b<a)
        statement=["BL",b,a]
    elif(sign==">="):# a>=b is equivalent to not(a<b)
        statement=["BL",a,b]
    else:# Invalid conditional operator
        print("Invalid conditional operator",sign,"for while loop")
        sys.exit()
    return statement
#
#
# Time complexity
# Time complexity = maximum number of operations performed = 7
# thus, time complexity is O(1)
#
#
# converts code into instructions
#
def transform(i):
#
# Input: i: int: index of the line that is to be transformed
#
    token_list = lines[i].split()# spliting the statement into a list of tokens
    p=len(token_list)# number of tokens
    if(p<3 or p>5):# checking for invalid statement
        print("Invalid Statement at line",i+1)
        sys.exit()
    x=tabs[i]# number of tabs in the begining of current line
    y=tabs[i+1]# number of tabs in the begining of next line
    if(x==y):# no change in indentation
        if(token_list[1]!="="):
            print("Invalid Statement")
            sys.exit()
        lis=assignment(token_list)
        statement=Instructions("Equation",lis[2],lis[3],lis[4],lis[0])# instruction is the same as token list
        instructions.append(statement)# adding instruction to instructions list
    elif(y>x):# increase in indentation
        if((y-x)>1):# more than one simultaneous tabs
            print("Invalid indentation at line",(i+1))
            sys.exit()
        else:
            if(p!=5):# invalid loop definition
                print("Loop definition invalid at line",i+1)
                sys.exit()
            elif(token_list[-1]!=":"):# invalid loop definition
                print("':' required at line",(i+1))
                sys.exit()
            elif(token_list[0]!="while"):# invalid loop definition
                print("invalid ststement at line",i+1)
                sys.exit()
            else:
                j=conditional(token_list[1],token_list[3],token_list[2])# converting token list to instruction
                statement=Instructions(j[0],j[1],None,j[2],None)
                instructions.append(statement)# adding instructions to token list
                branch.append(len(instructions)-1)# updating branch list
    else:# decrease in indentation
        p=x-y# total decrease in number of tabs
        if(p>len(branch)):# more decrease in indentation than number of open loops
            print("Invalid indentation")
            sys.exit()
        if(token_list[0]!="while"):
            statement=Instructions("Equation",token_list[2],token_list[3],token_list[4],token_list[0])
        else:
            if(p!=5):# invalid loop definition
                print("Loop definition invalid at line",i+1)
                sys.exit()
            elif(token_list[-1]!=":"):# invalid loop definition
                print("':' required at line",(i+1))
                sys.exit()
            elif(token_list[0]!="while"):# invalid loop definition
                print("invalid ststement at line",i+1)
                sys.exit()
            else:
                j=conditional(token_list)# converting token list to instruction
                statement=Instructions(j[0],j[1],None,j[2],None)
        instructions.append(statement)# adding instruction to instructions list
        for j in range(0,p):# Termination: i increases to p
            m=branch.pop(-1)# Taking the index of last open loop from branch
            instructions[m].instruction[3]=(len(instructions)+1)# adding index of next 
            #instruction to the instruction with open loop
            statement=Instructions("branch",None,None,None,m)
            instructions.append(statement)# adding a branch instruction with index of open loop
    #
    #
    #
    #
    # Time complexity
    # Time complexity = maximum number of operations performed 
    # therefore, T(n)=9 + len(lines[i]) + T(assignment)(n)+ T(Instructions())(n) = 33 + len(lines[i]) if type is Equation
    #                =14 + len(lines[i]) + T(conditional)(n) + T(Instructions())(n)= 36 + len(lines[i]) if the equation is equivalent to a loop defination
    #                =13 + len(lines[i]) + T(conditional)(n) + T(Instructions())(n) + T(loop)(p)=37 + 15p + len(lines[i]) if line is just preceding a branch type instruction
#
#
lines = [] # initalise to empty list
with open('a.txt') as f:
    lines = f.readlines() # read all lines into a list of strings
tabs=[]
for statement in lines: # each statement is on a separate line
    tab = 0
    while statement[tab] == '\t':
        tab += 1# counting number of tabs
    tabs.append(tab)# adding the number of tabs to the tabs list
tabs.append(0)# 0 represents no indentation
for i in range(0,len(lines)):
    transform(i)# converting each line to instructions
print("The equivalent instructions for the code are:")
for x in instructions:# printing the instructions
    print(x.instruction)
i=0
while(i<len(instructions)):
    j=instructions[i].execute(i)# executing each instruction
    if(j<i):# checking for branch type instructions
        used=[]
        garbage=[]
        output()# giving output if branch statement is found
    i=j
used=[]
garbage=[]
print("Final Output:")
output()# final output
#
#
# Example 1:
#
# Code:
"""
x = 5
i = 1
while i <= x :
    i = i + 1
    a = 3
    while a > 1 :
        a = a - 2
"""
#
# Output:
"""
The equivalent instructions for the code are:
['x', '=', '5']
['i', '=', '1']
['BL', 'x', 'i', 9]
['i', '=', 'i', '+', '1']
['a', '=', '3']
['BLE', 'a', '1', 8]
['a', '=', 'a', '-', '2']
['branch', 5]
['branch', 2]
Values of variables are:
x=5
i=2
a=1
Garbage values:  [3]
Values of variables are:
x=5
i=2
a=1
Garbage values:  [3]
Values of variables are:
x=5
i=3
a=1
Garbage values:  [2]
Values of variables are:
x=5
i=3
a=1
Garbage values:  [2]
Values of variables are:
x=5
i=4
a=1
Garbage values:  [2, 3]
Values of variables are:
x=5
i=4
a=1
Garbage values:  [2, 3]
Values of variables are:
x=5
i=5
a=1
Garbage values:  [2, 3, 4]
Values of variables are:
x=5
i=5
a=1
Garbage values:  [2, 3, 4]
Values of variables are:
x=5
i=6
a=1
Garbage values:  [2, 3, 4]
Values of variables are:
x=5
i=6
a=1
Garbage values:  [2, 3, 4]
Final Output:
Values of variables are:
x=5
i=6
a=1
Garbage values:  [2, 3, 4]
"""
#
# Time complexity
#
# time taken to store each line in lines=2* number of lines + 2 = 16
# time taken to count and add the number of tabs to tabs = 2*( number of lines + number of tabs)+ 2=26
# time taken to transform first line= 38
#                         second line= 38
#                         third line= 50
#                         fourth line= 49
#                         fifth line= 40
#                         sixth line= 53
#                         seventh line= 84
#
# time taken to execute first instruction = 2+ T(execute)(n)=16n + 55= 87 (taking n as 2)
#                      second instruction = 2+ T(execute)(n)=16n + 55= 119 (taking n as 4)
#                      third instruction = 2+ T(execute)(n)=16n + 55= 119 (taking n as 4)
#                      fourth instruction = 2+ T(execute)(n)=16n + 55= 135 (taking n as 5)
#                      fifth instruction = 2+ T(execute)(n)=16n + 55= 167 (taking n as 7)
#                      sixth instruction = 2+ T(execute)(n)=16n + 55= 167 (taking n as 7)
#                      seventh instruction = 2+ T(execute)(n)=16n + 55= 167 (taking n as 7)
#                      eighth instruction = 5
#                      sixth instruction again = 2+ T(execute)(n)=16n + 55= 167 (taking n as 7)
#                      ninth instructon = 5
# this set(3-4-5-6-7-8-6-9) of instructions runs for 1 iteration with n = 7 for each, time taken= 1012
# the instruction three is executed with n=7, time take= 167
# then the set(4-5-6-7-8-6-9) is executed with n=8, time taken= 925
# then the set(3-4-5-6-7-8-6-9) is executed with n=8, time taken= 1108
# then instructio three is executed with n=8, time taken= 183
# then the set(4-5-6-7-8-6-9) is executed with n=9, time taken= 1005
# then instruction 3 is executed with n=9, time taken= 199
#
# therefore, total time taken without output= 6131
#
# time taken for output= 4*232 + 2*288 + 5*350 = 3254 ( using T(n)=3n*n +11n +8)
#
# thus the total number of operations performed= 9385
#
# 
# Example 2
#
# Code:
"""
a = 5
while a > 0 :
    a = a - 1
"""
#
# Output:
"""
The equivalent instructions for the code are:
['a', '=', '5']
['BLE', 'a', '0', 4]
['a', '=', 'a', '-', '1']
['branch', 1]
Values of variables are:
a=4
Garbage values:  [5, 0, 1]
Values of variables are:
a=3
Garbage values:  [5, 0, 1, 4]
Values of variables are:
a=2
Garbage values:  [5, 0, 1, 4, 3]
Values of variables are:
a=1
Garbage values:  [5, 0, 4, 3, 2]
Values of variables are:
a=0
Garbage values:  [5, 1, 4, 3, 2]
Final Output:
Values of variables are:
a=0
Garbage values:  [5, 1, 4, 3, 2]
"""
#
# Time complexity
#
# time taken to store each line in lines=2* number of lines + 2 = 8
# time taken to count and add the number of tabs to tabs = 2*( number of lines + number of tabs)+ 2=10
# time taken to transform first line= 38
#                         second line= 49
#                         third line= 65
# time taken to execute first instruction = 2+ T(execute)(n)=16n + 55= 87 (taking n as 2)
#                      second instruction = 2+ T(execute)(n)=16n + 55= 103 (taking n as 3)
#                      third instruction = 2+ T(execute)(n)=16n + 55= 135 (taking n as 5)
#                      fourth instruction = 5
#                      second instruction again= 2+ T(execute)(n)=16n + 55= 135 (taking n as 5)
#                      third instruction again= 2+ T(execute)(n)=16n + 55= 151 (taking n as 6)
#                      fourth instruction = 5
#                      second instruction again= 2+ T(execute)(n)=16n + 55= 151 (taking n as 6)
#                      third instruction again= 2+ T(execute)(n)=16n + 55= 167 (taking n as 7)
#                      fourth instruction = 5
#                      second instruction again= 2+ T(execute)(n)=16n + 55= 167 (taking n as 7)
#                      third instruction again= 2+ T(execute)(n)=16n + 55= 167 (taking n as 7)
#                      fourth instruction = 5
#                      second instruction again= 2+ T(execute)(n)=16n + 55= 167 (taking n as 7)
#                      third instruction again= 2+ T(execute)(n)=16n + 55= 167 (taking n as 7)
#                      fourth instruction = 5
#                      second instruction again= 2+ T(execute)(n)=16n + 55= 167 (taking n as 7)
#
# Therefore, the total time without considering output=1959
#
# Time taken by output= 100 + 138 + 182 + 182 + 182 + 182= 966 ( using T(n)=3n*n +11n +8)
#
# Thus, the total number of operations performed= 2925
#
#