n = int(input("Input a number: "))

start = 2  # The first number in the sequence
for i in range(n):
    row = []  # Create an empty row for each iteration
    for j in range(i+1):
        row.append(start)  # Add the next number to the row
        start += 2  # Increment the start number by 2
    print(" ".join(str(num) for num in row))  # Print the row
for i in range(n-1):
    row = []  # Create an empty row for each iteration
    for j in range(n-i-1):
        row.append(start)  # Add the next number to the row
        start += 2  # Increment the start number by 2
    print(" ".join(str(num) for num in row))  # Print the row
