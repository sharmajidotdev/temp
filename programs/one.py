### Toolbox
print("===========================")
print("WELCOME to Toolbox")
print("===========================")
choice = 0

student = [
    [
        "saurabh",'CS',26
    ],
    [

    ],

]
while choice != 5:
    print("""
1. add  
2. sub
3. mul
4. div
6. show
5. exit
""")
    choice = int(input("Enter Choice: "))
    if choice == 1:
        print("add")
        student.append(input("enter name:"))
    elif choice == 2:
        print("sub")
        student.pop()
    elif choice == 3:
        print("mul")
    elif choice == 4:
        print("div")
    elif choice == 6:
        print(student)