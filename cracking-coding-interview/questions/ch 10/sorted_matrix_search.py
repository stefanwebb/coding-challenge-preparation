# Q10.9: Sorted matrix search
import numpy as np

# NOTE: This solution doesn't work because my reasoning was incorrect... :(
def sorted_matrix_search(matrix, x):
    # Initialize bounds
    rows_upper, cols_upper = matrix.shape
    rows_upper -= 1
    cols_upper -= 1 
    rows_lower = cols_lower = 0

    # binary search in two-dimensions
    # TODO: Should this be "and" or "or"???
    while True  #rows_lower < rows_upper or cols_lower < cols_upper:
        rows_median = (rows_lower + rows_upper)//2
        cols_median = (cols_lower + cols_upper)//2

        # Adjust the columns
        if cols_lower < cols_upper:
            if matrix[rows_lower, cols_median] > x:
                cols_upper = cols_median - 1
            elif matrix[rows_lower, cols_median] < x:
                cols_lower = cols_median + 1
            else:
                return (rows_lower, cols_median)

        # Adjust the rows
        if rows_lower < rows_upper:
            if matrix[rows_median, cols_lower] > x:
                rows_upper = rows_median - 1
            elif matrix[rows_median, cols_lower] < x:
                rows_lower = rows_median + 1
            else:
                return (rows_median, cols_lower)

        else:
            return None
