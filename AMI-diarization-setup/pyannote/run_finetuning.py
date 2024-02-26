
import os
os.environ["PYANNOTE_DATABASE_CONFIG"] = "/home/raikar/primock57/AMI-diarization-setup/pyannote/database.yml"
from pyannote.database import get_protocol, FileFinder
dataset = get_protocol("MEDICAL.SpeakerDiarization.mini", {"audio": FileFinder()})



from pyannote.audio import Pipeline
pretrained_pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization-3.1", use_auth_token="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")


# this takes approximately 2min to run on Google Colab GPU
from pyannote.metrics.diarization import DiarizationErrorRate
metric = DiarizationErrorRate()

for file in dataset.test():
    # apply pretrained pipeline
    file["pretrained pipeline"] = pretrained_pipeline(file)

    # evaluate its performance
    metric(file["annotation"], file["pretrained pipeline"], uem=file["annotated"])

print(f"The pretrained pipeline reaches a Diarization Error Rate (DER) of {100 * abs(metric):.1f}% on {dataset.name} test set.")

     
