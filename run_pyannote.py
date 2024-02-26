
import sys
from pyannote.audio import Pipeline
import os

audio_path = str(sys.argv[1])
filename = str(sys.argv[2])

#audio_path = "/home/raikar/primock57/audio/day1_consultation15_doctor.wav"

pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization-3.1",
                                    use_auth_token="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")



diarization = pipeline(audio_path, num_speakers = 2)
# dump the diarization output to disk using RTTM format
with open(str(filename)+".rttm", "w") as rttm:
    diarization.write_rttm(rttm)
