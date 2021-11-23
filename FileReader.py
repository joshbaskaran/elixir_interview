from sys import exit # masks exit() with sys.exit()
import numpy as np

# For bigger projects, all custom expections would ideally be in a separate file 
class FileExtentionError(Exception):
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
        if not isinstance(path, str): raise TypeError("{path} must be a string")


        self.valid_file_extentions: list = ['s', 'f']
        self.file_path = path
        self.file_name = self.file_path.split('/')[-1]
        self.file_extention = self.file_path.split('.')[-1]
        self.read_file()

    def read_file(self):
        try:
            if self.file_extention not in self.valid_file_extentions: raise FileExtentionError
        except FileExtentionError:
            print("{} is Not a valid file extention.".format(self.file_extention))
            exit(1)
        
        # From python 3.10 this should be replaced with a match clause instead
        if self.file_extention == "s": self.read_segment_file()
        if self.file_extention == "f": self.read_function_file()
        
    # read input file and return as a list
    def read_segment_file(self) -> list:
        self.segment_list: list = []
        with open(self.file_path, 'r') as input_handle:
            for line in input_handle:
                self.segment_list.append([int(val) for val in line.strip().split()]) # Convert to int
        
        # save as numpy array in the class instance for quick math operations
        # On the fly conversion would be better for saving memory, instead of 
        # saving directly in the class instance.
        self.segment_list_ndarray: np.ndarray = np.asarray(self.segment_list, dtype=int)


    def read_function_file(self):
        self.function_list: list = []
        with open(self.file_path, 'r') as input_handle:
            for line in input_handle:
                self.function_list.append(float(line.strip()))
        self.function_list_ndarray: np.ndarray = np.asarray(self.function_list, dtype=float)
