from sys import exit # masks exit() with sys.exit()
import numpy as np

# For bigger projects, all custom expections would ideally be in a separate file 
class FileExtentionError(Exception):
    pass

class BadSegmentFileError(Exception):
    pass

class BadFunctionFileError(Exception):
    pass

# read input files
class FileReader():   
    # This could potentially be more modular if we are to make it into a class 
    # for reading all the file types with various fields and not just tables
    def __init__(self, path: str):
        """
        Reads the file at the provided path and generates a list and a numpy array appropriate to the file extention.
        """
        # if the file extentions list becomes too large, list of file extentions should be moved into a separate file eg. contants.py

        self.valid_file_extentions: list = ['s', 'f']
        self.file_path = path
        self.file_name = self.file_path.split('/')[-1]
        self.file_extention = self.file_path.split('.')[-1]
        self.read_file()

    def read_file(self):
        """Checks file extension and calls the appropriate function to read the file"""
        if self.file_extention not in self.valid_file_extentions: raise FileExtentionError("{} not a valid file type".format(self.file_extention))
        
        # From python 3.10 this should be replaced with a match clause instead
        if self.file_extention == "s": self.read_segment_file()
        if self.file_extention == "f": self.read_function_file()
        
    # read input file and return as a list
    def read_segment_file(self):
        """Reads a segment file and converts it into a list of lists and a 2D numpy array"""
        self.segment_list: list = []

        try:
            with open(self.file_path, 'r') as input_handle:
                for line in input_handle:
                    self.segment_list.append([int(val) for val in line.strip().split()]) # Convert to int
        except ValueError:
            raise ValueError("{} file contains non-integer values".format(self.file_name))

        if not all(len(sub)==2 for sub in self.segment_list): raise BadSegmentFileError("{} segment file does not contain 2 entries in each row".format(self.file_name))

        start, end = self.segment_list[0]
        for index in range(1, len(self.segment_list)):
            if self.segment_list[index][0] < end:
                raise BadSegmentFileError("{} segment file has overlaping positions".format(self.file_name))
            start = self.segment_list[index][0]
            end = self.segment_list[index][-1]

        
        # save as numpy array in the class instance for quick math operations.
        # On the fly conversion would be better for saving memory, instead of 
        # saving directly in the class instance.
        self.segment_list_ndarray: np.ndarray = np.asarray(self.segment_list, dtype=int)


    def read_function_file(self):
        """Reads a function file and converts it into a list and a 1D numpy array"""
        self.function_list: list = []
        try:
            with open(self.file_path, 'r') as input_handle:
                for line in input_handle:
                    self.function_list.append(float(line.strip()))
        except ValueError:
            raise ValueError("{} file contains values not convertable to type float".format(self.file_name))

        if len(self.function_list) != 10000000: raise BadFunctionFileError("{} function file does not contain 10,000,000 lines".format(self.file_name))

        self.function_list_ndarray: np.ndarray = np.asarray(self.function_list, dtype=float)
