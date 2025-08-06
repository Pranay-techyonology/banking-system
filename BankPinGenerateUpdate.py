def pingenerate():
    acc_no = input("Enter account number: ")
    pin = input("Set your 4-digit PIN: ")
    with open("pins.txt", "a") as f:
        f.write(f"{acc_no},{pin}\n")
    print("PIN set successfully.")

def pinupdate():
    acc_no = input("Enter account number: ")
    new_pin = input("Enter new 4-digit PIN: ")
    lines = []
    found = False
    with open("pins.txt", "r") as f:
        lines = f.readlines()
    with open("pins.txt", "w") as f:
        for line in lines:
            if line.startswith(acc_no + ","):
                f.write(f"{acc_no},{new_pin}\n")
                found = True
            else:
                f.write(line)
    if found:
        print("PIN updated successfully.")
    else:
        print("Account not found.")
