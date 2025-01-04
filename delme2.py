## TYPES OF FUNCTIONS

## 4 types
# 1. With {Argument/parameter} && no {return}
# 2. With {Argument/parameter} && with {return}
# 3. No {Argument/parameter} && with {return}
# 4. No {Argument/parameter} && no {return}


## =================================
# With argument && no return

def add(num1,num2):
    total = num1+num2
    print(total)

# num1 = int(input("e"))
# num2 = int(input("en"))
# add(num1,num2)
## =================================
# With argument && with return
def add2(num1,num2):
    total = num1+num2
    return total

# ## INPUT
# num1 = int(input("e"))
# num2 = int(input("en"))

# ## PROCESS
# catch = add2(num1, num2)

# ## OUTPUT
# print(catch)

# print(add2(int(input("num1: ")), int(input("num2: "))))

## =================================
# No {Argument/parameter} && with {return}

def add3():
    num1 = int(input("num1:"))
    num2 = int(input("num2:"))
    total = num1+num2
    return total

# abc = add3()
# print(abc)

## =================================
#  No {Argument/parameter} && no {return}

def greetings():
    print("uh, dhan dhandhan")

# greetings()
