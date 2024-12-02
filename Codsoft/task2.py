def calc():
   
    n=int(input("enter number of operations you want to perform :")) 

    for i in range (1, n+1):
        a=int(input("enter first number "))
        b=int(input("enter second number "))
    
        operator=input("enter operator: + , - , * , /, %  ")
   
        if operator == "+":
            print(f"{a} + {b} = {a+b}")

        elif operator == "-":
            print(f"{a} - {b} = {a-b}")

        elif operator == "*":
            print(f"{a} * {b} = {a*b}")

        elif operator == "/":
            print(f"{a} / {b} = {a/b:.2f}")

        elif operator == "%":
            print(f"{a} % {b} = {a%b:.2f}")
        
        else:
            print("enter a valid operator")

     
    
calc()