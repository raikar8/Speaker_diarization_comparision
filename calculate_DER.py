from pyannote.core import Annotation
from pyannote.metrics.diarization import DiarizationErrorRate
from pyannote.database.util import load_rttm
import os

def calculate_average_der(reference_dir, hypothesis_dir):
    # Initialize the diarization error rate metric
    metric = DiarizationErrorRate()

    # Initialize a list to store DERs for each file
    ders = []

    # Loop over the RTTM files in the reference directory
    for reference_filename in os.listdir(reference_dir):
        if reference_filename.endswith('.rttm'):
            # Construct the full paths to the reference and hypothesis RTTM files
            reference_rttm_path = os.path.join(reference_dir, reference_filename)
            hypothesis_rttm_path = os.path.join(hypothesis_dir, reference_filename)
            print(reference_rttm_path)
            print(hypothesis_rttm_path)
            # Load the reference and hypothesis annotations
            reference_annotations = load_rttm(reference_rttm_path)[next(iter(load_rttm(reference_rttm_path)))]
            hypothesis_annotations = load_rttm(hypothesis_rttm_path)[next(iter(load_rttm(hypothesis_rttm_path)))]

            # Compute DER for the current file and add it to the list
            der = metric(reference_annotations, hypothesis_annotations)
            ders.append(der)

    # Calculate the average DER
    average_der = sum(ders) / len(ders)
    
    return average_der

# Specify the directories containing the reference and hypothesis RTTM files
reference_dir = '/home/raikar/primock57/reference_test_rttm'
hypothesis_dir = '/home/raikar/primock57/PYANNOTE_test_rttm'

# Calculate average DER
average_der = calculate_average_der(reference_dir, hypothesis_dir)
print(f"Average Diarization Error Rate (DER): {average_der:.2%}")

