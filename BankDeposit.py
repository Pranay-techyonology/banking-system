def deposit():
    acc_no = input("Enter account number: ")
    amount = int(input("Enter amount to deposit: "))
    lines = []
    found = False
    with open("accounts.txt", "r") as f:
        lines = f.readlines()
    with open("accounts.txt", "w") as f:
        for line in lines:
            parts = line.strip().split(',')
            if parts[0] == acc_no:
                balance = int(parts[2]) + amount
                f.write(f"{acc_no},{parts[1]},{balance}\n")
                found = True
            else:
                f.write(line)
    if found:
        print(f"Deposited ₹{amount} into account {acc_no}.")
    else:
        print("Account not found.")
