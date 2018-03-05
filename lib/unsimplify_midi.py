import os
#track, time, note_on_c, channel, note, velocity
DATA_DIR = "../data/processed/"
OUTPUT_DIR = "../data/unprocessed/"
MAX_NOTE_TIME = 15000 # TODO : Define MAX_NOTE_TIME as the highest timestamp where a note is played, produces by the neural network
for filename in os.listdir(DATA_DIR):
    if filename.endswith(".processed"):
        previous_time = -1
        track_number = 1
        my_file = open(DATA_DIR+filename, "r")
        output_file = open(OUTPUT_DIR+filename+".csv", "w")
        output_file.write("0, 0, Header, 1, 1, 480\n")
        output_file.write("1, 0, Start_track\n")
        file_content = my_file.readlines()
        for line in file_content:            
            line_split = line.split(',')
            if int(line_split[0]) < previous_time:
                output_file.write(str(track_number)+", "+str(previous_time)+", End_track\n")
                track_number = track_number + 1
                output_file.write(str(track_number)+", 0, Start_track\n")
            previous_time = int(line_split[0])
            output_file.write(str(track_number)+", "+line_split[0]+", Note_on_c, 0,"+line_split[1]+","+line_split[2])
        output_file.write(str(track_number)+", "+str(MAX_NOTE_TIME)+", End_track\n")
        output_file.write("0, 0, End_of_file\n")