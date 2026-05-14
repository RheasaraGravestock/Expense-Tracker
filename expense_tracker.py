import csv

def get_expense():
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    return {
        "category": category,
        "amount": amount,
        "description": description
    }


def display_expenses(expenses):
    print()
    print("ALL EXPENSES")

    for expense in expenses:
        print("Category:", expense["category"])
        print("Amount:", expense["amount"])
        print("Description:", expense["description"])
        print()


def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]
    
    return total


def get_continue_choice():
    while True:
        choice = input("Add another expense? (y/n): ").strip().lower()

        if choice in ["y", "yes", "no", "n"]:
            return choice
        
        print("Please enter yes/y or no/n.")


def save_to_csv(expenses):
    file = open("expenses.csv", "w", newline="")
    writer = csv.writer(file)

    writer.writerow(["Category", "Amount", "Description"])

    for expense in expenses:
        writer.writerow([
            expense["category"],
            expense["amount"],
            expense["description"]
        ])

    file.close()


def main():
    print("Expense Tracker")

    expenses = []

    while True:
        expense = get_expense()
        expenses.append(expense)

        choice = get_continue_choice()

        if choice in ["n", "no"]:
            break

    display_expenses(expenses)

    total = calculate_total(expenses)
    print("Total spent: ", total)

    save_to_csv(expenses)

if __name__ == "__main__":
    main()
