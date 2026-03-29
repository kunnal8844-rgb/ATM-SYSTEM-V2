class Atm:
    def __init__(self):
        self.__pin = None
        self.__balance = 0
        self.__transactions = []

    def __verify_pin(self):
        """Private helper to verify PIN and reduce code repetition."""
        if self.__pin is None:
            print("Error: No PIN set. Please create a PIN first.")
            return False
        
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.__pin:
            return True
        print("Invalid PIN.")
        return False

    def create_pin(self):
        new_pin = input("Set your 4-digit PIN: ")
        if len(new_pin) == 4 and new_pin.isdigit():
            self.__pin = new_pin
            print("PIN created successfully!")
        else:
            print("Invalid PIN format. Use 4 digits.")

    def deposit(self):
        if self.__verify_pin():
            try:
                amount = float(input("Enter amount to deposit: "))
                if amount > 0:
                    self.__balance += amount
                    self.__transactions.append(f"Deposited{amount}")
                    print(f"₹{amount} deposited. New balance: ₹{self.__balance}")
                else:
                    print("Amount must be positive.")
            except ValueError:
                print("Invalid input. Please enter a numerical value.")

    def withdraw(self):
        if self.__verify_pin():
            try:
                amount = float(input("Enter amount to withdraw: "))
                if 0 < amount <= self.__balance:
                    self.__balance -= amount
                    self.__transactions.append(f"Withdraw{amount}")
                    print(f"₹{amount} withdrawn. Remaining balance: ₹{self.__balance}")
                else:
                    print("Insufficient funds or invalid amount.")
            except ValueError:
                print("Invalid input.")

    def check_balance(self):
        if self.__verify_pin():
            print(f"Current Balance: ₹{self.__balance}")

    def show_transactions(self):
        if self.__verify_pin():
            if not self.__transactions:
                print("NO transactions")     
            else:
                for t in self.__transactions:
                    print(t)

# --- External Logic to Run the Program ---
def main():
    sbi = Atm()
    menu = """
    ---- ATM MENU ----
    1. Create PIN
    2. Deposit
    3. Withdraw
    4. Check Balance
    5. show transaction
    6.Exit
    Choose an option: """

    while True:
        choice = input(menu)
        if choice == "1": sbi.create_pin()
        elif choice == "2": sbi.deposit()
        elif choice == "3": sbi.withdraw()
        elif choice == "4": sbi.check_balance()
        elif choice == "5": sbi.show_transactions()
        elif choice == "6":
            print("Exiting. Have a nice day!")
            break
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()
