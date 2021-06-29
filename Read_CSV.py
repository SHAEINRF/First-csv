import csv
input=csv.DictReader(open('Sample.csv')) #csv.DictReader is a class under the csv module
for row in input: #loop iterates for all the values in the csv
    num=(row['Number']) #Number is the key for the dictionary
    print("Number: "+num)