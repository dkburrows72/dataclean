import pandas as pd


def check_line(in_string, quote_char='"', sep=","):
    """returns the count of comma separated items in in_string
    """

    # find start and end of quotes if they exist
    quote_start = in_string.find(quote_char)
    comma_sub = 0
    if quote_start > -1:
        quote_end = in_string.find(quote_char, quote_start + 1)
        # count the number of commas inside the quotes
        comma_sub = in_string[quote_start:quote_end].count(sep)

    # count columns (# commas + 1) and subtract commas inside quotes
    return in_string.count(sep) + 1 - comma_sub


def find_bad_data(filename, sep=",", verbose="No"):
    """Scans a csv file and checks for consistent number of columns.  
    Returns a list of line numbers that are inconsistent
    """

    bad_lines = []
    line_num = 1

    with open(filename, "r") as fp:
        num_columns = len(fp.readline().split(sep=sep))

        for line in fp:
            line_num += 1
            if check_line(line, '"') != num_columns:
                bad_lines.append(str(line_num) + ": " + line)

    if verbose == "Yes":
        print(f"The proper number of columns is {num_columns}")
        print("Bad lines:")
        print(*bad_lines, sep="\n")

    return bad_lines
