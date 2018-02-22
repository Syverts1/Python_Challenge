import os
import csv

combined = []
revenue = 0
prevRev = None
avgChange = 0
maxIncr = 0
maxIncrMonth = ""
maxDecr = 0
maxDecrMonth = ""
count = 0
#add csv paths
filename = str(input("Enter the file name: "))
csvFileName = str(filename) + ".csv"
file = os.path.join("raw_data", csvFileName)

#open and read first csv file
with open(file, 'r', newline='') as openFile:
    
    readFile = csv.reader(openFile, delimiter=',')
   
    #skip first line
    next(readFile, None)    
    
    for row in readFile:
        combined.append(row)

#count number of months

for row in combined:
    #total revenue calculation
    revenue = revenue + int(row[1])
    #calculate change in revenue
    if prevRev != None:
        change = int(row[1]) - prevRev
        row.append(change)
        if change > maxIncr:
            maxIncr = change
            maxIncrMonth = row[0]
        elif change < maxDecr:
            maxDecr = change
            maxDecrMonth = row[0]
        prevRev = int(row[1])
        #count number of rows (excluding) the first row
        count = count + 1
    else:
        row.append(0)
        prevRev = int(row[1])
    
    avgChange = avgChange + row[2]
    #print(row)


#print header
print("Financial Analysis")
print("--------------------")

#print calculations

print("Total Months: " + str(count + 1))
print("Total Revenue: $" + str(revenue))
print("Average Revenue Change: $" + str(round(float(avgChange/count),2)))
print("Greatest Increase in Revenue: " + maxIncrMonth + " ($" + str(maxIncr) + ")")
print("Greatest Decrease in Revenue: " + maxDecrMonth + " ($" + str(maxDecr) + ")")

#write results to text file
txtFileName = str(filename) + ".txt"
output = open(txtFileName, 'w+')

output.write("Financial Analysis\n")
output.write("--------------------\n")
output.write("Total Months: " + str(count + 1))
output.write("\nTotal Revenue: $" + str(revenue))
output.write("\nAverage Revenue Change: $" + str(round(float(avgChange/count),2)))
output.write("\nGreatest Increase in Revenue: " + maxIncrMonth + " ($" + str(maxIncr) + ")")
output.write("\nGreatest Decrease in Revenue: " + maxDecrMonth + " ($" + str(maxDecr) + ")\n")

output.close()