def viewcustomers():
    print("All Customers:")
    with open("accounts.txt", "r") as f:
        for line in f:
            parts = line.strip().split(',')
            print(f"Account: {parts[0]}, Name: {parts[1]}, Balance: ₹{parts[2]}")
