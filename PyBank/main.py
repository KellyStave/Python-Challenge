
import os , csv
#from tkinter.tix import COLUMN
csvpath = r'C:\Users\stave\Python-Challenge\python-challenge\PyBank\Resources\budget_data.csv'
months = 0.0
total = 0.0
#date = {"Date": [], "Profit Losses": []}
date =[]
profit_losses = []
change={}
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    print(csvreader)
    for row in csvreader:
        months += 1
        total += int(row[1])
    print("Total Months: " + str(months))
    print("Total: $" + str(total))
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    for col in csvreader:
        profit_losses.append(int(col[1]))
        date.append(col[0])
finalProfLoss = 0.00
finalProfLoss = (profit_losses[85] - profit_losses[0])/months
counter = 0
change_calc = []
lenght = len(profit_losses)
lenght -= 1

while counter < lenght:
    change_calc.append(profit_losses[counter + 1] - profit_losses [counter])
    counter += 1
finalProfLoss = round(finalProfLoss, 2)
print("Average Change: $" + str(finalProfLoss))
print("Greatest Increase in Profits: " + date[change_calc.index(max(change_calc)) + 1] + " ($" + str(max(change_calc)) + ")" )
print("Greatest Decrease in Profits: " + date[change_calc.index(min(change_calc)) + 1] + " ($" + str(min(change_calc)) + ")" )


