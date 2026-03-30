import os
import shutil

# First we will Get the folder path
folder_path = input("Enter the path of the folder you want to sort: ")

# We will check if the folder path exists or not. If does not exist then exit the program.
if not os.path.exists(folder_path):
    print("Folder does not exist. Please check the path!")
    exit()

# display all the files in that folder.
files = os.listdir(folder_path)
print("Files found:", files)

# we will sort the files by their extensions.
for file in files:
    full_path = os.path.join(folder_path, file)

    # Get extension
    _, ext = os.path.splitext(file)
    ext = ext[1:]  # remove the dot from the extension.

    # Create folder for extension
    ext_folder = os.path.join(folder_path, ext)
    if not os.path.exists(ext_folder): # if there is no folder for that extension then create a new folder.
        os.mkdir(ext_folder)

    # Move file
    shutil.move(full_path, os.path.join(ext_folder, file))

print("Sorting complete!")