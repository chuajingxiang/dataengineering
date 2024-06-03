#This script intends to mask sensitive information with * and generate a sanitized file.

import re
import os
import glob

def mask_file(input_file_path, output_file_path, keywords):
    # Read the input file and mask the contents
    with open(input_file_path, 'r') as input_file:
        text = input_file.read()
        masked_text = mask_data(text, keywords)

    # Write the masked contents to the output file
    with open(output_file_path, 'w') as output_file:
        output_file.write(masked_text)

def mask_data(text, keywords):
    # Replace each keyword with a mask (e.g. "*********")
    for keyword in keywords:
        mask = "*" * len(keyword)
        text = text.replace(keyword, mask)

    return text


#Need to input absolute path
user_root_directory = input("What is the root directory location: ")
user_output_folder = input("What is the output directory location: ")


root_directory = r"" + user_root_directory
output_folder = r"" + user_output_folder


# Get a list of all files in the directory and its subdirectories
file_list = glob.glob(os.path.join(root_directory, '**/*'), recursive=True)
for cur_file_path in file_list:
    if os.path.isfile(cur_file_path):
        cur_input_file_path = r"" + cur_file_path
        print("Current input file: " + cur_input_file_path)
        cur_filename = cur_file_path.split("\\")[-1]
        cur_output_file_path = output_folder + "\\" + cur_filename + ".sanitized"
        cur_output_file_path = r"" + cur_output_file_path
        print("Output file: " + cur_output_file_path)
        keywords = ['sampletext1','sampletext2','sampletext3','sampletext4','sampletext5','sampletext6']
        mask_file(cur_input_file_path, cur_output_file_path, keywords)
