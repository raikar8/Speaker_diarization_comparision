import os
import wave

# Specify the directory containing the .wav files
source_dir = '/home/raikar/primock57/output/mixed_audio'

# Specify the directory where you want to save the .uem files
uem_dir = '/home/raikar/primock57/AMI-diarization-setup/uems_medical'

# Create the uem_dir if it does not exist
if not os.path.exists(uem_dir):
    os.makedirs(uem_dir)

# Function to calculate the duration of a wav file
def get_wav_duration(wav_path):
    with wave.open(wav_path, 'r') as wav_file:
        frames = wav_file.getnframes()
        rate = wav_file.getframerate()
        duration = frames / float(rate)
        return duration

# Iterate through all .wav files in the source directory
for wav_file in os.listdir(source_dir):
    if wav_file.endswith('.wav'):
        # Calculate the duration of the wav file
        wav_path = os.path.join(source_dir, wav_file)
        duration = get_wav_duration(wav_path)
        
        # Prepare the content to be written to the .uem file
        file_name_without_ext = os.path.splitext(wav_file)[0]
        content = f"{file_name_without_ext} 1 0.000 {duration:.5f}\n"
        
        # Create and write to the .uem file in the specified uem_dir
        uem_path = os.path.join(uem_dir, f"{file_name_without_ext}.uem")
        with open(uem_path, 'w') as uem_file:
            uem_file.write(content)

print("UEM files have been created and stored in the specified directory.")

