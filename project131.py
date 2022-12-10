import pandas as pd
import csv

df=pd.read_csv("cleaned_data.csv")







rows = []

with open("cleaned_data.csv",'r') as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        rows.append(row)

headers = rows[0]
star_data_rows = rows[1:]
print(headers)
print(star_data_rows[0])

headers[0] = "row_num"



temp_star_data_rows = list(star_data_rows)
for star_data in temp_star_data_rows:
    star_mass = star_data[3]
    if star_mass.lower() == "unknown":
        star_data_rows.remove(star_data)
        continue
    else:
        star_mass = float(star_mass) * 1.989e+30
        star_data[3] = star_mass


    star_radius = star_data[4]
    if star_radius.lower() == "unknown":
        star_data_rows.remove(star_data)
        continue
    else:
        star_radius = float(star_radius) * 6.957e+8
        star_data[4] = star_radius


        temp_star_data_rows = list(star_data_rows)
        for star_data in temp_star_data_rows:
            if star_data[5].lower() == "Star_name":
                star_data_rows.remove(star_data)


star_masses = []
star_radiuses = []
star_names = []
for star_data in enumerate in star_data_rows:
    star_masses.append(star_data[3])
    star_radiuses.append(star_data[4])
    star_names.append(star_data[5])

star_gravity = []
for index,name in enumerate(star_names):
    gravity = (float(star_masses[index])*5.972e+24) / (float(star_radiuses[index]) * float(star_radiuses[index])*6371000*6371000) * 6.674e-11
    star_gravity.append(gravity)



star_masses = []
star_radiuses = []



with open("Mass", "r") as f:
    csvreader=csv.reader(f)
    for i in csvreader:
        star_masses.append(i)

with open ("Radius", "r") as f:
    csvreader=csv.reader(f)
    for i in csvreader:
        star_radiuses.append(i)

temp_list1=star_masses[3]
temp_list2=star_radiuses[4]

temp_list = temp_list1 + temp_list2

columns1=star_masses[3]
columns2=star_radiuses[4]

star_gravity=[]

for index, data_row in enumerate(columns1):
    star_gravity.append(columns1[index]+columns2[index])

with open ("star_gravity", "a+") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(temp_list)
    csvwriter.writerows(star_gravity)




