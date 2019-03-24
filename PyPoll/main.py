import os
import csv

# Correy
# Khan
# Li
# O'tooley
ccount = 0
kcount = 0
lcount = 0
ocount = 0

clist = []

# csvpath = os.path.join('..','PyPoll','election_data.csv')
csvpath = 'C:/Users/bryan/Desktop/BootCampStuff/Homework/HW_03_Python/PyPoll/election_data.csv'

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    header = next(csvreader)
    for row in csvreader:
        clist.append(row[2])
ccount = 0
kcount = 0
lcount = 0
ocount = 0

for i in range(len(clist)):

    if clist[i] == "Khan":
        kcount = kcount + 1
    elif clist[i] == "Correy":
        ccount = ccount + 1
    elif clist[i] == "Li":
        lcount = lcount + 1
    elif clist[i] == "O'Tooley":
        ocount = ocount + 1

print (kcount, ccount, lcount, ocount)
        # print(str(kcount))
        # for row in csvreader:
        #     if  is 'Khan':
        #         kcount = kcount + 1
