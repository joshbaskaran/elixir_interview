# elixir_interview
Solutions for the ELIXIR/ UiO interview problems

## Dependency requirements
The code should be runnable as long as both **python3** and **numpy** are installed.

A list of exact dependencies are given in the _requirements.txt_ file.
This can be used to produce the exact environment in which this solution was written.

On a linux system (64bit architecture) with a conda installation, simply run the following command in your favorite shell:

`conda create --name <env> --file requirements.txt`
`conda activate <env>`

## Running
To run the code, call the run.py followed by 2 input files like so:

`python run.py <input_file_1> <input_file_2>`

 ## Side note
 Within the Calculator.py, the function for counting the overlap between 2 segment files has been implemented twice.
 the 1st implementation, `count_overlaps` is more pythonic and readable/maintainable but slow while the second, `count_overlaps_2` is far less readable and hence harder to maintain but is almost twice as fast.
 Within the run.py, only the second implementation has been called.

## Possible improvements

### Unit testing
1. The unit testing of the Calculator module can be more robust buy testing more edge cases
2. Although possible exceptions have been handled for the FileReader class, these can be unit tested using the `unittest.mock` library and modelling a fake instance to check the side effects/ exceptions for the methods in the `FileReader.FileReader` class

### Extensibility
The FileReader class can be made more modular for easier extension for other file types. Particularly,
the declaration of possible file extensions could be made in a config file or drawn from a database instead.
In addition, the checking of the files' contents to validate if it matched the used extension could be written as a separate class instead of as part of the function definition which could be inherited by the FileReader class. This would make the code easier to maintain and extend.
Currently, the `read_segmentation_file()` performs both validating the file type as well as reading the file in one function, making it less modular. Implementing the above suggestion would make it easier to adhere to the _one function, one job_ rule.

### Scalability
Although not required here, it would be beneficial to implement parallelization here for future scalability. For example, the processing of the two input files, currently, happens successively, but can be parallelized instead. This requires some tweaking of the code of course, but something similar to the following can be implemented:
```
from multiprocessing import Pool
pool = Pool(2)
pool.map(read_file, [file_1, file_2])
```