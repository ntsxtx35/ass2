def read_file_create_dict(infile_name):
    """
    This function is used to read data from file and create a dictionary
    :param infile_name: Input file name
    :return: Return the dictionary of the data to use
    """
    dictionary = {}
    values = []
    with open(infile_name, 'r') as infile:

        # Read data by line
        lines = infile.readlines()

        # Loop through each line
        for line in lines:
            current_line = line.split(',')

            # Loop through each word after splitting the line
            for pos in range(1, len(current_line)):

                # Remove the \n character at the end and blank space
                current_line[pos] = current_line[pos].replace('\n', '')
                current_line[pos] = current_line[pos].strip()
                values.append(current_line[pos])

            # Change the data type from string to int
            values[1] = int(values[1])
            values[3] = int(values[3])

            dictionary[current_line[0]] = values
            values = []

    return dictionary


# Write data to the output file
def write_to_file(dictionary, outfile_name):
    """
    This function is used to write the data to the output file
    :param dictionary: The dictionary of data to write to output file
    :param outfile_name: Output file name
    :return:
    """
    with open(outfile_name, 'w') as outfile:

        # Loop through the dictionary of data
        for key, values in dictionary.items():
            outfile.write('%s:%s\n' % (key, values))
