import os
import csv
pybank = os.path.join("budget_data.csv")
profit_losses = []
change_pnl = []
i = 0
total_month = 0
month_list = []
avg_change = 0
total_pnl = 0
pnlchange = 0
top_profit = 0
bottom_profit = 0
month_top_profit = 0
month_bottom_profit = 0

with open(pybank, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)
    for row in csv_reader:
        total_month = total_month +1
        profit_losses.append(int(row[1]))
        month_list.append(row[0])
        total_pnl = sum(profit_losses)
    for i in range(len(profit_losses)-1):
        pnlchange = (profit_losses[i+1]) - (profit_losses[i])
        change_pnl.append(pnlchange)
        avg_change = sum(change_pnl) / (total_month - 1)    
    
    top_profit = max(change_pnl)
    month_top_profit = change_pnl.index(top_profit) + 1
    bottom_profit = min(change_pnl)
    month_bottom_profit = change_pnl.index(bottom_profit) + 1
        
    print(f"Total Months: {total_month}")
    print(f"Total P/L: ${total_pnl}")
    print(f"Average Change: ${avg_change: .2f}")
    print(f"Greatest Increase in Profits: {month_list[month_top_profit]} $({top_profit: .2f})")
    print(f"Greatest Decrease in Profits: {month_list[month_bottom_profit]} $({bottom_profit: .2f})")
  
output_file = os.path.join("Financial Analysis.txt")

with open(output_file,"w") as f:

    f.write("Financial Analysis")
    f.write("\n")
    f.write(f"----------------------------")
    f.write("\n")
    f.write(f"Total Months: {total_month}")
    f.write("\n")
    f.write(f"----------------------------")
    f.write("\n")
    f.write(f"Total P/L: ${total_pnl}")
    f.write("\n")
    f.write(f"Average Change: ${avg_change: .2f}")
    f.write("\n")
    f.write(f"Greatest Increase in Profits: {month_list[month_top_profit]} $({top_profit: .2f})")
    f.write("\n")
    f.write(f"Greatest Decrease in Profits: {month_list[month_bottom_profit]} $({bottom_profit: .2f})")
    f.write("\n")


