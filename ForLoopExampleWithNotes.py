# Weekly Sales Analyzer

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# A list of all days in the week — used to prompt the user and label the sales

sales = []
# An empty list to store the sales input by the user for each day

# 1. Get user input using a loop
print("📊 Enter your sales for each day of the week:")
# Print a header message for the user

for day in days:
    # Loop over each day in the 'days' list
    # Read for as "for each"
    amount = float(input(f"{day}: $"))
    # Ask the user to enter sales for that day. Use float() to allow decimal values.
    # The f-string (f"{day}") automatically plugs in the current day name.
    sales.append(amount)
    # Add that day's sales to the 'sales' list

# 2. Calculate total and average sales
total_sales = 0
# Start a variable at 0 to hold the sum of all sales

for amount in sales:
    # Loop through each value in the 'sales' list
    # for "each" amount
    total_sales += amount
    # Add that amount to the total_sales variable

average_sales = total_sales / len(sales)
# Calculate average by dividing total sales by the number of days (7)
# len gets the length of the sales list which is 7 objects(days)

# 3. Find best day
best_day_index = 0
# Start by assuming the first day has the highest sales

for i in range(1, len(sales)):
    # Loop through the sales list starting from the second item (index 1)
    if sales[i] > sales[best_day_index]:
        # If current day's sales are higher than the previous best
        best_day_index = i
        # Update best_day_index to the new best day

# 4. Print report
print("\n📈 Weekly Sales Report")
# Print a blank line and a heading for the sales report

print("-------------------------")
# Just a visual divider

print(f"Total Sales: ${total_sales:.2f}")
# Print total sales, rounded to 2 decimal places

print(f"Average Daily Sales: ${average_sales:.2f}")
# Print average daily sales, also formatted to 2 decimal places

print(f"Best Day: {days[best_day_index]} (${sales[best_day_index]:.2f})")
# Print the best day (get name from 'days' using index) and its sales amount

# 5. Give a simple recommendation
if average_sales < 100:
    # If the average is under $100, give a tip
    print("💡 Tip: Consider a small promotion mid-week to boost traffic.")
else:
    # Otherwise, give positive feedback
    print("✅ Great job keeping daily sales healthy! Keep it up.")
