'''Assignment 5 by SATWIK MITTAL ENTRY NUMBER : 2021PH10213'''

class Instruction:
    def eval2(x):#to evaluate value of object x stored in string if it is float or bool
    #Input: String : x
    #Output: value after opearting on object stored in x
        try:
          y=eval(x)
          return y
        except NameError:#to return error if variable stored in list {which cannot be evaluated}
           return "NameError occurred. Some variable isn't defined."
    
    
    
    def check(k,l):
    # INPUT L is a list of elements
    # INPUT k is the “key” element we try to find in list L
    # OUTPUT: List: [True, j] if k is present in L at position j
    # (False, _) if k is not present in L.
      n = len(l)
      found = False
      i = 0
    # INVARIANT found == False implies forall j (0 ≤ j < i): L[j] =/= k
    # found == True implies L[i] == k
      while (i < n) & (not found) :
         if (l[i] == k) :
            found = True # L[i] == k
         else: # L[i] =/= k
              i += 1
    # EXIT when found OR (i == n)
    # return (found, i)
      return [found, i]
    
    def listtostring(l):#Convert every element of list to string 
    #Input: list :l is a list of elements
    #Output: list: new_list containg elements of list l but in a string
        new_list = []#Initialising the final list
        #Invariants:
        #for every item in l,if l[i]=item (0<=i<len(l)) then new_list[i]=str(item)
        for item in l:
          new_list.append(str(item))
        #Exit when i{ where i is index of item } i>=len(l)
        return new_list
    
    def check2(l):
    # INPUT L is a list of elements
    # OUTPUT [True,l_] True if l contains tuples and l contains the tuples as wa hole list of tuples
    # (False, _) if l doesnot contain any tuple 
      n = len(l)
      found = False
      l_=[]
      i = 0
    # INVARIANT found == False implies forall j (0 ≤ j < i): type(L[j]) =/= tuple
    #found == True implies type(L[i]) == tuple and l_[j]=l[i] for j < len(l)
      while (i < n) :
         if type(l[i])==tuple:
            l_.append(l[i])
            found = True 
            i+=1
         else: # L[i] =/= k
             i += 1
    # EXIT when found OR (i == n)
    # return [found, l_]
      return [found,l_]
    
    def check3(k,l):
    #Input:l : a list of elements {where elements are further list}
    #Input k : the element which we want to find at the zeroth index of element in l
    #Output [found,i] found==False where for every element in l its first element was not equal to k 
    #found==True if for some element in l its first element is equal to k {i is index in l where l[i][0] was equal to k}
        found=False
        i=0
        #Invariants:
        #found==True implies l[j][0]==k for 0<=j<i 
        #found==False implies forall j (0 ≤ j < i): l[j][0]=/=k
        for i in range (len(l)):
            if l[i][0]==k:
                found=True
                break 
        #exit as soon as we met the required condition or when found==false and i>=len(l)
        return [found,i]
    
    
    def app(k,l):#since our input is of list but we need to have integer or boolean entries in data list
    #Input:l : a list of elements {where elements are further list}
    #Input k :the element to be added at the end of list 
    #Output : list l after appending 
        if k.isnumeric()==True:#to check is k contains integer 
            l.append(int(k))
            return l
        elif eval(k)==1 or eval(k)==0:#to check if k contains boolean
            l.append(bool(eval(k)))
            return l
        
    def check4(l,dl):#this function is helper function for binass function 
        #checks the appropriate condition for appending
        dl_=listtostring(dl)
        if bool(l[2]==l[4]) and check(l[2],dl_)[0]==False  and check(l[4],dl_)[0]==False :#if l[2]==l[4] only one should be appended to avoid duplication
            app(l[2],dl)
        elif bool(l[2]!=l[4]) and check(l[2],dl_)[0]==False  and check(l[4],dl_)[0]==False:#if l[2]!=l[4] both should be appended
            app(l[2],dl)
            app(l[4],dl)
        elif bool(l[2]!=l[4]) and (check(l[2],dl_)[0]==False)  and (check(l[4],dl_)[0]==True):#if l[4] prsent already append only l[2]
            app(l[2],dl)    
        elif bool(l[2]!=l[4]) and check(l[2],dl_)[0]==True  and check(l[4],dl_)[0]==False:#if l[2] prsent already append only l[4]
            app(l[4],dl)
    def swapPositions(list, pos1, pos2):
         
        list[pos1], list[pos2] = list[pos2], list[pos1]
        return list
            
    def eval1_(f,dl,g_,l):#appending the evaluated value to data list or changing the tuples when l[0] is present initially in tuples list
        dl_=listtostring(dl)
        if type(f)==int or type(f)==float:
         if check(f,dl)[0]==True:#checking is f is already present in data list 
             #removing the initially stored tuple to replace it with new containg new assigned value
             dl.append((l[0],check(f,dl)[1]))
             e=dl.index(g_)
             swapPositions(dl,e,len(dl)-1)
             dl.remove(dl[len(dl)-1])
             
             print(dl)
             
         else:
             #removing the initially stored tuple to replace it with new containg new assigned value
            dl.append(f)
            dl.append((l[0],len(dl)-1))
            e=dl.index(g_)
            swapPositions(dl,e,len(dl)-1)
            dl.remove(dl[len(dl)-1])
            
        elif type(f)==bool:
            if check(str(f),dl_)[0]==True:#checking is f is already present in data list{we used dl_ to differentiate True and one}
                
                dl.append((l[0],check(str(f),dl_)[1]))
                e=dl.index(g_)
                swapPositions(dl,e,len(dl)-1)
                dl.remove(dl[len(dl)-1])
                
            else:
                #removing the initially stored tuple to replace it with new containg new assigned value
                dl.append(f)
                dl.append((l[0],len(dl)-1))
                e=dl.index(g_)
                swapPositions(dl,e,len(dl)-1)
                dl.remove(dl[len(dl)-1])
                
    def eval2_(f,dl,l):#appending the evaluated value to data list or changing the tuples when l[0] is not present initially in tuples list
        dl_=listtostring(dl)
        if type(f)==int or type(f)==float:
         if check(f,dl)[0]==True:#checking is f is already present in data list 
             
             dl.append((l[0],check(f,dl)[1]))
             
         else:
            
            dl.append(f)
            dl.append((l[0],len(dl)-1))
            
        elif type(f)==bool:
            if check(str(f),dl_)[0]==True:#checking is f is already present in data list{we used dl_ to differentiate True and one}
                
                dl.append((l[0],check(str(f),dl_)[1]))
                
            else:
                
                dl.append(f)
                dl.append((l[0],len(dl)-1))
    
    def funcass(l,dl):#to deal with x=y {Assigning type equations} type equations 
    #Input list:l: contains elemnets as strings {equation which we want to solve or assigning values to variables}
    #Input list dl: its the data list
    #Output: dl (which contain variables as tuples and second element of tuple represting at which index in dl its value is stored ) also 
    #stores value of assigned integers or booleans
       #to deal with case when len(l[2])!=0 {avoiding error}
       if len(l[2])!=0: 
        dl_=listtostring(dl)
        x=check2(dl)
        if x[0]==True:#if dl contains tuples
            #Invariants:
            #if l[2] present in tuples for some e in l then for k=len(dl) dl[k-1]=((l[0],e[1]))
            #if l[2] not present in tuples but in dl for some i dl[i]=l[2] then for k=len(dl) dl[k-1]=((l[0],i))
            #if l[2] not prsent in tuples and dl both then for k=len(dl) dl[k-1]=((l[0],k-2)) and dl[k-2]=l[2]
            for e in x[1]:
              if e[0]!=l[2] and check3(l[2],x[1])[0]==True:#two conditions to avoid jumping to else statement if l[2] is present after some other variable
                 continue 
              elif e[0]==l[2]:
                 #invariant:
                 # f[0]!=l[0] and check3(l[0],x[1])[0]==True: continue the loop 
                 # if f[0]==l[0] , for k=len(dl) dl[k-1]=((l[0],e[1]))
                 # if for all f in x[1] if f[0]!=l[0] ,for k=len(dl) dl[k-1]=((l[0],e[1]))
                 for f in x[1]:
                     if f[0]!=l[0] and check3(l[0],x[1])[0]==True:
                         continue
                     elif f[0]==l[0]:
                         
                         dl.remove(f)
                         dl.append((l[0],e[1]))
                         break#exit the loop as soon as f is found such f[0]==l[0]
                     elif f[0]!=l[0] and check3(l[0],x[1])[0]==False:
                         dl.append((l[0],e[1]))  
                         break 
              #exit : if condition satisfies exit through break  
              elif check3(l[2],x[1])[0]==False: #l[2] not present in any tuple
               
                 y=check(l[2],dl_)#to check in reamaining data list
                 
                 if y[0]==True:#if l[2] present in dl {other than tuple}
                           
                           if e[0]!=l[0] and check3(l[0],x[1])[0]==True:
                               continue
                           elif e[0]==l[0]:
                               dl.remove(e)
                               dl.append((l[0],y[1]))
                               break
                           elif  e[0]!=l[0] and check3(l[0],x[1])[0]==False:   
                        
                               dl.append((l[0],(y[1]))) 
                               break
                   
                 elif y[0]==False:#if l[2] not present in dl {other than tuple}
                     
                        
                       if e[0]!=l[0] and check3(l[0],x[1])[0]==True:#l[0] present in x[1]
                           continue
                       elif e[0]==l[0]:
                           if l[2].isnumeric()==True:
                                dl.append(int(l[2]))
                                dl.remove(e)
                                dl.append((l[0],len(dl)-1))
                                break
                           elif eval2(l[2])==1:
                               dl.append(bool(eval2(l[2])))
                               dl.remove(e)
                               dl.append((l[0],len(dl)-1))
                               break
                           elif eval2(l[2])==1:
                               dl.append(bool(eval2(l[2])))
                               dl.remove(e)
                               dl.append((l[0],len(dl)-1))
                               break
                           else:
                               raise Exception("Variable not defined") #error when variable is not defined earlier and we refrence new variable to it   
                                
                              
                       
                       elif e[0]!=l[0] and check3(l[0],x[1])[0]==False:#l[0] not present in x[1]
                          
                           if l[2].isnumeric()==True:
                                dl.append(int(l[2]))
                                dl.append((l[0],len(dl)-1))
                                break
                           elif eval2(l[2])==1:
                                dl.append(bool(eval2(l[2])))
                                
                                dl.append((l[0],len(dl)-1))
                                break
                           elif eval2(l[2])==0:
                                dl.append(bool(eval2(l[2])))
                                
                                dl.append((l[0],len(dl)-1)) 
                                break
                           else:
                                raise Exception("Variable not defined")#error when variable is not defined earlier and we refrence new variable to it
                       
            #exit when index of e>=len(x[1]) or x[0]=False                    
        
        else:#Case when dl contains no tuples
          if check(l[2],dl_)[0]==True:#if l[2] present in dl
          
            if l[2].isnumeric()==True:
                 
                 dl.append((l[0],check(l[2],dl_)[1]))
          else:#if l[2] not present in dl
              if l[2].isnumeric()==True:
                  dl.append(int(l[2]))
                  dl.append((l[0],len(dl)-1))
                  
              elif eval2(l[2])==1:
                 dl.append(bool(eval2(l[2])))
                 
                 dl.append((l[0],len(dl)-1))
                 
              elif eval2(l[2])==0:
                 dl.append(bool(eval2(l[2])))
                 
                 dl.append((l[0],len(dl)-1))
                  
              else:
                 raise Exception("Variable not defined")#error when variable is not defined earlier and we refrence new variable to it
                 
                        
        return dl 
    
       elif len(l[2])==0:#to avoid error 
         raise Exception("operation cannot be performed") 
    
    
    
    
    
    def binass(l,dl):
    #Input list:l: contains elemnets as strings {equation which we want to solve }
    #Input list dl: its the data list
    #output list dl after solving equation
      if len(l[4])!=0 and len(l[2])!=0: #to avoid error  
        dl_=listtostring(dl)
        x=check2(dl)
        if x[0]==True:#if dl contain tuples 
          if check3(l[2],x[1])[0]==True and check3(l[4],x[1])[0]==True:#both variables present in tuples{l[2] and l[4]} 
              if check3(l[0],x[1])[0]==True:#checking of first variable if already present{l[0]}
                  f1=check3(l[2],x[1])[1]
                  f2=check3(l[4],x[1])[1]
                  e1=x[1][f1][1]
                  e2=x[1][f2][1]
                  e=str(dl[e1])+" "+l[3]+" "+str(dl[e2])
                  f=eval(e)
                  g=check3(l[0],x[1])[1]
                  g_=x[1][g]
                  
                  eval1_(f, dl, g_, l)
                       
              elif check3(l[0],x[1])[0]==False:#checking of first variable if not alraedy present 
                  f1=check3(l[2],x[1])[1]
                  f2=check3(l[4],x[1])[1]
                  e1=x[1][f1][1]
                  e2=x[1][f2][1]
                  e=str(dl[e1])+" "+l[3]+" "+str(dl[e2])
                  f=eval(e)
                  eval2_(f,dl,l)
                         
          elif check3(l[2],x[1])[0]==True and check3(l[4],x[1])[0]==False:# only l[2] is present in tuples not l[4] 
             
             if check(l[4],dl_)[0]==True:#to check if l[4] is present in remaining data list
                 if check3(l[0],x[1])[0]==True:#checking of first variable if already present{l[0]}
                   f1=check3(l[2],x[1])[1]
                   f2=check(l[4],dl_)[1]
                   e1=x[1][f1][1]
                   e2=dl[f2]
                   
                   e=str(dl[e1])+" "+l[3]+" "+str(e2)
                   
                   f=eval(e)
                   
                   g=check3(l[0],x[1])[1]
                   g_=x[1][g]
                   print(g_)
                   print(dl)
                   print(f)
                   
                   eval1_(f, dl, g_, l)    
                 elif check3(l[0],x[1])[0]==False: #checking of first variable if not alraedy present
                     f1=check3(l[2],x[1])[1]
                     f2=check(l[4],dl_)[1]
                     e1=x[1][f1][1]
                     e2=dl[f2]
                     e=str(dl[e1])+" "+l[3]+" "+str(e2)
                     f=eval(e)
                     eval2_(f, dl,l)
                             
             elif check(l[4],dl_)[0]==False:#if l[4] was not prsent in the remaining data list 
                     if l[4].isnumeric()==True or eval2(l[4])==1 or eval2(l[4])==0:#since l[4] not present in list it cannot be a name
                         if check3(l[0],x[1])[0]==True:#checking of first variable if alraedy present
                           f1=check3(l[2],x[1])[1]
                           e1=x[1][f1][1]
                           e2=l[4]
                           if l[4]!=str(dl[e1]):
                               app(l[4],dl)
                           e=str(dl[e1])+" "+l[3]+" " +l[4]
                           f=eval(e)
                           g=check3(l[0],x[1])[1]
                           g_=x[1][g]
                           eval1_(f, dl, g_, l)
                    
                         elif check3(l[0],x[1])[0]==False:#checking of first variable if not alraedy present
                             
                             f1=check3(l[2],x[1])[1]
                             e1=x[1][f1][1]
                             e2=l[4]
                             if l[4]!=str(dl[e1]):
                                 app(l[4],dl)
                             e=str(dl[e1])+" "+l[3]+" " +l[4]
                             f=eval(e)
                             eval2_(f, dl,l)
                     else:
                         raise Exception("Variable not defined")#exception where l[4] is a variable {not defined case} and we try to add it to something without defining before
                     
          elif check3(l[2],x[1])[0]==False and check3(l[4],x[1])[0]==True:# only l[4] is present in tuples not l[2]
            
             if check(l[2],dl_)[0]==True:#to check if l[2] is present in remaining data list
                 if check3(l[0],x[1])[0]==True:#checking of first variable if already present{l[0]}
                   f1=check3(l[4],x[1])[1]
                   f2=check(l[2],dl_)[1]
                   e1=x[1][f1][1]
                   e2=dl[f2]
                   e=str(dl[e1])+" "+l[3]+" "+str(e2)
                   f=eval(e)
                   g=check3(l[0],x[1])[1]
                   g_=x[1][g]
                   eval1_(f, dl, g_, l)
                            
                 elif check3(l[0],x[1])[0]==False:#checking of first variable if not alraedy present 
                     
                     f1=check3(l[4],x[1])[1]
                     f2=check(l[2],dl_)[1]
                     e1=x[1][f1][1]
                     e2=dl[f2]
                     e=str(dl[e1])+" "+l[3]+" "+str(e2)
                     f=eval(e)
                     eval2_(f, dl,l)
                             
             elif check(l[2],dl_)[0]==False:#if l[2] was not prsent in the remaining data list 
                     
                     if l[2].isnumeric()==True or eval2(l[2])==1 or eval2(l[2])==0:#since l[2] not present in list it cannot be a name
                         if check3(l[0],x[1])[0]==True:#checking of first variable if already present{l[0]}
                           f1=check3(l[4],x[1])[1]
                           e1=x[1][f1][1]
                           e2=l[2]
                           if l[2]!=str(dl[e1]):
                               app(l[2],dl)
                           e=str(dl[e1])+" "+l[3]+" " +l[2]
                           f=eval(e)
                           g=check3(l[0],x[1])[1]
                           g_=x[1][g]
                           eval1_(f, dl, g_, l)
                    
                         elif check3(l[0],x[1])[0]==False:#checking of first variable if not alraedy present  
                             f1=check3(l[4],x[1])[1]
                             
                             e1=x[1][f1][1]
                             e2=l[2]
                             if l[2]!=str(dl[e1]):
                                 app(l[2],dl)
                             e=str(dl[e1])+" "+l[3]+" " +l[2]
                             f=eval(e)
                             eval2_(f, dl,l)
                     
                     else:
                         raise Exception("Variable not defined")#exception where l[4] is a variable {not defined case} and we try to add it to something without defining before
          
          elif check3(l[2],x[1])[0]==False and check3(l[4],x[1])[0]==False:# both l[4] and l[2] are not present in tuples list
            #since l[2] and l[4] both not present in list they cannot be a name
            if (l[2].isnumeric()==True or eval2(l[2])==1 or eval2(l[2])==0) and  (l[4].isnumeric()==True or eval2(l[4])==1 or eval2(l[4])==0):
               if check3(l[0],x[1])[0]==True:#checking of first variable if alraedy present
                 check4(l, dl)
                 e=l[2]+" "+l[3]+" " +l[4]
                 f=eval(e)
                 g=check3(l[0],x[1])[1]
                 g_=x[1][g]
                 eval1_(f, dl, g_, l)
                          
               elif check3(l[0],x[1])[0]==False:#checking of first variable if not alraedy present
                   
                   check4(l, dl)
                   e=l[2]+" "+l[3]+" " +l[4]
                   f=eval(e)
                   eval2_(f, dl,l)         
            
            else:
             raise Exception("Variable not defined")#exception where l[4] is a variable {not defined case} and we try to add it to something without defining before    
        else:#no tuples in data list 
           if (l[2].isnumeric()==True or eval2(l[2])==1 or eval2(l[2])==0) and  (l[4].isnumeric()==True or eval2(l[4])==1 or eval2(l[4])==0):
              if check3(l[0],x[1])[0]==True:#checking of first variable if alraedy present
                check4(l, dl)
                e=l[2]+" "+l[3]+" " +l[4]
                f=eval(e)
                g=check3(l[0],x[1])[1]
                g_=x[1][g]
                eval1_(f, dl, g_, l)
                        
              elif check3(l[0],x[1])[0]==False:#checking of first variable if not alraedy present 
                  check4(l, dl)
                  e=l[2]+" "+l[3]+" " +l[4]
                  f=eval(e)
                  eval2_(f, dl,l)          
           
           else:
             raise Exception("Variable not defined")##exception where l[4] is a variable {not defined case} and we try to add it to something without defining before
        return dl 
      else:
         raise Exception("Operation cannot be performed") #len zero operation cannot be performed
        
        
    def uniass(l,dl):#to solve equations where unary operatorss are involved
    #Input list:l: contains elemnets as strings {equation which we want to solve }
    #Input list dl: its the data list
    #output list dl after solving equation
      if len(l[3])!=0:#to avoid error 
        dl_=listtostring(dl)
        x=check2(dl)
        if x[0]==True:#if dl contain tuples 
          if check3(l[3],x[1])[0]==True : #to check if l[3] is one of the tuples first element
              if check3(l[0],x[1])[0]==True:#checking of first variable if alraedy present
                  f1=check3(l[3],x[1])[1]
                  e1=x[1][f1][1]
                  e=l[2] +''+str(dl[e1])
                  f=eval(e)
                  g=check3(l[0],x[1])[1]
                  g_=x[1][g]
                  eval1_(f, dl, g_, l)
                       
              elif check3(l[0],x[1])[0]==False:#checking of first variable if not alraedy present 
                  f1=check3(l[3],x[1])[1]
                  e1=x[1][f1][1]
                  e=l[2] +'  '+str(dl[e1])
                  f=eval(e)
                  eval2_(f, dl,l) 
        
          elif check3(l[3],x[1])[0]==False :#if l[3] is not present in tuples list
           if check(l[3],dl_)[0]==True:#to check if l[3] present in dl or not 
             if (l[3].isnumeric()==True or eval2(l[3])==1 or eval2(l[3])==0) :
           
               if check3(l[0],x[1])[0]==True:#checking of first variable if alraedy present
                 
                 f2=check(l[3],dl_)[1]
                 
                 e2=dl[f2]
                 e=l[2]+"  "+str(e2)
                 f=eval(e)
                 g=check3(l[0],x[1])[1]
                 g_=x[1][g] 
                 eval1_(f, dl, g_, l)
                          
               elif check3(l[0],x[1])[0]==False:#checking of first variable if not alraedy present 
                   
                   f2=check(l[3],dl_)[1]
                   e2=dl[f2]
                   e=l[2]+"  "+str(e2)
                   f=eval(e)
                   eval2_(f, dl,l)
                           
             else:
                raise Exception("Variable not defined")#we cannot append the variable which is not defined before
                
           elif check(l[3],dl_)[0]==False:#if l[3] is not present in dl 
                   
                   if l[3].isnumeric()==True or eval2(l[3])==1 or eval2(l[3])==0:
                       if check3(l[0],x[1])[0]==True:#checking of first variable if alraedy present
                         app(l[3],dl)
                         e=l[2]+"  "+l[3]
                         f=eval(e)
                         g=check3(l[0],x[1])[1]
                         g_=x[1][g]
                         eval1_(f, dl, g_, l)
                  
                       elif check3(l[0],x[1])[0]==False:#checking of first variable if not alraedy present 
                           app(l[3],dl)
                           e=l[2]+"  "+l[3]
                           f=eval(e)
                           eval2_(f, dl,l)
                   
                   else:
                       raise Exception("Variable not defined")#we cannot append the variable which is not defined before     
                
        else:#case when dl doesnot contain any tuple
            if check(l[3],dl_)[0]==True:#if l[3] already present in dl or not 
              if (l[3].isnumeric()==True or eval2(l[3])==1 or eval2(l[3])==0) :
            
                if check3(l[0],x[1])[0]==True:#checking of first variable if alraedy present
                  
                  f2=check(l[3],dl_)[1]
                  
                  e2=dl[f2]
                  e=l[2]+"  "+str(e2)
                  f=eval(e)
                  g=check3(l[0],x[1])[1]
                  g_=x[1][g] 
                  eval1_(f, dl, g_, l)
                           
                elif check3(l[0],x[1])[0]==False:#checking of first variable if not alraedy present 
                    
                    f2=check(l[3],dl_)[1]
                    e2=dl[f2]
                    e=l[2]+"  "+str(e2)
                    f=eval(e)
                    eval2_(f, dl,l)
                            
              else:
                 raise Exception("Variable not defined")#we cannot append the variable which is not defined before
                 
            elif check(l[3],dl_)[0]==False: #l[3] not initially present in dl
                    
                    if l[3].isnumeric()==True or eval2(l[3])==1 or eval2(l[3])==0:
                        if check3(l[0],x[1])[0]==True:#checking of first variable if alraedy present
                          
                          app(l[3],dl)
                          e=l[2]+"  "+l[3]
                          f=eval(e)
                          g=check3(l[0],x[1])[1]
                          g_=x[1][g]
                          eval1_(f, dl, g_, l)
                   
                        elif check3(l[0],x[1])[0]==False:#checking of first variable if not alraedy present 
                            app(l[3],dl)
                            e=l[2]+"  "+l[3]
                            f=eval(e)
                            eval2_(f, dl,l)
                    
                    else:
                        raise Exception("Variable not defined") #we cannot append the variable which is not defined before 
        
        return dl        
      else:
          raise Exception("Operation cannot be performed")#no meaning if l[3] is empty                   
    
    
    def solve(l,dl):
    #Input list:l: contains elemnets as strings {equation which we want to solve }
    #Input list dl: its the data list
    #output : the function to be performed satisfying the required conditions
        if len(l)==5:#to tackle equations where binary operators are used
            binass(l, dl)
            
        elif len(l)==4:#to tackle equations where unary operators are used
         if l[3].isalnum()==False or l[3]=="not" or l[3]=="and":
            raise Exception("Operation cannot be performed")#to avoid error
         else:
             uniass(l,dl)
        elif len(l)==3:#to tackle assignment type equations where a variable is assigned a value
         if l[2].isalnum()==False or l[2]=="not" or l[2]=="and":
            raise Exception("Operation cannot be performed")#to avoid error
         else:
            funcass(l, dl)
        
