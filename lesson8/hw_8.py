import json

file = open('/Downloads/service_param_values_202002171548.json')

f = json.load(file)
file = open('/Downloads/service_param_values_202002171548.json', 'w')
file.write(json.dumps(f, indent=4))
file.close()

print(f)



def for_csv(path, filename=None):
    f = open(path)


# headers = f.readline()[:-1].split(',')
# print(headers)
filename = list(csv.DictReader(f))
# headers = f.readline()[:-1].split(',')
f.close()
f = open(path, 'w')
# print(filename)
# headers = filename[0].keys()
writer = csv.DictWriter(f, filename[0].keys())
writer.writeheader()
writer.writerows(filename)
f.close()
return filename

print(for_csv('/home/sasha/Downloads/service_param_values_202002171436.csv'))
#
# file = open('/home/sasha/Downloads/service_param_values_202002171436.csv')
# headers = file.readline()[:-1].split(',')
# # print(headers)
# lines = file.read().split('\n')
# # print(lines)
# file.close()
# lines = [
# dict(zip(headers, line.split(',')))
# for line in lines if line
# ]
# print(headers)
# print(lines)

import os
import csv
import sys

def check_extensions(path, filename=None):
extensions = {'json': "it's json file", 'csv': "it's csv file", 'xml': "it's xml file", 'bin': "it's pickle"}
for key in extensions:
if filename.endswith(f'.{key}'):
print(extensions[key])
#
#
# check_extensions('/home/sasha', )

with open('/home/sasha/Downloads/7.csv', 'r') as file:
# file = open('/home/sasha/Downloads/7.csv')
# reader = csv.reader(file)
# print(list(reader))
# file.close()
f_obj = csv.DictReader(file, delimiter=',')
for line in f_obj:
    print(line['Served MSISDN'])
# print(line["Record Type"])