import math
print("===== Calculator =====")

#user input
print("which operation you want to perform")
print('''
      "+" for Addition\n
      "-" for Subtraction \n
      "*" for Multiplication\n
      "/" for Division\n
      "%" for Modulus\n 
      "**" for Power\n
      "//" for floor value\n
      "^" for sqrt\n  
''')

ch = input("Press the operator: ")
print("You selected:", ch)
#get the numbers to perform operation
if ch == "^":
    num = float(input("Enter a number: "))
else:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

#calculation
match(ch):
    case "+":
        print("Result:",num1+num2)
    case "-":
        print("Result:",num1-num2)
    case "*":
        print("Result:",num1*num2)
    case "/": 
        if num2!=0:
            print("Result:",num1/num2)
        else:
            print("Error! Cannot divide by zero")
    case "%":
        if num2!=0:
            print("Result:",num1%num2)
        else:
            print("Error! Cannot divide by zero")
    case "**":
        print("Result:",num1**num2)
    case "//":
        if num2!=0:
         print("Result:",num1//num2)
        else:
          print("Error! Cannot divide by zero")
    case "^":
         print(math.sqrt(num))
    case _:
        print("Inavalid choice :Try Again!!! ")


