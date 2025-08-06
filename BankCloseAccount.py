def closeaccount():
    acc_no = input("Enter account number to close: ")
    lines = []
    found = False
    with open("accounts.txt", "r") as f:
        lines = f.readlines()
    with open("accounts.txt", "w") as f:
        for line in lines:
            if not line.startswith(acc_no + ","):
                f.write(line)
            else:
                found = True
    if found:
        print(f"Account {acc_no} closed.")
    else:
        print("Account not found.")
