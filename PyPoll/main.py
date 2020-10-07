import os
import csv

budget_csv = os.path.join("Resources", "election_data.csv")

voter_id = []
county = []
candidate = []

countKhan = 0
countCorrey = 0
countLi = 0
countTooley = 0

with open(budget_csv, "r", encoding = "UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    # Skip the header
    csv_header = next(csv_reader)    
    
    for row in csv_reader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])    

# i_increase = candidate.index("Li")
# print(i_increase)


for i in range(len(candidate)):

    if candidate[i] == 'Khan':
        countKhan += 1
    elif candidate[i] == 'Correy':
        countCorrey += 1
    elif candidate[i] == 'Li':
        countLi += 1
    else:
        countTooley += 1

# Calculation
total = countKhan + countCorrey + countLi + countTooley
Khan_percent = round(countKhan / total * 100, 3)
Correy_percent = round(countCorrey / total * 100, 3)
Li_percent = round(countLi / total * 100, 3)
Tooley_percent = round(countTooley / total * 100, 3)

# Printing in terminal
print(f"""Election Results
-------------------------
Total Votes:  {str(total)}
-------------------------
Khan: {str(Khan_percent)}% ({countKhan})
Correy: {str(Correy_percent)}% ({countCorrey})
Li: {str(Li_percent)}% ({countLi})
O'Tooley: {str(Tooley_percent)}% ({countTooley})
-------------------------
Winner: Khan
-------------------------
""")
# Appending the rows to print into text file
print_rows = []
print_rows.append("Election Results")
print_rows.append("-------------------------")
print_rows.append("Total Votes: " + str(total))
print_rows.append("-------------------------")
print_rows.append("Khan: " + str(Khan_percent) + "% (" + str(countKhan) + ")" )
print_rows.append("Correy: " + str(Correy_percent) + "% (" + str(countCorrey) + ")" )
print_rows.append("Li: " + str(Li_percent) + "% (" + str(countLi) + ")" )
print_rows.append("O'Tooley: " + str(Tooley_percent) + "% (" + str(countTooley) + ")" )
print_rows.append("-------------------------")
print_rows.append("Winner: Khan")
print_rows.append("-------------------------")
zip_rows = zip(print_rows)

# Printing in a text file
output_file = os.path.join("analysis", "result.txt")
with open(output_file, "w", newline="\n") as file:
    csv_writer = csv.writer(file)    
    csv_writer.writerows(zip_rows)