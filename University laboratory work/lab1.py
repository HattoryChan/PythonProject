# -*- coding: utf-8 -*-
"""
Labratory work №1
Calcucated etwo value expression
MelnikovEA FM-104
"""
# Main function
def main():
    fl = 1
    while(fl):          
        expr : str = str(input("Input your expression: \n"))            
        print("%.3f" % signAction(expr))    
    
        # continuation or exit part
        check = input("Enter 0 to Stop or continuation\n")
        if (check.isdigit()):        #Checking the correctness of input Data
            if (not int(check)):       #Checking the correctness of input Data
                print("GoodBye!")
                fl=0
            else:
                print("Continue...")
        else:                
          print("You enter not digit")

# search sign in you expression
def signSearch(expr = str()):           
    for i in range(len(expr)): #Run in string array and search a sign
        if((expr[i] == '+' or expr[i] == '-' 
            or expr[i] == '*' or expr[i] == '/') and i != 0):
            return i
    else:   
        print("Don't found sign")
        return 0    
 
# validation of data and get value    
def getInVal(expr : str, numb):  
    if(signSearch(expr) == 0 or (expr[0:signSearch(expr)]).isalpha() or (expr[signSearch(expr)+1:len(expr)]).isalpha() ): #Checking correct input Data
        print("Input data is not correct")
        return 0
    
    catStr = expr[0:signSearch(expr)]       
    if (not catStr.isalpha() and numb == 0): #Checking the correctness of input Data
        return catStr
   
    catStr = expr[signSearch(expr)+1:len(expr)] 
    if (not catStr.isalpha() and numb == 1):  #Checking the correctness of input Data
        return catStr    
    
    print("Symbol is not digit")
    return 0

# Performance of a calculations
def signAction(expr : str):
    if(signSearch(expr) == 0): #Checking the correctness of the return value
        return 0
    
    if expr[signSearch(expr)] == '+' :            
        if (type(getInVal(expr, 0) == float) and type(getInVal(expr, 1) == float)): #Checking the correctness of input Data
            return(float(getInVal(expr, 0)) + float(getInVal(expr,1)))   
        
        
    if expr[signSearch(expr)] == '-' :
        if (type(getInVal(expr, 0) == float) and type(getInVal(expr, 1) == float)): #Checking the correctness of input Data
            return(float(getInVal(expr, 0)) - float(getInVal(expr,1)))
        
    if expr[signSearch(expr)] == '*' :
        if (type(getInVal(expr, 0) == float) and type(getInVal(expr, 1) == float)): #Checking the correctness of input Data
            return(float(getInVal(expr, 0)) * float(getInVal(expr,1)))

    if expr[signSearch(expr)] == '/' :
        if (type(getInVal(expr, 0) == float) and type(getInVal(expr, 1) == float) and (float(getInVal(expr,1)) != 0.0)): #Checking the correctness of input Data
            return(float(getInVal(expr, 0)) / float(getInVal(expr,1)))
        else:
            print("You divide on zero!")
            return 0
            
    print("Invalid number")
    return 0        
   
         
"""
START
"""
main()    