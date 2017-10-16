operation = raw_input("Choose math operation (+, -, *, /): ")

x = int(raw_input("Enter the value for x: "))
y = int(raw_input("Enter the value for y: "))
#
# print (x+y)

if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "*":
    print(x * y)
elif operation == ("/"):
    print(x / y)
else:
    print ("Not Ok")
    raise ValueError("Wrong operation!")
