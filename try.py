while True:
    number = int(input("Enter a number: "))

    # First half of the pattern
    for x in range(1, number+1):
        for y in range(1, x+1):
            print(y, end=' ')
        print(" ")

    # Second half of the pattern
    for x in range(number-1, 0, -1):
        for y in range(1, x+1):
            print(y, end=' ')
        print(" ")

    # Input validation for continue prompt
    while True:
        answer = input("Continue? [Y/N]: ").upper()
        if answer == 'N' or answer == 'Y':
            break
        print("Invalid input. Please enter Y or N only.")

    if answer == 'N':
        break
