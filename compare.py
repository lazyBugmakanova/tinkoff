import argparse
import re


def levenshtein_distance(line_one, line_two):
    len_one, len_two = len(line_one), len(line_two)
    cur_row = range(len_one + 1)
    for i in range(1, len_two + 1):
        prev_row, cur_row = cur_row, [i] + [0] * len_one
        for j in range(1, len_one + 1):
            change = prev_row[j - 1]
            if line_one[j - 1] != line_two[i - 1]:
                change += 1
            cur_row[j] = min(prev_row[j] + 1, cur_row[j - 1] + 1, change)

    return round(cur_row[len_one] / len_one, 3)


parser = argparse.ArgumentParser()
parser.add_argument('one_dir', type=str, help='File One')
parser.add_argument('two_dir', type=str, help='File Two')
args = parser.parse_args()
output = open(args.two_dir, "w+")
output.close()
with open(args.one_dir, 'r') as input_file:
    for line in input_file:
        one_path, two_path = line.rstrip().split()
        with open(one_path, 'r') as file_one:
            one_line = file_one.read()
        with open(two_path, 'r') as file_two:
            two_line = file_two.read()
        output = open(args.two_dir, "a+")
        output.write(f"{str(levenshtein_distance(one_line, two_line))}\n")
        output.close()
