import os
import csv

# Specify the file to write to
months=0
netprofits=0
row=2
averagechange=0
values= []
changes = []
valuechange=0
averagechange=0
highprof=0
highloss=0
dates=[]
highmonth=""
lowmonth=""

infile_path=os.path.join("/Users/nithinsunil/Desktop/Repositories/Homework/python-challenge/python-challenge/PyBank/03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv")
with open(infile_path, 'r', newline="") as infile:
    reader = csv.reader(infile)
    for row in reader:
        months=months+1
        if str(row[1]) == "Profit/Losses":
            continue
       
        netprofits = netprofits + int(row[1])
        values.append(int(row[1]))
       

        dates.append(row[0])
        
    for j in range(len(values)):
        if j==0:
            continue
        
        chng = values[j]-values[j-1]
        changes.append(chng)
    for r in range(len(changes)):
        if changes[r]== max(changes):
            highmonth=dates[r+1]
        if changes[r]== min(changes):
            lowmonth=dates[r+1]
      
print("Financial Analysis")
print("-------------------------")
months=months-1
print("Total Months:",months)
print("Total: $"+str(netprofits))
averagechange= round(sum(changes)/ len(changes), 2)
print("Average Change: $"+str(averagechange))
highprof= max(changes)
highloss= min(changes)
print("Greatest Increase in Profits:"+highmonth+" $"+str(highprof))
print("Greatest Decrease in Profits:"+lowmonth+" $"+str(highloss))

outfile= os.path.join("FinancialReport.txt")
with open(outfile,"w",) as FinancialReport:
    writer= FinancialReport.write
    writer("Financial Analysis\n")
    writer("-------------------------\n")
    writer("Total Months: "+ str(months)+"\n")
    writer("Total: $"+str(netprofits)+"\n")
    writer("Average Change: $"+str(averagechange)+"\n")
    writer("Greatest Increase in Profits:"+highmonth+" $"+str(highprof)+"\n")
    writer("Greatest Decrease in Profits:"+lowmonth+" $"+str(highloss)+"\n")
