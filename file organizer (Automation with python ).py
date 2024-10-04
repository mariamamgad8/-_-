import os
import shutil

path = input("Enter path: ")
files = os.listdir(path)

for file in files:
    # Skip directories
    if os.path.isdir(os.path.join(path, file)):
        continue

    filename, extension = os.path.splitext(file)
    extension = extension[1:]  # Remove the dot from extension

    # Handle files without extensions
    if extension == "":
        extension = "no_extension"

    # Construct the target directory path
    target_dir = os.path.join(path, extension)

    # If the directory exists, move the file
    if os.path.exists(target_dir):
        shutil.move(os.path.join(path, file), os.path.join(target_dir, file))
    else:
        # Create the directory and move the file
        os.makedirs(target_dir)
        shutil.move(os.path.join(path, file), os.path.join(target_dir, file))

print("Files organized successfully.")
