import os
import shutil

folder = input("Enter the folder path: ")

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".webm"],
    "Audio": [".mp3", ".wav", ".flac", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Programs": [".exe", ".msi", ".deb", ".AppImage"],
    "Code": [".py", ".cpp", ".c", ".java", ".js", ".html", ".css"],
}

def organize_files():
    if not os.path.exists(folder):
        print("Folder does not exists!")
        return
    
    files = os.listdir(folder)
    
    for file in files:
        
        file_path = os.path.join(folder, file)
        
        if os.path.isdir(file_path):
            continue
        
        extension = os.path.splitext(file[1].lower())
        
        category = "Others"
        
        for folder_name, extensions in file_types.items():
            if extension in extensions:
                category = folder_name
                break
            
        category_path = os.path.join(folder, category)
        
        if not os.path.exists(category_path):
            os.makedirs(category_path)
            
        destination = os.path.join(category_path, file)
        
        if os.path.exists(destination):
            print(f"Skipped:  {file}")
        else:
            shutil.move(file_path, destination)
            print(f"Moved: {file} -> {category}")
            
organize_files()


print("\nFiles organized successfully!")
