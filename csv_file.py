import csv # in line in csv file is seperate data stream/set, the field are seperated using comma. 

''' read data from a txt file, interpret as csv format  using reader class'''
file = open("path")
csv_f = csv.reader(file)

for row in csv_f:
  # unpack the row if needed
 
''' write data to csv file writer class '''
data = [[x,x],[x,x]]
 with open("file_name", 'w' ) as file:
    writer = csv.writer(file)
    writer.writerows(data) # writerows method to write multiple rows, writerow help to write single row at a time
    
    




  
  
