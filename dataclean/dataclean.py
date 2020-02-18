import pandas as pd

def find_bad_data(filename, sep = ',', verbose = 'No'):
    """Scans a csv file and checks for consistent number of columns.  
    Returns a list of line numbers that are inconsistent
    """

    bad_lines = []
    line_num = 1

    with open(filename,"r") as fp:
        num_columns = len(fp.readline().split(sep=sep))

        for line in fp:
            line_num += 1
            if len(line.split(sep=sep)) != num_columns:
                bad_lines.append(str(line_num)+": "+line)
    
    if verbose == 'Yes':
        print(f"The proper number of columns is {num_columns}")
        print("Bad lines:")
        print(*bad_lines,sep='\n')


    return bad_lines

