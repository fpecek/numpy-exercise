import numpy as np


# Define a main() function that generates a 10 x 3 array of random numbers
# and for each row pick the number closest to 0.5.
def main():
    rand_arr = np.random.random((10, 3))
    print(rand_arr)
    abs_arr = abs(rand_arr - 0.5)
    min_idx = np.argmin(abs_arr, axis=1)
    print(rand_arr[np.arange(len(rand_arr)), min_idx])

    # argsort solution #
    # mask = abs_arr.argsort(axis=1)
    # i = np.arange(len(rand_arr))[:, np.newaxis]
    # sorted_arr = rand_arr[i, mask]
    # print(sorted_arr[:, :1])


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
