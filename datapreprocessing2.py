import csv

dataset1=[]
dataset2=[]

with open("bright_stars.csv", "r") as f:
    csvreader=csv.reader(f)
    for i in csvreader:
        dataset1.append(i)

with open ("converted_stars.csv", "r") as f:
    csvreader=csv.reader(f)
    for i in csvreader:
        dataset2.append(i)

temp_list1=dataset1[0]
temp_list2=dataset2[0]

temp_list = temp_list1 + temp_list2

columns1=dataset1[1:]
columns2=dataset2[1:]

columns=[]

for index, data_row in enumerate(columns1):
    columns.append(columns1[index]+columns2[index])

with open ("mergeddata2.csv", "a+") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(temp_list)
    csvwriter.writerows(columns)




