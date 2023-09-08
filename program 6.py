#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os.path
import sys
fname = input("Enter the filename : ")
if not os.path.isfile(fname):
   print("File", fname, "doesn't exists")
   sys.exit(0)
infile = open(fname, "r")
lineList = infile.readlines()
for i in range(20):
    print(i+1, ":", lineList[i])
word = input("Enter a word : ")
cnt = 0
for line in lineList:
    cnt += line.count(word)
print("The word", word, "appears", cnt, "times in the file")


# In[7]:


import os
import zipfile
def create_zip_folder(folder_path, zip_filename):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return

    # Check if the zip file already exists
    if os.path.exists(zip_filename):
        print(f"Warning: File '{zip_filename}' already exists. Overwriting...")

    try:
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Walk through the folder and add its content to the ZIP file
            for foldername, subfolders, filenames in os.walk(folder_path):
                for filename in filenames:
                    file_path = os.path.join(foldername, filename)
                    # Add the file to the ZIP file with the relative path
                    zipf.write(file_path, os.path.relpath(file_path, folder_path))

        print(f"ZIP file '{zip_filename}' created successfully.")
    except Exception as e:
        print(f"Error: Failed to create ZIP file '{zip_filename}'.")
        print(f"Reason: {e}")
folder_path = "/content/Myzip"
zip_filename = "zipped.zip"
create_zip_folder(folder_path,zip_filename)


# In[ ]:




