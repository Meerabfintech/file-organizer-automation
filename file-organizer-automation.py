#!/usr/bin/env python3
import os
import shutil
import sys
FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.csv', '.pptx', '.md'],
    'Music': ['.mp3', '.wav', '.aac', '.flac', '.m4a'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.wmv'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Code': ['.py', '.cpp', '.c', '.java', '.js', '.html', '.css', '.json', '.xml'],
    'Applications': ['.exe', '.msi', '.dmg', '.app'],
    'Other': []
}
def organize_files(directory):
    """Organizes files in the specified directory into folders by type."""
    
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return False
  
    os.chdir(directory)
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
  
    if not files:
        print(f"no files found in '{directory}'. ")
        return False

    print(f"\n Found {len(files)} files to organize...")
    organized_count =0

    for file in files:
        # Get file extension
        _, ext = os.path.splitext(file)
        ext = ext.lower()
        # find which category this file belongs to
        folder_name = 'Other'
        for category, extensions in FILE_CATEGORIES.items():
            if ext in extensions:
                folder_name = category
                break
        # create folder if it does not exist
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f" Created folder: {folder_name}/")
        # Move file to folder
        try:
            shutil.move(file, os.path.join(folder_name, file))
            print(f"Moved: {file} --> {folder_name}/")
            organized_count += 1
        except Exception as e:
            print(f"Error moving {file}: {e}")
    print(f"\nOrganized {organized_count} out of {len(files)} files.")
    return True
def main():
    """Main function"""
    print("=" * 50)
    print("📂 FILE ORGANIZER - Automation Tool")
    print("=" * 50)
    
    # Get directory from user or use default
    print("\nEnter folder path to organize")
    print("(Press Enter for Downloads folder)")
    
    default_path = os.path.join(os.path.expanduser("~"), "Downloads")
    user_input = input("Path: ").strip()
    
    if user_input:
        target_dir = user_input
    else:
        target_dir = default_path
    
    print(f"\nTarget directory: {target_dir}")
    
    # Confirm before organizing
    confirm = input("\nProceed with organization? (y/n): ").lower().strip()
    
    if confirm == 'y' or confirm == 'yes':
        organize_files(target_dir)
    else:
        print("Operation cancelled.")
    
    input("\nPress Enter to exit...")     
if __name__ == "__main__":
    main()                


