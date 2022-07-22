import csv

data=[]
with open("archive_dataset.csv",'r') as a:
    csvreader=csv.reader(a)
    for row in csvreader:
        data.append(row)
headers=data[0]
planetdata=data[1:]
#converting all planet name to lower case
for datapoint in planetdata:
    datapoint[2]=datapoint[2].lower()
#sorting names in alphabetical order
planetdata.sort(key=lambda planetdata:planetdata[2])
with open("archive_sorted.csv",'a+') as b:
    csvwriter=csv.writer(b)
    csvwriter.writerow(headers)
    csvwriter.writerows(planetdata)

#remove blank lines
with open("archive_sorted.csv") as input,open("archive_sorted1.csv",'w',newline='') as output:
    writer=csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip()for field in row):
            writer.writerow(row)



