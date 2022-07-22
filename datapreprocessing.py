import csv

dataset1=[]
dataset2=[]

with open("final.csv",'r') as a:
    reader=csv.reader(a)
    for row in reader:
        dataset1.append(row)
with open("archive_sorted1.csv",'r') as b:
    reader=csv.reader(b)
    for row in reader:
        dataset2.append(row)
headers1=dataset1[0]
planetdata1=dataset1[1:]

headers2=dataset2[0]
planetdata2=dataset2[1:]

headers=headers1+headers2
planetdata=[]
for index,datarow in enumerate(planetdata1):
    planetdata.append(planetdata1[index]+planetdata2[index])
with open("mergedata.csv",'w',newline='') as c:
    csvwriter=csv.writer(c)
    csvwriter.writerow(headers)
    for row in planetdata:
        csvwriter.writerow(row)
    
