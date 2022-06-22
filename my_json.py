import json
import csv
# Another simple example of reading JSON data and writing to csv file
with open("./sample1.json") as file:
    data=json.load(file)

fname="output1.csv"

with open(fname,"w") as file:
    csv_file=csv.writer(file)
    csv_file.writerow(["Name", " Age", "Created"])
    
    for item in data:
        csv_file.writerow([item['name'],item['age'],item['created_at']])