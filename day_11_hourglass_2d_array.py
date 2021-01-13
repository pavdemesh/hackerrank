"""There are 6 lines of input, where each line contains 6 space-separated integers
 that describe the 2D Array A. Print the maximum hourglass sum in A.
 """
import sys

if __name__ == '__main__':
    # Define empty list to hold our 2D-Array
    arr = []
    # Get input, convert to int and populate 2D-array
    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))

    # GET INPUT WITH SYS.STDIN:
    input_lines = sys.stdin.readlines()
    for line in input_lines:
        row = list(map(int, line.strip().split()))
        arr.append(row)

    # Define function to get the hourglass sum
    # Parameters: location [i],[j] and the array
    def fn_sum_hourglass(i, j, array):
        # Calculate sums for each of 3 rows in hourglass
        sum1 = array[i][j] + array[i][j+1] + array[i][j+2]
        sum2 = array[i+1][j+1]
        sum3 = array[i+2][j] + array[i+2][j+1] + array[i+2][j+2]
        # Return result
        return sum1 + sum2 + sum3
    # Define variables to hold maximum nd current hourglass sum
    max_hourglass = -999
    cur_hourglass = None
    # Iterate over indices stopping before index len(arr) - 2
    for i in range(len(arr) - 2):
        for j in range(len(arr) - 2):
            # Calculate hourglass sum for the current hourglass
            cur_hourglass = fn_sum_hourglass(i, j, arr)
            # Update max_hourglass if necessary
            max_hourglass = max(cur_hourglass, max_hourglass)

    print(max_hourglass)
