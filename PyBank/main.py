import os
import csv

# importing counter module
from collections import Counter

def difference(a):
    return round((a + 1) - a, 2)

#setting csv path
# csvpath = os.path.join('..','PyBank','budget_data.csv')
csvpath = "C:/Users/bryan/Desktop/BootCampStuff/Homework/HW_03_Python/PyBank/budget_data.csv"

#setting list for counter
clist = []
maxdif = 0
mindif = 0
total = 0
# opens CSV file, sets delimiter and appends results to a list
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    next(csvreader, None)
    for row in csvreader:
        clist.append(row[1])
        total = total + int(row[1])


        # Broken here or the function is broken idk.

        ########## if difference(int(row[1])) > maxdif:
        ##########     maxdif = difference(int(row[1]))
        ##########     maxdifmo = row[0]
        ##########     diflist.append(difference(row[1]))
        ########## elif difference(int(row[1])) < mindif:
        ##########     mindif = difference(int(row[1]))
        ##########     mindifmo = row[0]
        ##########     diflist.append(difference(row[1]))
        ########## else:
        ##########     diflist.append(difference(row[1]))


totalmoney = Counter(clist)
totalmonths = len(clist)

print("Financial Analysis")
print("-"*28)
print("Total Months: "+str(totalmonths))
print("Total: $"+str(total))
# print("Average Change: $"+str())
# print("Greatest Increase in Profits: "+str()+" ($"+str()+")")
# print("Greatest Decrease in Profits: "+str()+" ($"+str()+")")

# #prints end to textfile
# with open("pybank.txt", "w") as outfile:
#     print("Financial Analysis", file=outfile)
#     print("-"*28, file=outfile)
#     print("Total Months: "+str(totalmonths), file=outfile)
#     print("Total: $"+str(total), file=outfile)
#     print("Average Change: $"+str(##############), file=outfile)
#     print("Greatest Increase in Profits: "+str(########)+" ($"+str(########)+")", file=outfile)
#     print("Greatest Decrease in Profits: "+str(#######)+" ($"+str(########)+")", file=outfile)
# outfile.close()
