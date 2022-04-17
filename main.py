import os
import sys
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print("Welcome to the CLI calculator!")

def exit():
    print("\nExiting...")
    time.sleep(2)
    sys.exit()

calcFilled = False

while(calcFilled == False):
    print("Please enter your calculation:")

    valid = False
    while (valid == False):
        try: 
            x = int(input("x = "))
            break
        except:
            print("Invalid input")
            continue
    
    oValid = False
    while (oValid == False):       
        opand = input("opand = ") 
             
        if(opand != "+" and opand != "-" and opand != "*" and opand != "/" and opand != "X" and opand != "x"):
            print("Invalid Operator")
            continue
        else:
            break
    
            
    
    if(opand == "X" or opand == "x"):
        opand = "*"    
        
    yValid = False
    
    while(yValid == False):
        try:
            y = int(input("y = "))
            if(y == KeyboardInterrupt):
                print("\nExiting...")
                sys.exit()
            break
        except:
            print("Invalid input")
            continue           
    
    print("Calculating...")
    time.sleep(1)
    clear()
    
    sum = eval(f"{x}{opand}{y}")
    
    print(sum)
    
    ct = False
    
    while(ct == False):
        print("continue with current sum?")
        t = input("y/n: ")
        #lower didnt work?
        if(t != "y" and t != "n" and t != "Y" and t != "N"):
            print("Invalid input")
            continue
        if(t == ""):
            print("Invalid input")
            continue
        if(t == "n"):
            print("Continue with new calculation?")
            q = input("y/n: ")
            if(q == "n"):
                print("Goodbye!")
                sys.exit()       
            if(q == "y"):
                clear()
                calcFilled = False
                break
            if(q != "y" and q != "n" and q != "Y" and q != "N"):
                print("Invalid input")
                continue
            if(q == ""):
                print("Invalid input")
                continue
            
            print("Goodbye!")
            sys.exit()
        if(t == "y"):
            ct = True
            valid = False
            while(valid == False):
                opand = input("opand = ")
                if(opand != "+" and opand != "-" and opand != "*" and opand != "/" and opand != "x" and opand != "X"):
                    print("Invalid input | enter a valid operator")
                    continue
                else:
                    valid = True
                    
                if(opand.lower() == "x"):
                    opand = "*"  
                         
                yVal = False
                while (yVal == False):
                    try:
                        y = int(input("y = "))
                        yVal = True
                    except:
                        print("Invalid input")
                        yVal = False 
                                                    
        print("Calculating...")
        time.sleep(1)
        clear()
        sum = eval(f"{sum}{opand}{y}")
        print(sum)
        ct = False

    

    