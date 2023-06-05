import os
import shutil

def backup_files(source_dir, destination_dir):
    # Check if the source directory exists
    if not os.path.exists(source_dir):
        print("Source directory does not exist.")
        return

    # Check if the destination directory exists, if not, create it
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Get a list of files in the source directory
    files = os.listdir(source_dir)

    # Backup each file in the source directory
    for file_name in files:
        source_file = os.path.join(source_dir, file_name)
        destination_file = os.path.join(destination_dir, file_name)

        # Check if the file is a regular file (not a directory)
        if os.path.isfile(source_file):
            shutil.copy2(source_file, destination_file)
            print(f"File '{file_name}' backed up successfully.")

    print("Backup complete.")

def main():
    print("Welcome to the file backup application!")

    source_dir = input("Enter the source directory: ")
    destination_dir = input("Enter the destination directory: ")

    backup_files(source_dir, destination_dir)

if __name__ == "__main__":
    main()
