def openaccount():
    name = input("Enter full name: ")
    acc_no = input("Enter desired account number: ")
    with open("accounts.txt", "a") as f:
        f.write(f"{acc_no},{name},0\n")
    print(f"Account {acc_no} created for {name}.")
