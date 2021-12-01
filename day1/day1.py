import numpy as np

arr = np.loadtxt('input.txt')

# part 1 use diff 

increasing_idx = np.where(np.diff(arr) > 0)[0] + 1
print('Result part 1: ', increasing_idx.shape[0])

# part 2 sum of window = sum of three times the array with respective shifts of 0, 1 and 2
windows_sum = arr + np.roll(arr, 1) + np.roll(arr, 2)
windows_sum = windows_sum[2:] # ignore 2 first elements because they have an overlapping window with the front and back of the array
increasing_idx_windows = np.where(np.diff(windows_sum) > 0)[0] + 1
print('Result part 2: ', increasing_idx_windows.shape[0])