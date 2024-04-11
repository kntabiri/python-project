import sys

def add (num1, num2):
    add = num1 + num2
    return add

def sub (num1, num2):
    sub = num1 - num2
    return sub

def mul (num1, num2):
    mul = num1 * num2 
    return mul

# # print(add (5,10))
# # print(sub(10,5))
# # print(mul(10,5))

# num1 = int(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])

if operation == "sub":
    output = sub(num2,num1)
    print(output)

# python3 calculator-new.py 4 sub 1 to execute a command line arg
