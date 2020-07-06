import numpy as np


# Define a main() function that divide each column of the array
# element-wise with another array.
def main():
    a = np.arange(25).reshape(5, 5)
    b = np.array([1., 5, 10, 15, 20])

    result = a / b[:, np.newaxis]

    print(result)


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
