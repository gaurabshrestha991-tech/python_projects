import os

search_name = input("Enter the file or folder name to search: ")

found = False

for root, folders, files in os.walk("/home"):
    for folder in folders:
        if search_name.lower() in folder.lower():
            print("Folder found: ", os.path.join(root, folder))
            found = True
            
    for file in files:
        if search_name.lower() in file.lower():
            print("File found: ", os.path.join(root, file))
            found = True
            
if not found:
    print("Nothing found.")