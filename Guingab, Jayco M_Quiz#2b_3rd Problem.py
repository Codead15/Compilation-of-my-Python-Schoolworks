#Jayco M. Guingab

max_num = int(input("Enter a number: "))

print("Output:")
current = 2
for i in range(1, max_num + 1):
    for j in range(1, i + 1):
        print(current, end="\t")
        current += 2
    print()
    
for i in range(max_num - 1, 0, -1):
    for j in range(i, 0, -1):
        print(current, end="\t")
        current += 2
    print()
