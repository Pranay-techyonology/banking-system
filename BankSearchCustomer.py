def search():
    acc_no = input("Enter account number to search: ")
    with open("accounts.txt", "r") as f:
        for line in f:
            parts = line.strip().split(',')
            if parts[0] == acc_no:
                print(f"Account: {parts[0]}, Name: {parts[1]}, Balance: ₹{parts[2]}")
                return
    print("Account not found.")
