import csv
import json
with open('a.csv', 'r') as csvfile:
    data = list(csv.reader(csvfile, delimiter=","))
    hdr = [str(i).lower() for i in data[0]]
    crs_data = []
    for i in range(1, len(data)):
        if (i != 4):
            crs_data.append(data[i])
        else:
            crs_data.append(data[i])
            m = list(data[i])
            crs_data.append(m[0])
    datajson = json.dumps(crs_data)
fd = open('data.json', 'w')
fd.write(datajson)
fd.close()
