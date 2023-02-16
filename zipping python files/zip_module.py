import zipfile
import os
import shutil

#How to compress files in python
#create the files to compress
f = open('file1.txt', 'w+')
f.write('this is a line in file1 ')
f.close()

f = open('file2.txt', 'w+')
f.write('this is a line in file2 ')
f.close()

#create zip file
comp_file = zipfile.ZipFile('comp_file.zip','w')

#add previously created files to the zip file
comp_file.write('file1.txt', compress_type =zipfile.ZIP_DEFLATED)

comp_file.write('file2.txt', compress_type=zipfile.ZIP_DEFLATED)

#close file
comp_file.close()

#extract the files from the folder
zip_object = zipfile.ZipFile('comp_file.zip', 'r')

zip_object.extractall('extracted_zip_file')

#compress whole folders and file in python
#using shutil module

output_file = 'example'
dir_to_zip = os.getcwd() + '\python_files'
shutil.make_archive(output_file, 'zip', dir_to_zip)

shutil.unpack_archive('example.zip', 'final_unzip', 'zip')

