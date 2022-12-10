import csv
data=[]

with open ("archive_dataset.csv", "r") as f:
    csvreader=csv.reader(f)
    for i in csvreader:
        data.append(i)

headers=data[0]
planets_data=data[1:]

for i in planets_data:
    i[2]=i[2].lower()

planets_data.sort(key=lambda planets_data:planets_data[2])
with open ("sortedarchive.csv", "a+") as f:
    csvwriter=csv.writer(f) 
    csvwriter.writerow(headers)
    csvwriter.writerows(planets_data)

with open('sortedarchive.csv') as input, open('sorted.csv', 'w', newline='') as output:
     writer = csv.writer(output) 
     for row in csv.reader(input):
         if any(field.strip() for field in row):
             writer.writerow(row)

