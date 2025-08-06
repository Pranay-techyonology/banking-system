def withdraw():
    acc_no = input("Enter account number: ")
    amount = int(input("Enter amount to withdraw: "))
    lines = []
    found = False
    with open("accounts.txt", "r") as f:
        lines = f.readlines()
    with open("accounts.txt", "w") as f:
        for line in lines:
            parts = line.strip().split(',')
            if parts[0] == acc_no:
                balance = int(parts[2])
                if balance >= amount:
                    balance -= amount
                    f.write(f"{acc_no},{parts[1]},{balance}\n")
                    print(f"Withdrew ₹{amount} from account {acc_no}.")
                else:
                    f.write(line)
                    print("Insufficient balance.")
                found = True
            else:
                f.write(line)
    if not found:
        print("Account not found.")
