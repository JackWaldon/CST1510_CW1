def add(n1, n2):
    return n1+n2
def subtract(n1, n2):
    return n1-n2
def multiplation(n1, n2):
    return n1*n2
def divition (n1, n2):
    return n1/n2

n1 = float(input ("give me your first number:  "))
keep_going = True

while keep_going:
    oporator = input ("pick one: + - * / -- ")
    n2 = float(input ("give me your second number:  "))
    if oporator == "+":
        result = add(n1, n2)
    elif oporator == "-":
        result = subtract(n1, n2)
    elif oporator == "*":
        result = multiplation(n1, n2)
    elif oporator == "/":
        result = divition(n1, n2)
    else:
        print("invalid oporator")
        continue
    print(f"the answer is {result}")
    n1 = result
    cont = input("input y to continue")
    if cont == "y":
        continue
    else:
        break

