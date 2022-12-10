import csv

dataset1=[]
dataset2=[]


with open ("final.csv", "r") as f:
    csvreader=csv.reader(f)
    for i in csvreader:
        dataset1.append(i)

with open ("sorted.csv","r") as f:
    csvreader=csv.reader(f)
    for i in csvreader:
        dataset2.append(i)

headers1=dataset1[0]
headers2=dataset2[0]

headers=headers1 + headers2

planet_data1=dataset1[1:]
planet_data2=dataset2[1:]

planet_data=[]

for index, data_row in enumerate(planet_data1):
     planet_data.append(planet_data1[index] + planet_data2[index])

with open ("mergeddata.csv","a+") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)