import os
import shutil

def list_files(directory):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            print(filename)

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory {directory} created.")
    else:
        print(f"Directory {directory} already exists.")

def move_files(source_directory, target_directory, file_extension):
    for filename in os.listdir(source_directory):
        if filename.endswith(file_extension):
            shutil.move(os.path.join(source_directory, filename), target_directory)
            print(f"Moved {filename} to {target_directory}")

def main():
    source_directory = "./"
    target_directory = "./txt_files"
    file_extension = ".txt"

    print("Files in directory:")
    list_files(source_directory)

    print("\nCreating new directory...")
    create_directory(target_directory)

    print("\nMoving .txt files...")
    move_files(source_directory, target_directory, file_extension)

    print("\nFiles in new directory:")
    list_files(target_directory)

if __name__ == "__main__":
    main()
