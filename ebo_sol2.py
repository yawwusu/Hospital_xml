# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 11:37:47 2018

@author: Yaw
"""

import xml.etree.ElementTree as ET
import csv
filename = 'vegetarian_types.xml'
tree = ET.parse(filename)
root = tree.getroot()

# open a file for writing
csv_data = open('xmlData.csv', 'w')

# create the csv writer object
csvwriter = csv.writer(csv_data)

# Create the header row
header = root.find('*/record')
data_head = [field.get('name') for field in header]
csvwriter.writerow(data_head)

# Fill in data at respective columns
for record in root.findall('*/record'):      
    data = [field.text for field in record]
    csvwriter.writerow(data)
    
csv_data.close()
print('Program has run successfully, check xmlData.csv in the folder to see the output')