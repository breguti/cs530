import numpy as np


def location_address():
    array_array = user_input()

    for temp in array_array:
        if len(array_array[temp]) == 3:  # if three elements there is label[0], instruction[1], and context[2]
            label = array_array[temp][0]
            instruction = array_array[temp][1]
            context = array_array[temp][2]

        elif len(array_array[temp]) == 2:  # if two elements there is instruction[0] and  context[1]
            instruction = array_array[temp][0]
            context = array_array[temp][1]

        elif len(array_array[temp]) == 1:  # if one label there is only instruction[0]
            instruction = array_array[temp][0]


def user_input():
    # read in line of code and seperate data list of string array
    text_file = open("SIC:XE PROGRAM.txt")
    line_array = text_file.readlines()
    line_array = [x.strip() for x in line_array]
    array_array = []
    num_lines = 0

    for temp in line_array:
        num_lines = num_lines + 1
        string_array = temp.split()
        array_array.append(string_array)

    return array_array


def main():
    location_address()


if __name__ == "__main__":
    main()