import os
import shutil

from requests import delete

source_dir = 'source_directory'
destination_dir = 'destination_directory'

def list_files(directory):
    files = os.listdir(directory)
    print("Files in", directory, ":", files)

def copy_files(source, destination):
    files = os.listdir(source)
    for file in files:
        source_file = os.path.join(source, file)
        destination_file = os.path.join(destination, file)
        shutil.copyfile(source_file, destination_file)
    print("Files copied successfully from", source, "to", destination)

def move_files(source, destination):
    files = os.listdir(source)
    for file in files:
        source_file = os.path.join(source, file)
        destination_file = os.path.join(destination, file)
        shutil.move(source_file, destination_file)
    print("Files moved successfully from", source, "to", destination)

def delete_files(directory):
    files = os.listdir(directory)
    for file in files:
        file_path = os.path.join(directory, file)
        os.remove(file_path)
    print("Files deleted successfully from", directory)


if 
list_files(source_dir)
copy_files(source_dir, destination_dir)
move_files(source_dir, destination_dir)
delete
