#JAN ROLF V. BALUNES 							
#JAYCO MORAL GUINGAB

#BSIT 2-1
#INTEGRATIVE ACT #6

def ADD_record():
    with open("Products.txt", "a") as file_handler:
        while True:
            prod_code = input("PRODUCT CODE: ")
            prod_name = input("PRODUCT NAME: ")
            prod_quantity = input("QUANTITY: ")
            file_handler.write(f"{prod_code},{prod_name},{prod_quantity}\n")

            while True:
                input_more = input("\nEnter more? [Y/N]: ")
                if input_more == "Y":
                    break
                elif input_more == "N":
                    return
                else:
                    print("\nInvalid input. Only 'Y' or 'N' are accepted.")

def DELETE_record():
    prod_code = input("\nEnter the product code to delete: ")
    rec_found = False
    with open("Products.txt", "r") as file:
        record_lines = file.readlines()

    with open("Products.txt", "w") as file_handler:
        for line in record_lines:
            code, _, _ = line.strip().split(",")
            if code == prod_code:
                rec_found = True
                user_confirmation = input(f"\nProduct found:\n{line}Do you want to delete this record? [Y/N]: ")
                while user_confirmation not in ["Y", "N"]:
                    print("\nInvalid input. Please enter Y or N.")
                    user_confirmation = input("\nDo you want to delete this record? [Y/N]: ")
                if user_confirmation == "Y":
                    continue
            file_handler.write(line)

    if not rec_found:
        print("\nRecord not found.")

def EDIT_record():
    prod_code = input("\nEnter the product code to edit: ")
    rec_found = False
    with open("Products.txt", "r") as file:
        record_lines = file.readlines()

    with open("Products.txt", "w") as file_handler:
        for line in record_lines:
            code, name, quantity = line.strip().split(",")
            if code == prod_code:
                rec_found = True
                print(f"\nCurrent record:\n{line}")
                updated_name = input("Enter new product name: ")
                update_quantity = input("Enter new quantity: ")
                line = f"{code},{updated_name},{update_quantity}\n"
            file_handler.write(line)

    if not rec_found:
        print("\nRecord not found.")

def TRANSACT_record():
    prod_code = input("\nPRODUCT CODE: ")
    trans_code = input("TRANSACTION CODE (P for Purchase, S for Sold): ")
    quantity = int(input("QUANTITY: "))

    rec_found = False
    with open("Products.txt", "r") as file:
        record_lines = file.readlines()

    with open("Products.txt", "w") as file_handler:
        for line in record_lines:
            code, name, current_quantity = line.strip().split(",")
            if code == prod_code:
                rec_found = True
                current_quantity = int(current_quantity)
                if trans_code == "P":
                    new_quantity = current_quantity + quantity
                elif trans_code == "S":
                    new_quantity = current_quantity - quantity
                else:
                    print("\nInvalid transaction code. Only 'P' or 'S' are accepted.")
                    break
                line = f"{code},{name},{new_quantity}\n"
            file_handler.write(line)

    if not rec_found:
        print("\nRecord not found.")

try:
    while True:
        print("Options:")
        print("A - ADD")
        print("D - DELETE")
        print("E - EDIT")
        print("T - TRANSACT")
        print("X - EXIT")

        choice = input("WHAT DO YOU WANT TO DO? ")

        if choice == "A":
            ADD_record()
        elif choice == "D":
            DELETE_record()
        elif choice == "E":
            EDIT_record()
        elif choice == "T":
            TRANSACT_record()
        elif choice == "X":
            with open("Products.txt", "r") as file:
                print("\nUpdated file contents:")
                print(file.read())
            print("\nEnd of program.")
            break
        else:
            print("\nInvalid choice. Please try again.")

except Exception as e:
    print("\nAn error occurred:", str(e))
