import os
import shutil
from sklearn.model_selection import train_test_split

# Specify the directory containing the .wav files
source_dir = '/home/raikar/primock57/output/mixed_audio'

# Specify the base directory where you want to create the folders
base_dir = '/home/raikar/primock57/AMI-diarization-setup/pyannote/medical_dataset'

# Get a list of all .wav files in the source directory
wav_files = [f for f in os.listdir(source_dir) if f.endswith('.wav')]

# Split the files into train, dev, and test sets
train_files, test_dev_files = train_test_split(wav_files, test_size=0.2, random_state=42)
dev_files, test_files = train_test_split(test_dev_files, test_size=0.5, random_state=42)

# Function to create folders and move files
def create_folders_and_move_files(file_list, parent_dir):
    for file_name in file_list:
        # Create a folder named after the file (without the extension)
        folder_name = os.path.splitext(file_name)[0]
        folder_path = os.path.join(parent_dir, folder_name)
        os.makedirs(folder_path+"/audio", exist_ok=True)
        
        # Move the file into the newly created folder
        shutil.copy2(os.path.join(source_dir, file_name), folder_path+"/audio")

# Create folders and move files
create_folders_and_move_files(wav_files, base_dir)

# Function to write file names to a text file
def write_filenames_to_text(file_list, file_path):
    with open(file_path, 'w') as file:
        for file_name in file_list:
            file.write(f"{file_name}\n")

# Write train, dev, and test filenames to text files
write_filenames_to_text(train_files, os.path.join(base_dir, 'train.txt'))
write_filenames_to_text(dev_files, os.path.join(base_dir, 'dev.txt'))
write_filenames_to_text(test_files, os.path.join(base_dir, 'test.txt'))

print("Folders created and file lists saved.")

