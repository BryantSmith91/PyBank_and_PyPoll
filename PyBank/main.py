import os
import csv

# importing counter module
from collections import Counter

def difference(a, b):
    return round(float(a) - float(b), 2)

#setting csv path
# csvpath = os.path.join('..','PyBank','budget_data.csv')
csvpath = "C:/Users/bryan/Desktop/BootCampStuff/Homework/HW_03_Python/PyBank/budget_data.csv"

#setting list for counter
clist = []
v1 = 0
v2 = 0
maxdif = 0
mindif = 0
total = 0
diflist = []
# opens CSV file, sets delimiter and appends results to a list
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    next(csvreader, None)
    for row in csvreader:
        v2 = row[1]
        clist.append(row[1])
        total = total + int(row[1])
        if float(v1) <= difference(v2, v1):
            maxdif = float(v2)
            maxdifmo = str(row[0])
            diflist.append(difference(v2,v1))
            v1 = row[1]
        elif float(v1) >= difference(v2,v1):
            mindif = float(v2)
            mindifmo = str(row[0])
            diflist.append(difference(v2,v1))
            v1 = row[1]
        else:
            v1 = row[1]


        # Broken here or the function is broken idk.

        ########## elif difference(int(row[1])) < mindif:
        ##########     mindif = difference(int(row[1]))
        ##########     mindifmo = row[0]
        ##########     diflist.append(difference(row[1]))
        ########## else:
        ##########     diflist.append(difference(row[1]))
print(maxdif,maxdifmo)

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
