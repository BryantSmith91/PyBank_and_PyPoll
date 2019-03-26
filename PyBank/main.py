import os
import csv

# importing counter module
from collections import Counter

def difference(a, b):
	return round(int(a) - int(b), 2)

#setting csv path
csvpath = os.path.join('budget_data.csv')


#initalizing lists and variables
clist = []
diflist = []
v1 = 0
v2 = 0
maxdif = 0
mindif = 0
total = 0

# opens CSV file, sets delimiter and skips header
with open(csvpath, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter =',')
	next(csvreader, None)

# here is where the magic happens! for each row in csvreader
	for row in csvreader:

		# v2 is set equal to the current active spot in the row
		v2 = row[1]

		# current spot is appended to a list (clist)
		clist.append(row[1])

		# row is added to running total
		total += int(row[1])

		# making a list for the difference of current cell and previous cell
		diflist.append(difference(v2,v1))

		# if difference of current cell and previous cell is greater than maxdif
		if difference(v2,v1) > int(maxdif):
			maxdif = difference(v2,v1)
			maxdifmo = str(row[0])
			v1 = row[1]

		# if the prior section doesnt run this checks to see if the difference is
		# less than the current minimum difference
		elif difference(v2,v1) < int(mindif):
			mindif = difference(v2,v1)
			mindifmo = str(row[0])
			v1 = row[1]

		# if neither prior section runs this runs
		else:
			v1 = row[1]

# deletes the first item in diflist as there is no difference at the start
del diflist[0]

# checks length of clist and sets totalmonths equal to it
totalmonths = len(clist)

# finds average difference by putting sum of differences over amount of differences
avgdif = round(float(sum(diflist)/len(diflist)),2)



# printing output to terminal
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
