import os
import csv

# importing counter module
from collections import Counter

# defines percentage equation
def percentage(a,b):
    return round(a/b*100,2)

# #List of names for my purposes.
# Correy
# Khan
# Li
# O'Tooley

#setting list for counter
clist = []

#setting csv path
csvpath = os.path.join('..','PyPoll','election_data.csv')

# opens CSV file, sets delimiter and appends results to a list
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    header = next(csvreader)
    for row in csvreader:
        clist.append(row[2])

#counts the list and sets results to polldic
polldic = Counter(clist)

#finds length of the list for total amount of votes
totalvotes =  (len(clist))

#pulls values from the dictionaries, how many votes each cantidate got
kcount = polldic["Khan"]
ccount = polldic["Correy"]
lcount = polldic["Li"]
ocount = polldic["O'Tooley"]

# applies cantidate votes and total votes to the percentage function
    # to find overall percentage
kpercent = percentage(kcount,totalvotes)
cpercent = percentage(ccount,totalvotes)
lpercent = percentage(lcount,totalvotes)
opercent = percentage(ocount,totalvotes)

#finds the largest value in the polldic to find election winner
winner = max(polldic, key=lambda key: polldic[key])

#prints results in terminal
print("Election Results")
print("-"*26)
print(f'Total Votes: {totalvotes}')
print("-"*26)
print(f'Kahn: {kpercent}00% ({kcount})')
print(f'Correy: {cpercent}00% ({ccount})')
print(f'Li: {lpercent}00% ({lcount})')
print(f"O'Tooley: {opercent}00% ({ocount})")
print("-"*26)
print(f'Winner = {winner}')
print("-"*26)


#prints results to textfile
with open("pypoll.txt", "w") as outfile:
    print("Election Results", file=outfile)
    print("-"*26, file=outfile)
    print("Total Votes: "+str(totalvotes), file=outfile)
    print("-"*26, file=outfile)
    print("Khan: "+str(kpercent)+"00% ("+str(kcount)+")", file=outfile)
    print("Correy: "+str(cpercent)+"00% ("+str(ccount)+")", file=outfile)
    print("O'Tooley: "+str(opercent)+"00% ("+str(ocount)+")", file=outfile)
    print("Li: "+str(lpercent)+"00% ("+str(lcount)+")", file=outfile)
    print("-"*26, file=outfile)
    print("Winner = "+str(winner), file=outfile)
    print("-"*26, file=outfile)
outfile.close()
