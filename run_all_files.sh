#!/bin/bash

SOURCE_DIR=/home/raikar/primock57/output/mixed_audio

echo "$SOURCE_DIR"
for file in "$SOURCE_DIR"/*; do
  # Extract the filename without its path and extension
  filename=$(basename -- "$file")
  extension="${filename##*.}"
  filename="${filename%.*}"
  
  # Define the output path and filename
  output="$SOURCE_DIR/${filename}.wav"
  echo "$output"
  echo "$filename"

  python3 run_pyannote.py $output $filename
 
done

echo "Conversion complete."
