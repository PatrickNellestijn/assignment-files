__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os
import shutil 
import zipfile
import pathlib

folder = os.getcwd()
folder_cache = folder + "/cache"
zip_file = folder + "/data.zip"


#function 1
#takes no arguments and creates an empty folder named cache in the current directory. 
# If it already exists, it deletes everything in the cache folder.
def clean_cache():
    folder_check = os.listdir(folder)
    if 'cache' in folder_check:
        shutil.rmtree(folder_cache) 
    #code-create folder
    os.mkdir(folder_cache)
    return

#function 2 zip
# takes a zip file path (str) and a cache dir path (str) as arguments, 
# in that order. The function then unpacks the indicated zip file into a clean cache folder.
#You can test this with data.zip file.
def cache_zip(zip_file, folder_cache):
    with zipfile.ZipFile(zip_file, 'r',) as zip_ref:
        zip_ref.extractall(folder_cache)
    return 


#function 3 files
#takes no arguments and returns a list of all the files in the cache. The file paths should be specified in absolute terms. Search the web for what this means! No folders should be included in the list. 
#You do not have to account for files within folders within the cache directory.
def cached_files():
    list_files = []
    with os.scandir(folder_cache) as list_of_entries:
        for entry in list_of_entries:
            if entry.is_file():
                result = os.path.abspath(entry)
                list_files.append(result)
                
    return list_files

#function 4 password
#takes the list of file paths from cached_files as an argument. This function should read the text in each one to see if the password is in there. Surely there should be a word in there to incidicate
#the presence of the password? Once found, find_password should return this password string.
def find_password(list_files):
    for file_name in list_files:
        file = open(file_name, 'r')
        for line in file:
            if 'password' in line:
                return line[line.find(' ')+1:].rstrip()