import numpy as np


# Define a main() function that transpose matrix and
# create view array containing only 2nd and 4th row.
def main():
    arr = np.arange(1, 16).reshape(3, 5)
    arr_transpose = arr.T
    print(arr_transpose)

    second_and_forth_row_arr = arr_transpose[[1, 3], :]
    print(second_and_forth_row_arr)


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
