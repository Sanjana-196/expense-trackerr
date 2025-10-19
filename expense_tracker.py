# expense_tracker.py
print("===== Personal Expense Tracker =====")

# Step 1: Get number of expense entries
num_expenses = int(input("How many expenses do you want to add? "))

# Step 2: Store expenses in a list
expenses = []
for i in range(num_expenses):
    print(f"\nEnter details for expense {i+1}:")
    date = input("Date (DD-MM-YYYY): ")
    category = input("Category (e.g., Food, Travel, Shopping, Bills): ")
    amount = float(input("Amount spent: "))
    note = input("Short note about this expense: ")
    
    expense = {
        "date": date,
        "category": category.capitalize(),
        "amount": amount,
        "note": note
    }
    expenses.append(expense)

# Step 3: Calculate total spending
total_spent = sum(item["amount"] for item in expenses)

# Step 4: Calculate spending per category
category_summary = {}
for item in expenses:
    cat = item["category"]
    category_summary[cat] = category_summary.get(cat, 0) + item["amount"]

# Step 5: Display all entered expenses
print("\n===== Expense Summary =====")
for i, item in enumerate(expenses, start=1):
    print(f"{i}. Date: {item['date']} | Category: {item['category']} | Amount: ₹{item['amount']:.2f} | Note: {item['note']}")

# Step 6: Display totals
print("\n----- Total Spending -----")
print(f"Total Amount Spent: ₹{total_spent:.2f}")

print("\n----- Category-wise Breakdown -----")
for cat, amt in category_summary.items():
    print(f"{cat}: ₹{amt:.2f}")

print("\n✅ Expense tracking complete!")
