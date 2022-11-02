import os , csv
csvpath = r"C:\Users\stave\Python-Challenge\Python-Challenge-1\python-challenge\PyPoll\Resources\election_data.csv"
votes = 0
#candidate1 = 'Charles Casper Stockham'
#candidate2 = 'Diana DeGette'
#candidate3 = 'Raymon Anthony Doane'
count1 = 0
count2 = 0
count3 = 0
candidatelist = []
#open csv file
with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    print(csvreader)
    for row in csvreader:
        #print(row)
        votes += 1

with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    for row in csvreader:
        if row[2] not in candidatelist:
            candidatelist.append(row[2])
       

with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    print(csvreader)
    for row in csvreader:
        for word in row:
            if word == candidatelist[0]:
                count1 += 1
            if word == candidatelist[1]:
                count2 += 1
            if word == candidatelist[2]:
                count3 += 1

percent1 = "{:.3%}".format(count1/votes)
percent2 = "{:.3%}".format(count2/votes)
percent3 = "{:.3%}".format(count3/votes)

print("Election Results")
print("Total Votes: " + str(votes))
print(candidatelist [0] + ": " + percent1 + " (" + str(count1) +")")
print(candidatelist [1] + ": " + percent2 + " (" + str(count2) +")")
print(candidatelist [2] + ": " + percent3 + " (" + str(count3) +")")
print("Winner: " + candidatelist[1])

with open(r'C:\Users\stave\Python-Challenge\Python-Challenge-1\python-challenge\PyPoll\analysis\ReadMe.txt', 'w') as f:
    f.write("""Election Results 
--------------------- 
Total Votes: """ + str(votes) + """ 
---------------------    
""" + (candidatelist [0] + ": " + str(percent1) + " (" + str(count1)) + ")""""
""" + (candidatelist [1] + ": " + str(percent2) + " (" + str(count2)) + ")""""
""" + (candidatelist [2] + ": " + str(percent3) + " (" + str(count3)) + ")""""
--------------------- 
Winner: """ + candidatelist[1] )