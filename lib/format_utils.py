def processed_to_2d_array(input_file):
    input_file = open(input_file, "r")
    file_lines = input_file.readlines()
    output_list = list()
    for file_line in file_lines:
        note_info = file_line.split(',')
        note_info_list = list()
        for ni in note_info:
            note_info_list.append(int(ni.strip(' ')))
        output_list.append(note_info_list)
    return output_list
