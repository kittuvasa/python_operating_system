import csv # in line in csv file is seperate data stream/set, the field are seperated using comma. 

file = open("path")
csv_f = csv.reader(file)

for row in csv_f:
  # unpack the row if needed
  
  
