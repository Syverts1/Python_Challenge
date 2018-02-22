import os
import csv

combined=[]
firstLast = []
empid = []
first=[]
last=[]
splitDate=[]
dob=[]
ssn=[]
state=[]

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
empOne = os.path.join("raw_data", "employee_data1.csv")
#open and read first csv file
with open(empOne, 'r', newline='') as openEmpOne:
    
    readEmpOne = csv.reader(openEmpOne, delimiter=',')
   
    #skip first line
    next(readEmpOne, None)    
    
    for row in readEmpOne:
        combined.append(row)

empTwo = os.path.join("raw_data", "employee_data2.csv")
#open and read second csv file
with open(empTwo, 'r', newline='') as openEmpTwo:
    
    readEmpTwo = csv.reader(openEmpTwo, delimiter=',')
   
    #skip first line
    next(readEmpTwo, None)    
    
    for row in readEmpTwo:
        combined.append(row)
        
for row in combined:
    #add employee id to empid list
    empid.append(row[0])
    
    #add first and last name to appropriate list
    firstLast = row[1].split(" ")
    first.append(firstLast[0])
    last.append(firstLast[1])
    
    #restructure date
    splitDate = row[2].split("-")
    splitDate[0], splitDate[1], splitDate[2] = splitDate[1], splitDate[2], splitDate[0]
    fixDate = "/".join(splitDate)
    dob.append(fixDate)
    
    #restructure ssn
    splitSSN = row[3].split("-")
    ssn.append("***-**-" + str(splitSSN[2]))
    
    #restructure state
    stateAbbr= us_state_abbrev[row[4]]
    state.append(stateAbbr)
#print(ssn)

# Zip lists together
parsed = zip(empid,first,last,dob,ssn,state)

# Set variable for output file
outputfile = os.path.join("parsed.csv")

#  Open the output file
with open(outputfile, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Emp ID","Fist Name","Last Name", "DOB","SSN","State"])

    # Write in zipped rows
    writer.writerows(parsed)