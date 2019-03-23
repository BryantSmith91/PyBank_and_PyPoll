import os
import csv

csvpath = os.path.join('..','PyPoll','election_data.csv')
with open(csvpath, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter =',')


        print(len(csvreader))