def garbage(dl):
#Input list dl: its the data list
#output list g: containg all the garbage values
    y=check2(dl)[1]
    #initialisation
    g_=[]#to create a list of assigned index to each variable in tuple
    g=[]
    #invariants:
    #for all i such that 0<=i< len(y) g_[i]=dl[y[i][1]
    for i in range (len(y)):
        g_.append(dl[y[i][1]])
    #Exit when i>= len(y)
    #invariants:
    #for some j 0<=j<len(g) and i 0<=i<len(dl) dl[i]=g[j] 
    for i in range (len(dl)) :
        if check(dl[i],g_)[0]==False and type(dl[i])!=tuple:
            g.append(dl[i])
    #exit when i>=len(dl)      
    return g 
def convert(dl):#used as helper function so as to return final values of integers
#Input list dl: its the data list
#output list p: modified list of tuple where the second element of tuple is turned to string  
     x=check2(dl)
     #initialisation
     p=[]
     #invariants:
     # for all i 0<=i<len(x[1]) p[i][1]=str([x[1][i][1])
     for  i in range (len(x[1])):
         p.append((x[1][i][0],str(dl[x[1][i][1]])))
     #exit when i>=len(x[1])    
     return p
 
def finalval(dl):#to return final values of variables
#Input list dl: its the data list
#output: printed value of all integers in the form x = value
       x=convert(dl)
       #invariants:
       #for all i such that 0<=i<len(x) print x[i][0]+' = '+x[i][1]
       for i in range (len(x)):
           print(x[i][0]+' = '+x[i][1]) 
       #exit when i>=len(x)
    

#END OF ASSIGNMENT 
    