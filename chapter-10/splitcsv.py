"""
Write a script that will take three required command line arguments - input_file,
output_file, and the row_limit. From those arguments, split the input CSV into
multiple files based on the row_limit argument.
Arguments:
1. -i: input file name
2. -o: output file name
3. -r: row limit to split
Default settings:
1. output_path is the current directory
2. headers are displayed on each split file
3. the default delimiter is a comma
Example usage:
1 # split csv by every 100 rows
2 >> python csv_split.py -i input.csv -o output -r 100
"""
import argparse
import os

def write_chunk(basename, chunk, header, lines):
    with open(basename + str(chunk) + ".csv", "w") as outputfile:
        outputfile.write(header)
        outputfile.writelines(lines)
    
    
parser = argparse.ArgumentParser(description='Split input file into output file(s), limit # rows per file')
parser.add_argument('-i', '--input_file', help='input file name', required=True)
parser.add_argument('-o', '--output_file', help='output file name', required=True)
parser.add_argument('-r', '--row_limit', help='row limit to split file',required=True,type=int)
args = parser.parse_args()

try:
    with open(args.input_file,'r') as input_file:
        lines = input_file.readlines()
except IOError:
    print "Helaas ..."
    exit()

# pop first line into header, remainder stay in lines    
header,lines = lines[0],lines[1:]
line_count = len(lines)
if args.row_limit >= line_count:
    write_chunk(args.output_file,1, header, lines)
else:
    start_index = 0
    end_index   = args.row_limit
    chunk = 1
    while start_index < line_count:
           write_chunk(args.output_file, chunk, header, lines[start_index:end_index])
           chunk += 1
           start_index = end_index
           end_index = min(end_index+args.row_limit,line_count+1)
