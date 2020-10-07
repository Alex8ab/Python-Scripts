import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

profit_losses = []
date = []
grtst_increase = 0
grtst_decrease = 0
total = 0
change = []

with open(budget_csv, "r", encoding = "UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    # Skip the header
    csv_header = next(csv_reader)    
    
    for row in csv_reader:
        date.append(row[0])
        profit_losses.append(float(row[1]))    

for i in range(1, len(profit_losses)):    
    change.append(profit_losses[i] - profit_losses[i-1])

# Calculation
total = round(sum(profit_losses), 2)
average_change = round(sum(change) / len(change), 2)
grtst_increase = max(change)
grtst_decrease = min(change)
i_increase = change.index(grtst_increase)
i_decrease = change.index(grtst_decrease)
grtst_increase = round(grtst_increase, 2)
grtst_decrease = round(grtst_decrease, 2)

# Printing in terminal
print(f"""Financial Analysis  
---------------------------- 
Total Months:  {str(len(date))}
Total: $ {str(total)}  
Average Changes: $ {str(average_change)} 
Greatest Increase in Profits: {date[i_increase + 1]} (${grtst_increase})
Greatest Decrease in Profits: {date[i_decrease + 1]} (${grtst_increase})
""")

# Appending the rows to print into text file
print_rows = []
print_rows.append("Financial Analysis")
print_rows.append("----------------------------")
print_rows.append("Total Months: " + str(len(date)))
print_rows.append("Total: $" + str(total))
print_rows.append("Average Changes: $" + str(average_change))
print_rows.append("Greatest Increase in Profits: " + date[i_increase + 1] + " ($" + str(round(grtst_increase, 2)) + ")")
print_rows.append("Greatest Decrease in Profits: " + date[i_decrease + 1] + " ($" + str(round(grtst_decrease, 2)) + ")")
zip_rows = zip(print_rows)

# Printing in a text file
output_file = os.path.join("analysis", "result.txt")
with open(output_file, "w", newline="\n") as file:
    csv_writer = csv.writer(file)    
    csv_writer.writerows(zip_rows)