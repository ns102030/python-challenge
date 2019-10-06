import os
import csv
import numpy as np
voterID=[]
county=[]
candidate=[]
correyVotes=0
khanVotes=0
liVotes=0
otooleyVotes=0
def unique(list1): 
    x = np.array(list1) 
    print(np.unique(x))

infile_path=os.path.join("/Users/nithinsunil/Desktop/Repositories/Homework/python-challenge/python-challenge/PyPoll/03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv")
with open(infile_path, 'r', newline="") as infile:
    reader = csv.reader(infile)
    for row in reader:
        if row[0]=="Voter ID":
            continue
        voterID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

    print("Election Results")
    print("--------------------------")
    print("Total Votes: " +str(len(candidate)))
    khanVotes=candidate.count("Khan")
    correyVotes= candidate.count("Correy")
    liVotes= candidate.count("Li")
    otooleyVotes= candidate.count("O'Tooley")
    print("Khan: "+str(round(khanVotes*100/len(candidate), 5))+"% " +"("+str(khanVotes)+")") 
    print("Correy: "+ str(round(correyVotes*100/len(candidate), 5))+"% " +"("+str(correyVotes)+")")
    print("Li: "+str(round(liVotes*100/len(candidate), 5))+"% " + "("+str(liVotes)+")")
    print("O'Tooley: "+str(round(otooleyVotes*100/len(candidate), 5))+"% " + "("+str(otooleyVotes)+")")
    print("--------------------------")
    print("Winner is "+ str(max(set(candidate), key=candidate.count)))

    outfile= os.path.join("ElectionResults.txt")
with open(outfile,"w",) as ElectionResults:
    writer= ElectionResults.write
    writer("Election Results\n")
    writer("--------------------------\n")
    writer("Total Votes: " +str(len(candidate))+"\n")
    writer("Khan: "+str(round(khanVotes*100/len(candidate), 5))+"% " +"("+str(khanVotes)+")"+"\n") 
    writer("Correy: "+ str(round(correyVotes*100/len(candidate), 5))+"% " +"("+str(correyVotes)+")"+"\n")
    writer("Li: "+str(round(liVotes*100/len(candidate), 5))+"% " + "("+str(liVotes)+")"+"\n")
    writer("O'Tooley: "+str(round(otooleyVotes*100/len(candidate), 5))+"% " + "("+str(otooleyVotes)+")"+"\n")
    writer("--------------------------\n")
    writer("Winner is "+ str(max(set(candidate), key=candidate.count))+"\n")