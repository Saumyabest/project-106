import csv
with open('heightweight.csv') as f:
  reader = csv.reader(f)
  heightweight_data = list(reader)
heightweight_data.pop(0)
height=[]
for i in heightweight_data:
    height.append(heightweight_data[i][1])
print(height)

