# read a text file and paste content in another file
import os
import sys

from customExceptions.FourDivisionError import FourDivisionError
base_path = "C:/Users/garima.agarwal/Desktop"

test = os.path.join(base_path, "python.txt")

## when we read a file
# 1)we open a file
# 2)we decide which mode do we want, read, read-write, write, rb etc
# 3)do our operation
# 4)close the connection

data_to_write = []
try:
    with open(test, "r+") as file:
        print(file.__sizeof__())
        for row in file:
            try:
                a = 2//4
                if isinstance(a, int):
                    raise FourDivisionError("hdwjsadhna")
            except ZeroDivisionError as e:
                raise e
            data_to_write = row.split('w')
        file.write("wefewfrfewdsacdsad")
    print(data_to_write)
except IOError as e:
    raise e
finally:
    print("i am in finally")



# print every line in a new line a new a file
# create a new file
# final_directory = "C:/test"
# if os.path.isdir(final_directory):
#
#     with open("C:/test/test.txt", "w") as write_file:
#         for row in data_to_write:
#             write_file.write(row)
#             write_file.write("\n")
# else:
#     os.mkdir(final_directory)
#     with open("C:/test/test.txt", "w") as write_file:
#         for row in data_to_write:
#             write_file.write(row)
#             write_file.write("\n")


## assignment
## in a set of files arrange the file names in an order on the chain
## you find a chain when the last line of a file is the first line of another file

## find all modes in which we can open a file and write it;s description








