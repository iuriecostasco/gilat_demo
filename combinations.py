#Script will write in CSV file all possible combinations of defined values
import csv

#Define CSV Header
header=['value1','value2','value3']

#indicate all values that you want to combine
a=[['1','2','3'],['blue', 'green', 'red'],['light','black']]

r=[[]]
for x in a:
    t = []
    for y in x:
        for i in r:
            t.append(i+[y])
    r = t

with open('Combinations.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for row in r:
        writer.writerow(row)
