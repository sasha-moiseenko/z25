import sys
import os
import json
import csv
import xml
import xml.etree.cElementTree as eTree

def read_json(filename):
    f = open(filename)
    f_json = json.load(f)
    f.close()
    return f_json


def read_csv(filename):
    f = open(filename)
    reader = csv.DictReader(f)
    f_csv = list(reader)
    return f_csv


def read_xml(filename):
    f = open(filename)
    tree = eTree.parse(f)
    root = tree.getroot()
    f_xml = []
    for i in root:
        f_xml.append({child.tag: child.text for child in i.getchildren()})
    return f_xml

def read_file_data(filename):
    name, ext = os.path.splitext(filename)
    if ext == '.json':
        return read_json(filename)
    elif ext == '.csv':
        return read_csv(filename)
    elif ext == '.xml':
        return read_xml(filename)


def write_csv(filename, data):
    f = open(filename, 'w')
    writer = csv.DictWriter(f, data[0].keys())
    writer.writeheader()
    writer.writerows(data)
    f.close()
    return f


def write_json(filename, data):
    f = open(filename, 'w')
    f.write(json.dumps(data, indent=4))
    f.close()
    return f

def write_xml(filename, data):
    # f = open(filename, 'w')
    # result = []
    # for child in data:
    pass

def write_file_data(filename, data):
    name, ext = os.path.splitext(filename)
    if ext == '.csv':
        write_csv(filename, data)
    elif ext == '.json':
        write_json(filename, data)
    elif ext == '.xml':
        write_xml(filename, data)


def converter(in_file, out_file):
    data = read_file_data(in_file)
    write_file_data(out_file, data)


converter(sys.argv[1], sys.argv[2])
