1#control_statements
#num = 0
#if num > 0:
   # print("The number is positive.")
#elif num == 0:
    #print("The number is zero.")
#else:
    #print("The number is negative.")
    
    #Control Statements part2
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
   
if num1 > num2:
    print(num1, "is greater than", num2) 
elif num2 > num1:
    print(num2, "is greater than", num1)
else:
    print("Both numbers are equal")