## program to print multiplication table

print("Welcome to multiplication table program")

n = int(input("Enter table number: "))

print("===========================")
i = 1  ## START
while i < 11:   ## END CONDITION
    print(f"{n} x {i} = {n*i}")
    i = i+1   ## STEP
print("===========================")