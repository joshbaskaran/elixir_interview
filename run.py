# Driver script to launch the needed modules
# for a real project, better to use __init__.py
# and create a package instead

import sys
from os.path import exists as file_exists
import FileReader as fr
import Calculator as calc
import time

def overlap_positions(segment_1:fr.FileReader, segment_2:fr.FileReader) -> None:
    """Takes two segment files as input and prints the number of overlaps"""

    count:int = calc.CustomStatistics.count_overlaps_2(segment_1.segment_list,segment_2.segment_list)
    print("Number of overlapping positions between {} and {} is {}".format(segment_1.file_name, segment_2.file_name, count))
    
def perason_correlation(function_1:fr.FileReader, function_2:fr.FileReader) -> None:
    """Takes two function files as input and calculates the sample pearson correlation"""

    corr:float = calc.CustomStatistics.p_corr(function_1.function_list_ndarray, function_2.function_list_ndarray)
    print("Pearson correlation between {} and {} is {}".format(function_1.file_name, function_2.file_name, corr))

def mean_seg_func(segment:fr.FileReader, function_:fr.FileReader) -> float:
    """
    Takes a segment and a function file and returns the average of the values in the function file
    indexed on the positions from the segment file.
    """

    average: float = calc.CustomStatistics.average(segment.segment_list, function_.function_list_ndarray)
    print("Average of functions in {} based on segments in {} is {}".format(segment.file_name, function_.file_name, average))


def main():
    try:
        if not file_exists(sys.argv[1]): raise FileExistsError
    except FileExistsError:
        print("{}: No such file".format(sys.argv[1]))
        sys.exit(1)
    
    try:
        if not file_exists(sys.argv[2]): raise FileExistsError
    except FileExistsError:
        print("{}: No such file".format(sys.argv[2]))
        sys.exit(1)

    input_1 = fr.FileReader(sys.argv[1])
    input_2 = fr.FileReader(sys.argv[2])

    if input_1.file_extention == input_2.file_extention == 's': overlap_positions(input_1, input_2)
    elif input_1.file_extention == input_2.file_extention == 'f': perason_correlation(input_1, input_2)
    else:
        if input_1.file_extention == 's': mean_seg_func(input_1, input_2)
        else: mean_seg_func(input_2, input_1)

if __name__ == "__main__":
    start = time.time()
    main()
    stop = time.time()
    print("Time = {}".format(stop-start))