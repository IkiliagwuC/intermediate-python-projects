import csv

#check working directory
import os
os.getcwd()


#open the file
data = open('example.csv', encoding = 'utf-8')
#add encoding to prevent error for special characters
#open the csv reader on it
csv_data = csv.reader(data)
#reformat it into a python object list of lists
data_lines = list(csv_data)


for line in data_lines[:6]:
    print(line)



#grab a list of all emails from the list
email_list = []
for line in data_lines[1:]:
    email_list.append(line[3])


#grab a list of the fullnames in the csv file
full_names = []

for line in data_lines[1:]:
    full_names.append(line[1] + ' ' + line[2])

file_to_output = open('to_save_file.csv', mode = 'w', newline = '')

csv_writer = csv.writer(file_to_output, delimiter = ',')

file_to_output.close()