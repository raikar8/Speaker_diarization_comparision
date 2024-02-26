import json
meta = {
    'audio_filepath': an4_audio, 
    'offset': 0, 
    'duration':None, 
    'label': 'infer', 
    'text': '-', 
    'num_speakers': 2, 
    'rttm_filepath': None, 
    'uem_filepath' : None
}
with open('data/input_manifest.json','w') as fp:
    json.dump(meta,fp)
    fp.write('\n')

#!cat data/input_manifest.json

#output_dir = os.path.join(ROOT, 'oracle_vad')
#os.makedirs(output_dir,exist_ok=True)
