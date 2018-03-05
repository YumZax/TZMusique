import os
#track, time, note_on_c, channel, note, velocity
DATA_DIR = "../data/processed/"
for filename in os.listdir(DATA_DIR):
    if filename.endswith(".csv"): 
        my_file = open(DATA_DIR+filename, "r")
        output_file = open(DATA_DIR+filename+".processed", "w")
        file_content = my_file.readlines()
        for line in file_content:            
            line_split = line.split(',')
            if " Note_on_c" in line_split:
                output_file.write(line_split[1]+","+line_split[4]+","+line_split[5])