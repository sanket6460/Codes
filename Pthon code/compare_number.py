#Python Program to Compare three number

def comp_nums(num1,num2,num3): #function working on comparison
    
    if (num1 > num2) and (num1 > num3):
        if (num1 < num2) and (num1 < num3):
            print(num1," is smallest number between given number")
        elif (num2 < num1) and (num2 < num3):
            print(num2," is smallest number between given number")
        else:
            print(num3," is smallest number between given number")
            
        print("%d is greatest number between given number " %(num1))
    elif (num2 >num1) and (num2 >num3):
        if (num1 < num2) and (num1 < num3):
            print(num1," is smallest number between given number")
        elif (num2 < num1) and (num2 < num3):
            print(num2," is smallest number between given number")
        else:
            print(num3," is smallest number between given number")
            
        print("%d is greatest number between given number " %(num2))
    else:
        print("%d is greatest number between given number " %(num3))
        if (num1 < num2) and (num1 < num3):
            print(num1," is smallest number between given number")
        elif (num2 < num1) and (num2 < num3):
            print(num2," is smallest number between given number")
        else:
            print(num3," is smallest number between given number")
        

numbers = input("Enter three numbers :").split()
a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])

comp_nums(a,b,c) #calling of function
        
    
