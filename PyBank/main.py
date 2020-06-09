import os
import csv

filepath = os.path.join("Resources", "budget_data.csv")

totmonths = 0
nettot = 0
profit = []

previous_profit = 0
monthlychange_profit = 0
profit_change = []
totchange_profit = 0

date = []


with open(filepath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")

    header = next(csvreader)
    

    for row in csvreader:

        totmonths = totmonths + 1

        nettot = nettot + int(row[1])
        profit.append(row[1])

        if (totmonths == 1):
            previous_profit = int(row[1])
            continue

        else:      
  
            present_profit = int(row[1])
            monthlychange_profit = present_profit - previous_profit
            profit_change.append(monthlychange_profit)

            totchange_profit = totchange_profit + monthlychange_profit
            previous_profit = present_profit

            date.append(row[0])

    average_profitchange = totchange_profit/(totmonths-1)
    maxprofit = max(profit_change)
    minprofit = min(profit_change)

    print("Financial Analysis")
    print("---------------------------\n")
    print(f"Total Months: {str(totmonths)}")
    print(f"Total: ${str(nettot)}")
    print(f"Average Change: ${str(round(average_profitchange, 2))}")
    print(f"Greatest Increase in Profits: {str(date[profit_change.index(maxprofit)])} (${str(maxprofit)})")
    print(f"Greatest Decrease in Profits: {str(date[profit_change.index(minprofit)])} (${str(minprofit)})")

txtpath = os.path.join("analysis", "result.txt")
with open(txtpath, "w") as txtfile:

    txtfile.write("Financial Analysis\n")
    txtfile.write("---------------------------------------------------\n")
    txtfile.write(f"Total Months: {str(totmonths)}\n")
    txtfile.write(f"Total: ${str(nettot)}\n")
    txtfile.write(f"Average Change: ${str(round(average_profitchange, 2))}\n")
    txtfile.write(f"Greatest Increase in Profits: {str(date[profit_change.index(maxprofit)])} (${str(maxprofit)})\n")
    txtfile.write(f"Greatest Decrease in Profits: {str(date[profit_change.index(minprofit)])} (${str(minprofit)})")
