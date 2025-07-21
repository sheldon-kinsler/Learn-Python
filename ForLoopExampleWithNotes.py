# Weekly Sales Analyzer

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] #A list of all days in the week — used to prompt the user and label the sales

sales = [] #An empty list to store the sales input by the user for each day

print("📊 Enter your sales for each day of the week:") #Print a header message for the user

# 1. Get user input using a loop
for day in days: #Loop over each day in the 'days' list. Read for as "for each"
    amount = float(input(f"{day}: $"))   #Prompts user to enter sales amount for that day. Use float() to allow decimal values. Displays $ sign before the number user enters
    # The f-string (f"{day}") automatically plugs in the current day name. Shows each day after each line as it moves through loop
    sales.append(amount) #Add that day's sales to the 'sales' list. For example will add 100 to the sales list if user enters 100

# 2. Calculate total and average sales
total_sales = 0 #Start a variable at 0 since there are no sales yet

for amount in sales: #Loop through each value in the 'sales' list. Read as for "each" amount
    total_sales += amount #Adds that amount to the total_sales variable. If user entered 100 for Monday and 200 for Tuesday, will add 100 + 200 to sales list. So the 0 would become 300

average_sales = total_sales / len(sales)
# Calculate average sales by dividing total sales by the number of days (7)
# len gets the length of the sales list which is 7 objects(days)

# 3. Find best day
best_day_index = 0 #Start by assuming the first day has the highest sales. Lists always start at index 0 on the left. So for this, Monday is at index 0
                   #index number:  0        1          2          3          4         5        6
                   #day:         Monday  tuesday   wednesday   thursday   friday   saturday   sunday

for i in range(1, len(sales)): #Loop through the sales list starting from 1 index, which is the 2nd item, and going the whole length of the sales list. Have to start at 2nd item since we are comparing to previous day
    if sales[i] > sales[best_day_index]: #If current day's sales are higher than the previous best. Boolean statement looks for true or false. best_day_index is currently set at monday or index 0
        #above statement is seeing if tuesday sales are better than monday sales and so on through the list
        #i in sales[i] is a placeholder for current value in the list as we loop through the range
        best_day_index = i #If above statement is true, update best_day_index to the new best day. If tuesday sales are greater than monday sales than best_day_index becomes 1

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
