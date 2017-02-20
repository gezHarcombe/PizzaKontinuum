from funcs import *
from gez import *

""" Iterate over the different possible slices of the long side of the array.
    Returns the axis being sliced along and the index of the best slice.

    The index is such that arr(0:index,:) gives the left slice and
    arr(index:length,:) gives the right slice. Assuming axis = 0.
"""
def get_slice_pos(arr):

    if arr.shape[0] > arr.shape[1]:
        long_side = 0
        length = arr.shape[0]
        width = arr.shape[1]
    else:
        long_side = 1
        length = arr.shape[1]
        width = arr.shape[0]

    best_score = 0
    for i in range(1,length):
        score = get_slice_cut_score(arr, length, i, long_side)
        if score > best_score:
            best_score = score
            best_cut = i

    return long_side, i



# work out the score for the slice by adding the left and right slice ratios
def get_slice_cut_score(arr, length, slice_point, axis):
    if axis == 0:
        return ratio(arr[0:slice_point,:]) + ratio(arr[slice_point:length,:])
    else:
        return ratio(arr[:,0:slice_point]) + ratio(arr[:,slice_point:length])
