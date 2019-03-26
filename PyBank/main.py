import os
import csv

# importing counter module
from collections import Counter

def difference(a, b):
    return round(int(a) - int(b), 2)

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
        total += int(row[1])
        diflist.append(difference(v2,v1))
        if difference(v2,v1) > float(maxdif):
            maxdif = difference(v2,v1)
            maxdifmo = str(row[0])
            # diflist.append(difference(v2,v1))
            v1 = row[1]
        elif difference(v2,v1) < float(mindif):
            mindif = difference(v2,v1)
            mindifmo = str(row[0])
            # diflist.append(difference(v2,v1))
            v1 = row[1]
        else:
            v1 = row[1]

del diflist[0]
totalmonths = len(clist)
totaldif = sum(diflist)
avgdif = round(float(totaldif/(totalmonths-1)),2)
# print(totalmonths,totaldif,avgdif)



print("Financial Analysis")
print("-"*28)
print("Total Months: "+str(totalmonths))
print("Total: $"+str(total))
print("Average Change: $"+str(avgdif))
print("Greatest Increase in Profits: "+str(maxdifmo)+" ($"+str(maxdif)+")")
print("Greatest Decrease in Profits: "+str(mindifmo)+" ($"+str(mindif)+")")

#prints end to textfile
with open("pybank.txt", "w") as outfile:
    print("Financial Analysis", file=outfile)
    print("-"*28, file=outfile)
    print("Total Months: "+str(totalmonths), file=outfile)
    print("Total: $"+str(total), file=outfile)
    print("Average Change: $"+str(avgdif), file=outfile)
    print("Greatest Increase in Profits: "+str(maxdifmo)+" ($"+str(maxdif)+")", file=outfile)
    print("Greatest Decrease in Profits: "+str(mindifmo)+" ($"+str(mindif)+")", file=outfile)
outfile.close()
