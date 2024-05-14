# Expense Tracker

class Expense:
    def __init__(self, date, des, amt):
        self.date = date
        self.des = des
        self.amt = amt

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            print("Expense removed successfully.")
        else:
            print("Invalid expense index.")

    def view_expenses(self):
        if len(self.expenses) == 0:
            print("No expense found")
        else:
            print("Expense List:")
            for i, expense in enumerate(self.expenses, start=1):
                print(f"{i}. Date: {expense.date}, Description: {expense.des}, Amount: {expense.amt}")

    def total_expenses(self):
        total = sum(expense.amt for expense in self.expenses)
        print(f"Total Expenses: ${total:.2f}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense\n2. Remove Expense\n3. View Expenses\n4. Total Expenses\n5. Exit")

        ch = input("Enter your choice (1-5): ")

        if ch == '1':
            date = input("Enter the date: ")
            des = input("Enter the description: ")
            amt = float(input("Enter the amount: "))
            expense = Expense(date, des, amt)

            tracker.add_expense(expense)
            print("Expense added successfully.")
        elif ch == '2':
            index = int(input("Enter the expense index to remove: "))
            tracker.remove_expense(index - 1)
        elif ch == '3':
            tracker.view_expenses()
        elif ch == '4':
            tracker.total_expenses()
        elif ch == '5':
            print("Good Bye")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 