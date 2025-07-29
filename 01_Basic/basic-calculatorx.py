a = input("entre the first value ")
a = int(a)

c = input("Enter the operation: ")

b = input("entre the second value ")
b = int(b)

if c == '+':
    result = a + b
elif c == '-':
    result = a - b
elif c == '*':
    result = a * b
elif c == '/':
    result = a / b
else:
    result = "Please enter valid operation"

print(result)


# c = a + b 
# print("the sum of first and second value is",c)
# d = a - b 
# print("the sustract first and second value is ",d)
# r = a * b 
# print("the multipication of first and second value is ",r)
# y = a / b 
# print("the division  of first and second value is ",y)
