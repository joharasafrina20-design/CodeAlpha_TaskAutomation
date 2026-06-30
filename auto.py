import os
import shutil

# Source and destination folders
source_folder = "Photos"
destination_folder = "Moved_Images"

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Move all JPG files
for file in os.listdir(source_folder):
    if file.endswith(".jpg"):
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)
        shutil.move(source_path, destination_path)
        print(f"{file} moved successfully!")

print("\n✅ All JPG files have been moved.")