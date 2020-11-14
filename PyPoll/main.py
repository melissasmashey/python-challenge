import os
import csv

#Bring in CSV File and Read in
election_data_csv = os.path.join("./Resources/election_data.csv")

# Open and read csv
with open(election_data_csv, newline="") as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=",")
    csv_header= next(csv_file)
 #Variables
    candidate = []
    candidate_names=[]
    candidate_votes=[]
    y=1
 #For loop to collect candidate vote counts and candidate name
    for row in csv_reader:
     candidate.append(row[2])
    candidate_count = [[y,candidate.count(y)] for y in set(candidate)]
    
#For loop within candidate_count to get winner
    for row in candidate_count:
        candidate_names.append(row[0])
        candidate_votes.append(row[1])
        x=candidate_votes.index(max(candidate_votes))
        Candidate_winner=(candidate_names[x])
    
total=len(candidate)
#####labeling candidate votes and percentages######
khan=candidate.count("Khan")
correy=candidate.count("Correy")
li=candidate.count("Li")
otooley=candidate.count("O'Tooley")
khan_perc='{:,.3%}'.format(khan/total)
correy_perc='{:,.3%}'.format(correy/total)
li_perc='{:,.3%}'.format(li/total)
otooley_per='{:,.3%}'.format(otooley/total)
###### PRINT TO TERMINAL ######
print ("Election Results")
print ("------------------------")
print ("Total Votes:",(total))
print ("------------------------")
print ("Khan:",(khan_perc),"(",(khan),")")
print ("Correy:",(correy_perc),"(",(correy),")")
print ("Li:",(li_perc),"(",(li),")")
print ("O'Tooley:",(otooley_per),"(",(otooley),")")
print ("------------------------")
print ("Winner:", (Candidate_winner))
print ("-----------------------")


# PRINT TO TEXT FILE #
text_file = os.path.join("./analysis/PyPoll.txt") 
with open(text_file, "w") as f:

    print ("Election Results",file=f)
    print ("------------------------")
    print ("Total Votes:",(total), file=f)
    print ("------------------------", file=f)
    print ("Khan:",(khan_perc),"(",(khan),")", file=f)
    print ("Correy:",(correy_perc),"(",(correy),")", file=f)
    print ("Li:",(li_perc),"(",(li),")", file=f)
    print ("O'Tooley:",(otooley_per),"(",(otooley),")", file=f)
    print ("------------------------", file=f)
    print ("Winner:", (Candidate_winner), file=f)
    print ("------------------------", file=f)
