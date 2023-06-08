class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, new_name):
        self.name = new_name
        return new_name


    def change_pin(self, new_pin):
        self.pin = new_pin


    def change_password(self, password):
        self.password = password


class BankUser(User):
    def __init__(self, name, pin, password,):
        super().__init__(name, pin, password)
        self.balance = 0.0

    def show_balance(self):
        print(f"{self.name} has an account balance of: {self.balance}")

    def withdraw(self, amount):
        while self.balance > 0:
            self.balance -= amount
            self.show_balance()
            return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.show_balance()

    # We passed another instance of bank user(user_receiving).
    def transfer_money(self, amount, user_receiving,):
        # Then to get the name we did dot.name that jumps to the bank users name.
        print(f"You are transferring {amount} to {user_receiving.name}")
        authenticate = int(input("Authentication required\nEnter your PIN: "))
        if self.pin == authenticate:
            print("Transfer authorized")
            print(f"Transferring ${amount} to {user_receiving.name}")
            # Withdrew from self.account with amount as its parameter value, that is called with the code below.
            self.withdraw(amount)
            # We deposit to the receiving user with amount as its parameter value
            user_receiving.deposit(amount)
            return True
        else:
            print("Invalid PIN. Transaction canceled.")
            self.show_balance()
            user_receiving.show_balance()
            return False

    def request_money(self, amount, requesting_from_user, ):
        print(f"You are requesting ${amount} from {requesting_from_user.name}")
        print("User authentication is required... ")
        pin_input = int(input(f"Enter {requesting_from_user.name}'s PIN..."))
        if pin_input != requesting_from_user.pin:
            print("Invalid PIN. Transaction canceled.")
            self.show_balance()
            requesting_from_user.show_balance()
            return
        password_input = input("Enter your password: ")
        if password_input == self.password:
            print("Request authorized")
            print(f"{requesting_from_user.name} sent ${amount}")
            self.deposit(amount)
            requesting_from_user.withdraw(amount)
        else:
            print("Invalid password. Transaction canceled.")
            self.show_balance()
            requesting_from_user.show_balance()
            return








"""
Driver Code for Task 1
user1 = User("Bob", 1234, "password")
print(user1.name, user1.pin, user1.password)
#vars returns the values in dic order.
print(vars(user1))

"""


"""
Driver Code for Task 2

new_name = input("Enter new Username: ")
user1.change_name(new_name)


new_pin = int(input("Enter new Pin: "))
user1.change_pin(new_pin)

new_password = input("Enter new Password: ")
user1.change_password(new_password)

print(user1.name, user1.pin, user1.password)

"""

"""
#Driver Code for Task 3
user1 = BankUser("Bob", 1234, "password")
print(user1.name, user1.pin, user1.password, user1.balance)

"""

""""
user1 = BankUser("Bob", 1234, "password")
user1.show_balance()
user1.deposit(1000)
user1.withdraw(500)
user1.show_balance()
"""

user1 = BankUser("Alice", 1234, "password")
user2 = BankUser("Bob", 4321, "bobpassword")
user1.deposit(5000)
user2.show_balance()
print()
if user1.transfer_money(500, user2):
    print()
    user1.request_money(250, user2)



