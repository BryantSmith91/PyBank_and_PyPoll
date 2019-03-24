import os
import csv
from collections import Counter
# Correy
# Khan
# Li
# O'Tooley
ccount = 0
kcount = 0
lcount = 0
ocount = 0
def percentage(a,b):
    return round(a/b*100,2)

clist = []

# csvpath = os.path.join('..','PyPoll','election_data.csv')
csvpath = 'C:/Users/bryan/Desktop/BootCampStuff/Homework/HW_03_Python/PyPoll/election_data.csv'

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    header = next(csvreader)
    for row in csvreader:
        clist.append(row[2])
polldic = Counter(clist)
totalvotes =  (len(clist))

kcount = polldic["Khan"]
ccount = polldic["Correy"]
lcount = polldic["Li"]
ocount = polldic["O'Tooley"]
kpercent = percentage(kcount,totalvotes)
cpercent = percentage(ccount,totalvotes)
lpercent = percentage(lcount,totalvotes)
opercent = percentage(ocount,totalvotes)
winner = max(polldic, key=lambda key: polldic[key])
print(f"{totalvotes},{kcount},{ccount},{lcount},{ocount}")
print(f"{kpercent}%,{cpercent}%,{lpercent},{opercent}%, {winner}")
print("-"*26)
        # print(str(kcount))
        # for row in csvreader:
        #     if  is 'Khan':
        #         kcount = kcount + 1
