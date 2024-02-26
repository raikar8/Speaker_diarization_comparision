from pyannote.metrics.diarization import DiarizationErrorRate
from pyannote.core import Annotation



def rttm_to_audacity_label(rttm_path, output_text_path):
    # Open the RTTM file and the output text file
    with open(rttm_path, 'r') as rttm_file, open(output_text_path, 'w') as output_file:
        # Iterate over each line in the RTTM file
        for line in rttm_file:
            # RTTM format: SPEAKER file_id 1 start_time duration <NA> <NA> speaker_label <NA> <NA>
            parts = line.strip().split()
            start_time = float(parts[3])
            duration = float(parts[4])
            end_time = start_time + duration
            speaker_label = parts[7]
            
            # Write to the output file in Audacity label format: start_time end_time label
            output_file.write(f"{start_time}\t{end_time}\t{speaker_label}\n")

# Example usage

import glob
import os

from_file="NEMO_pretrained_test_rttm"
to_file="NEMO_pretrained_test_audacity"

rttm_path = '/home/raikar/primock57/'+from_file+'/*.rttm'

rttm_files = glob.glob(rttm_path)
for rttm_file in rttm_files:
    print(rttm_file)
    audacity_file = os.path.join(to_file,str((rttm_file).split('/')[-1].split('.')[0]+'.txt'))
    print(audacity_file)
#output_text_path = '/home/raikar/primock57/reference_audacity/day1_consulation01.txt'

    rttm_to_audacity_label(rttm_file, audacity_file)

