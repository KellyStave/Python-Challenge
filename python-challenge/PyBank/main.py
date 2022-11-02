#import csv file
import os , csv
csvpath = r'C:\Users\stave\Python-Challenge\python-challenge\PyBank\Resources\budget_data.csv'
#create variables and lists
months = 0.0
total = 0.0
date =[]
profit_losses = []
change={}
#open csv file
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    print(csvreader)
    #calculate total months and total profits/losses
    for row in csvreader:
        months += 1
        total += int(row[1])
    print("Total Months: " + str(months))
    print("Total: $" + str(total))
    #create list of profits/losses
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    for col in csvreader:
        profit_losses.append(int(col[1]))
        date.append(col[0])
#calculate average change in profits/losses
finalProfLoss = 0.00
finalProfLoss = (profit_losses[85] - profit_losses[0])/months
counter = 0
change_calc = []
lenght = len(profit_losses)
lenght -= 1
#calculate greatest increase and decrease
while counter < lenght:
    change_calc.append(profit_losses[counter + 1] - profit_losses [counter])
    counter += 1
finalProfLoss = round(finalProfLoss, 2)
maxProfit = date[change_calc.index(max(change_calc)) + 1]
#print financial analysis
print("Financial Analysis")
print("---------------------")
print("Total Months: " + str(months))
print("Total: $" + str(total))
print("Average Change: $" + str(finalProfLoss))
print("Greatest Increase in Profits: " + date[change_calc.index(max(change_calc)) + 1] + " ($" + str(max(change_calc)) + ")" )
print("Greatest Decrease in Profits: " + date[change_calc.index(min(change_calc)) + 1] + " ($" + str(min(change_calc)) + ")" )
#write financial analysis to folder
with open(r'C:\Users\stave\Python-Challenge\Python-Challenge-1\python-challenge\PyBank\analysis\ReadMe.txt', 'w') as f:
    f.write("""Financial Analysis
--------------------- 
Total Months: """ + str(months)  + """ 
Average Change: $""" + str(finalProfLoss) + """
Greatest Increase in Profits: """ + date[change_calc.index(max(change_calc)) + 1] + " ($" + str(max(change_calc)) + """)
Greatest Decrease in Profits: """ + date[change_calc.index(min(change_calc)) + 1] + " ($" + str(min(change_calc)) + ")""")
