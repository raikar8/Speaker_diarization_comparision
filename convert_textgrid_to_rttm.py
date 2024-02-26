from textgrid import TextGrid
import glob

def merge_textgrids_to_rttm(doctor_textgrid_path, patient_textgrid_path, rttm_output_path, recording_id="recording"):
    # Load the TextGrid files
    doctor_tg = TextGrid.fromFile(doctor_textgrid_path)
    patient_tg = TextGrid.fromFile(patient_textgrid_path)
    
    # Initialize a list to hold all intervals
    intervals = []

    # Extract intervals from the Doctor's TextGrid and add them to the list
    for interval in doctor_tg[0]:
        if interval.mark.strip():  # Ignore empty labels
            #print(interval.mark.strip())
            intervals.append((interval.minTime, interval.maxTime, "SPEAKER_00"))
    
    # Extract intervals from the Patient's TextGrid and add them to the list
    for interval in patient_tg[0]:
        if interval.mark.strip():  # Ignore empty labels
            intervals.append((interval.minTime, interval.maxTime, "SPEAKER_01"))

    # Sort the intervals by start time
    intervals.sort(key=lambda x: x[0])

    # Open the RTTM output file
    with open(rttm_output_path, 'w') as rttm_file:
        for start_time, end_time, speaker in intervals:
            duration = end_time - start_time
            # Write to RTTM: SPEAKER <file_id> 1 <start> <duration> <NA> <NA> <speaker> <NA> <NA>
            rttm_file.write(f"SPEAKER {recording_id} 1 {start_time} {duration} <NA> <NA> {speaker} <NA> <NA>\n")

# Example usage

Doctor_TextGrid_files = glob.glob("/home/raikar/primock57/transcripts/*doctor.TextGrid")
#Patient_TextGrid_files = glob.glob("/home/raikar/primock57/transcripts/*patient.TextGrid")

for doctor_textgrid_files in Doctor_TextGrid_files:
    print(doctor_textgrid_files)
    patient_textgrid_files = "/home/raikar/primock57/transcripts/"+doctor_textgrid_files.split('.')[0].split('/')[-1].replace('_doctor', '_patient')+".TextGrid"
    print(patient_textgrid_files)
    rttm_output_path = "reference_rttm"+"/"+doctor_textgrid_files.split('.')[0].split('/')[-1].replace('_doctor', '')
    print(rttm_output_path+'.rttm')
    print(doctor_textgrid_files.split('.')[0].split('/')[-1].replace('_doctor', ''))
    merge_textgrids_to_rttm(doctor_textgrid_files, patient_textgrid_files, rttm_output_path+".rttm" ,doctor_textgrid_files.split('.')[0].split('/')[-1].replace('_doctor', ''))
