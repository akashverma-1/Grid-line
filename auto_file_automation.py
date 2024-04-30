# Write scripts to organize, move, rename, or delete files and directories automatically.

import os
import shutil
import zipfile
import re

# a function that take a path containing files, and rename each file with a suffix and a number starting from 1 to n and stores them in a zip file and sttore in the destination folder
def rename_files_and_store_in_zip(source_folder, destination_folder, suffix, filetype):
    result = {}
    os.makedirs(destination_folder, exist_ok=True)
    try:
        files = os.listdir(source_folder)
        if len(files) == 0:
            result['status'] = 'error'
            result['message'] = 'No files found in the source folder'
            return result
        i = 1
        with zipfile.ZipFile(destination_folder + '/files.zip', 'w') as zipf:
            for file in files:
                if file.endswith(filetype):
                    new_name = f'{suffix}_{i}{filetype}'
                    os.rename(source_folder + '/' + file, source_folder + '/' + new_name)
                    zipf.write(source_folder + '/' + new_name, new_name)
                    i += 1
        result['status'] = 'success'
        result['message'] = 'Files renamed and stored in zip file'
        result['path'] = destination_folder + '/files.zip'

    except Exception as e:
        result['status'] = 'error'
        result['message'] = str(e)
    return result
    
def segregate_files_by_extension(source_folder, group_dict = None):
    if group_dict is None:
        group_dict = {
            'images': ['jpg', 'jpeg', 'png', 'gif'],
            'videos': ['mp4', 'mkv', 'avi', 'mov'],
            'documents': ['doc', 'docx', 'pdf', 'txt'],
            'spreadsheets': ['xls', 'xlsx', 'csv'],
            'presentations': ['ppt', 'pptx'],
            'codes': ['py', 'java', 'js', 'html', 'css'],
            'compressed': ['zip', 'rar', 'tar', 'gz'],
            'executables': ['exe', 'msi'],
            'others': []
        }
    # a function that takes a path containing files and segregates them by extension
    # makes a backup folder in the destination folder and moves the files to the respective extension folder
    # then create folders in the source folder and move the files to the respective group
    # finally, return true or false
    result = {}
    try:
        os.makedirs(source_folder + '/backup', exist_ok=True)
        files = os.listdir(source_folder)
        if len(files) == 0:
            result['status'] = 'error'
            result['message'] = 'No files found in the source folder'
            return result
        for file in files:
            if os.path.isfile(source_folder + '/' + file):
                extension = file.split('.')[-1]
                for group in group_dict.keys():
                    if extension in group_dict[group]:
                        if not os.path.exists(source_folder + '/' + group):
                            os.makedirs(source_folder + '/' + group)
                        shutil.move(source_folder + '/' + file, source_folder + '/' + group + '/' + file)
                        shutil.copy(source_folder + '/' + group + '/' + file, source_folder + '/backup/' + file)
        # remove backup folder
        shutil.rmtree(source_folder + '/backup')
        # zip the src folder
        shutil.make_archive(source_folder, 'zip', source_folder)
        result['path'] = source_folder + '.zip'
        result['status'] = 'success'
        result['message'] = 'Files segregated by extension'
    except Exception as e:
        result['status'] = 'error'
        result['message'] = str(e)
    return result

