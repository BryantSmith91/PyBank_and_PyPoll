import os
import csv

# importing counter module
from collections import Counter

#setting csv path
# csvpath = os.path.join('..','PyBank','budget_data.csv')
csvpath = "C:/Users/bryan/Desktop/BootCampStuff/Homework/HW_03_Python/PyBank/budget_data.csv"

#setting list for counter
clist = []
clist2 = []
total = 0
# opens CSV file, sets delimiter and appends results to a list
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    next(csvreader, None)
    for i in csvreader:
        total = total + i[1]
    for row in csvreader:
        clist.append(row[1])


totalmoney = Counter(clist)
# maximum = max(totalmoney, key=lambda key: totalmoney[key])
# minimum = min(totalmoney, key=lambda key: totalmoney[key])
print(maximum, minimum)
# for i in totalmoney:
#     clist2.append(int(i))
#
# total = sum(totalmoney.elements())

totalmonths = len(clist)

print(f'{total},{totalmonths}')



# #prints end to textfile
# with open("pybank.txt", "w") as outfile:
#     print("Financial Analysis", file=outfile)
#     print("-"*28, file=outfile)
#     print("Total Months: "+str(), file=outfile)
#     print("Total: $"+str(), file=outfile)
#     print("Average Change: $"+str(), file=outfile)
#     print("Greatest Increase in Profits: "+str()+" ($"+str()+")", file=outfile)
#     print("Greatest Decrease in Profits: "+str()+" ($"+str()+")", file=outfile)
# outfile.close()
