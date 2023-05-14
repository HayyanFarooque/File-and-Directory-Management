import os

def rename_files(directory, prefix):
    for filename in os.listdir(directory):
        os.rename(os.path.join(directory, filename), os.path.join(directory, prefix + filename))

if __name__ == "__main__":
    directory = "./"
    prefix = "new_"
    rename_files(directory, prefix)
