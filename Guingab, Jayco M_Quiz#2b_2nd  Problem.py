#Jayco M. Guingab

rows_no = int(input("Enter a number: "))


for i in range(1, rows_no+1):
    print(" "*(rows_no-i), end="")
    for j in range(1, i*2):
        print("*", end="")
    print()


for i in range(rows_no-1, 0, -1):
    print(" "*(rows_no-i), end="")
    for j in range(1, i*2):
        print("*", end="")
    print()




    
