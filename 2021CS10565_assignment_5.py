import sys
class Instructions:
    data=[]
    l=[]
    finalvalues=[]
    garbage=[]
    def member(self,S,e):
        #The function returns true if e is a member of set S, and otherwise it returns 𝐹𝑎𝑙𝑠𝑒.
        #Input: A list S which represents a set that contains no duplicates of some type and an element e of the same type
        #Output: Boolean
        #LOOP INVARIANT: found= True implies e is a member of S and at this value the loop is exitted
        n=len(S)
        found=False
        i=0
        while (i<n and (not found)):
            #n-i decreases 
            #TERMINATION: either i==n and found= Fasle implies e is not a member of S or 
            #found=True implies e is a member of S
            if S[i]==e and type(S[i])==type(e):
                found=True
            i +=1
        return found
    def updatelist(self,l1,m,new_index):
        def abc(l1):
            found=False
            for i in range(len(l1)):
                if type(l1[i])==tuple:
                   found=True
            return found
        if abc(l1)==False:
            l1.append((m,new_index))
        else:
            for i in range(len(l1)):
                if type(l1[i])==tuple:
                    a=(l1[i])[0]
                    if a==m:
                        l1.remove(l1[i])
                        z=(a,new_index)
                        if self.member(l1,z)==False:  
                            l1.append(z)
                    else:
                        if self.member(l1,(m,new_index))==False:
                            l1.append((m,new_index))
        
            return (l1)
    def operator(self,a,b,s):
        if s=='+':
            return a+b
        elif s=='-':
            return a-b
        elif s=='*':
            return a*b
        elif s=='/':
            if b!=0:
                return (a//b)
            else:
                sys.exit("Division by zero is invalid")
        elif s=='>':
            if a>b:
                return True 
        elif s=='<':
            if a<b:
                return True
            else:
                return False
        elif s=='>=':
            if a>=b:
                return True
            else:
                return False
        elif s=='<=':
            if a<=b:
                return True
            else:
                return False
        elif s=='==':
            if a==b:
                return True
            else:
                return False
        elif s=='!=':
            if a!=b:
                return True
            else:
                return False
        elif s=='and':
            return a and b
        elif s=='or':
            return a or b
    def stringtobool(x):
        if x=='True':
            return True
        elif x=='False':
            return False
    def findindex(L,t):
        for i in range(len(L)):
            if L[i] is t:
                break
        return i
    
    def equation(self,L):
        i=0
        l=[L]
        if len(l[i])==3:   
            if l[i][1]=='=':
                if l[i][2].isdigit():
                    self.updatelist(self.data,l[i][0],self.findindex(self.data,int(l[i][2])))
                    self.updatelist(self.finalvalues,l[i][0],int(l[i][2])) 
                elif (l[i][2]=='True' or l[i][2]=='False'):
                    self.updatelist(self.data,l[i][0],self.findindex(self.data,self.stringtobool(l[i][2])))
                    self.updatelist(self.finalvalues,l[i][0],self.stringtobool(l[i][2])) 
                else:
                    for r in (self.data):
                        if type(r)==tuple:
                            if r[0]==l[i][2]:
                                k=r[1]
                                break
                    if k==r[1]:
                        self.updatelist(self.data,l[i][0],k)
                        self.updatelist(self.finalvalues,l[i][0],self.data[k]) 
                    else:
                        sys.exit("BAD INPUT TYPE please define the variable before assigning it to some other variable")
            else:
                sys.exit("Statement must be of the form Variable = Expression")
    
        elif len(l[i])==4:   
            if l[i][1]=='=':
                if l[i][2]=='-':
                    if l[i][3].isdigit():
                        if self.member(self.data,-int(l[i][3]))==False:
                            self.data.append(-int(l[i][3]))
                        self.updatelist(self.data,l[i][0],self.findindex(self.data,-int(l[i][3])))
                        self.updatelist(self.finalvalues,l[i][0],-int(l[i][3]))   
                    elif l[i][3]=='True' or l[i][3]=='False':
                        sys.exit("- must take an integer argumnet after it (-Boolean) make no sense")    
                    else:
                        for r in (self.data):
                            if type(r)==tuple:
                                if r[0]==l[i][3]:
                                    k=r[1]
                                    break
                        if k==r[1]:
                            if type(self.data[k])==int:
                                if self.member(self.data,(-1)*self.data[k])==False:
                                    self.data.append((-1)*self.data[k])
                                self.updatelist(self.data,l[i][0],self.findindex(self.data,-self.data[k]))
                                self.updatelist(self.finalvalues,l[i][0],-self.data[k]) 
                            else:
                                sys.exit("- must take an integer argumnet after it examples like (-Boolean) make no sense")
                        else:
                            sys.exit('BAD INPUT TYPE please define the variable before assigning it to some other variable')
                elif l[i][2]== 'not':
                    if l[i][3]== 'True' or l[i][3]=='False':
                        if self.member(self.data,not(self.stringtobool(l[i][3])))==False:
                            self.data.append(not(self.stringtobool(l[i][3])))
                        self.updatelist(self.data,l[i][0],self.findindex(self.data,not(self.stringtobool(l[i][3]))))
                        self.updatelist(self.finalvalues,l[i][0],not(self.stringtobool(l[i][3]))) 
                    else:
                        for r in (self.data):
                            if type(r)==tuple:
                                if r[0]==l[i][3]:
                                    k=r[1]
                                    break
                        if k==r[1]:
                            if type(self.data[k])==bool:
                                if self.member(self.data,not(self.data[k]))==False:
                                    self.data.append(not(self.data[k]))
                                self.updatelist(self.data,l[i][0],self.findindex(self.data,not(self.data[k])))
                                self.updatelist(self.finalvalues,l[i][0],not(self.data[k])) 
                            else:
                                sys.exit("BAD INPUT TYPE not must take boolean arguments only")
                        else:
                            sys.exit("BAD INPUT TYPE please define the variable before assigning it to some other variable")
                else:
                    sys.exit("BAD INPUT TYPE length 4 statement must be not(Expression) or -(Expression) type only.")
            else:    
                sys.exit("BAD INPUT TYPE statement must be of the form VARIABLE = EXPRESSION only.")
        
        elif len(l[i])==5:
            if l[i][1]=='=':
                if (l[i][2]=='True'or l[i][2]=='False'):
                    if (l[i][4]=='True' or l[i][4]=='False'):
                        x=self.operator(self.stringtobool(l[i][2]),self.stringtobool(l[i][4]),l[i][3])
                        if (self.member(self.data,x)==False):
                            self.data.append((x))
                        self.updatelist(self.data,l[i][0],self.findindex(self.data,x))
                        self.updatelist(self.finalvalues,l[i][0],x) 
                    else:
                        for r in (self.data):
                            if type(r)==tuple:
                                if r[0]==l[i][4]:
                                    q1=r[1]
                                    break
                        if q1==r[1]:
                            if type(self.data[q1])==bool:    
                                f=self.operator(self.stringtobool(l[i][2]),self.data[q1],l[i][3])
                                if self.member(self.data,f)==False:
                                    self.data.append(f)    
                                self.updatelist(self.data,l[i][0],self.findindex(self.data,f))
                                self.updatelist(self.finalvalues,l[i][0],f) 
                            else:
                                sys.exit("Input cannot have operator between boolean and some other type")
                        else:
                            sys.exit("BAD INPUT TYPE please define the variable before assigning it to some other variable")
                
                elif (l[i][4]=='True' or l[i][4]=='False') and (l[i][2]!='True' and l[i][2]!='False'):
                    for r in self.data:
                        if type(r)==tuple:
                            if r[0]==l[i][2]:
                                m1=r[1]
                                break
                    if m1==r[1]:
                        if type(self.data[m1])==bool:
                            f=self.operator(self.data[m1],self.stringtobool(l[i][4]),l[i][3])
                            if self.member(self.data,f)==False:
                                self.data.append(f)    
                            self.updatelist(self.data,l[i][0],self.findindex(f))
                            self.updatelist(self.finalvalues,l[i][0],f)
                        else:
                            sys.exit("Input cannot have operator between boolean and some other type")
                    else:
                        sys.exit("BAD INPUT TYPE please define the variable before assigning it to some other variable") 
                
                elif (l[i][2]).isdigit():
                    if l[i][4].isdigit():
                        x=self.operator(int(l[i][2]),int(l[i][4]),l[i][3])
                        if (self.member(self.data,x)==False):
                            self.data.append(x)    
                        self.updatelist(self.data,l[i][0],self.findindex(self.data,x))
                        self.updatelist(self.finalvalues,l[i][0],x) 
                    else:
                        for r in (self.data):
                            if type(r)==tuple:
                                if r[0]==l[i][4]:
                                    q1=r[1]
                                    break
                        if q1==r[1]:
                            if type(self.data[q1])==int:    
                                f=self.operator(int(l[i][2]),self.data[q1],l[i][3])
                                if self.member(self.data,f)==False:
                                    self.data.append(f)
                                self.updatelist(self.data,l[i][0],self.findindex(self.data,f))
                                self.updatelist(self.finalvalues,l[i][0],f) 
                            else:
                                sys.exit("Input cannot have operator between integer and some other type")
                        else:
                            sys.exit("BAD INPUT TYPE please define the variable before assigning it to some other variable")
                            
                elif l[i][4].isdigit() and (l[i][2]).isdigit()==False:
                    for r in self.finalvalues:
                        if type(r)==tuple:
                            if r[0]==l[i][2]:
                                m1=r[1]
                                break
                    if m1==r[1]:
                        if type(m1)==int:
                            f=(self.operator(m1,int(l[i][4]),l[i][3]))
                            if self.member(self.data,f)==False:
                                self.data.append(f)
                            self.updatelist(self.data,l[i][0],self.findindex(self.data,f))
                            self.updatelist(self.finalvalues,l[i][0],f) 
                        else:
                            sys.exit("Input cannot have operator between integer and some other type")
                    else:
                        sys.exit("BAD INPUT TYPE please define the variable before assigning it to some other variable")
                else:
                    for r in (self.finalvalues):
                        if type(r)==tuple:
                            if r[0]==l[i][2]:
                                k=r[1]
                                break
                    if k==r[1]:
                        for r1 in (self.finalvalues):
                            if type(r1)==tuple:
                                if r1[0]==l[i][4]:
                                    q1=r1[1]
                                    break
                        if q1==r1[1]:
                            if ((type(k)==type(q1)==int) or (type(k)==type(q1)==bool)):
                                f=self.operator(k,q1,l[i][3])
                                if self.member(self.data,f)==False:
                                    self.data.append(f)    
                                self.updatelist(self.data,l[i][0],(self.findindex(self.data,f)))
                                self.updatelist(self.finalvalues,l[i][0],f) 
                            else:
                                sys.exit("Values assigned to variables must be of the form int or bool only for operator to be applied") 
                        else:
                            sys.exit("BAD INPUT TYPE please define the variable before assigning it to some other variable")
                    else:
                        sys.exit("BAD INPUT TYPE please define the variable before assigning it to some other variable")
            else:
                sys.exit("BAD INPUT TYPE statement should be of the form VARIABLE = EXPRESSION.")
    
        else:   
            sys.exit("Line is not of the correct form ,length of each input line should be 3,4 or 5")

#Helper functions used :
#member(S,e) : This function checks if an element e is present in a list S
#updatelist(l1,m,new_index): This function works on three different conditions
#(1) When l1 has no tuple present then the function appends (m,new_index) to the list
#(2) When l1 has tuples present and has a tuple whose zeroth index element is equal to m then the function 
# deletes the previous tuple and appends (m,new_index) to the list l1
#(3) When l1 has tuples present and none of the tuples have zeroeth index element equal to m then the
# function appends (m,new_index) to the list l1
#operator(a,b,s): This function operates the operation quoted under string s on a and b
#stringtobool(x): This function converts 'True' to True and 'False' to False

#The whole algoithm works in a very systematic manner 
#First we open the text file and take it line by line as an input
   #List g stores each line of the input as strings 
   #List l stores list of elements of each line of the input
#Then we store all the integers and booleans present in the input file in a new list (data) and if 
#there is no integer or boolean in the whole input file we print an error and exit the program
#Then for each element of l we check it's length and according to the grammar provided to us
#TERM can only be integer boolean or a variable that has been assigned in any of the previous lines
#Depending on the cases we enter the if condition qnd store the operated value of any variable in
#the data list and also store a tuple (x,i) where i points to the position in data list where
#the value of x is stored, in any other case the program prints an error and terminates the program
#List finalvalues contains (x,t) where x is any variable mentioned in the input file and t is the final 
#value of it 
#List garbage contains those values in the data list to which no variable points at the end be it boolean or 
#integer
#In any grammatical or syntax error in the input file an error message is printed and the program
#is terminated


    
    
        


