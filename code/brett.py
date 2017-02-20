from funcs import *
from gez import ratio, is_too_small

""" Iterate over the different possible slices for both sides of the array.
    Returns the axis being sliced along and the index of the best slice.

    The index is such that arr(0:index,:) gives the left slice and
    arr(index:length,:) gives the right slice. Assuming axis = 0.
"""
def get_slice_pos(arr):

    length = arr.shape[0]
    width = arr.shape[1]

    best_score = 0
    # loop over all axis=0 sweeps
    for i in range(1,length):
        print(i)
        score = get_slice_cut_score(arr, length, i, 0)
        print(score)
        if score > best_score:
            best_score = score
            best_cut = i
            is_rows = True
    # loop over all axis=1 sweeps
    for i in range(1,width):
        print(i)
        score = get_slice_cut_score(arr, width, i, 1)
        print(score)
        if score > best_score:
            best_score = score
            best_cut = i
            is_rows = False

    return is_rows, best_cut



# work out the score for the slice by adding the left and right slice ratios
def get_slice_cut_score(arr, length, slice_point, axis):

    if axis == 0:
        left = arr[ :slice_point,:]
        right = arr[ slice_point:, :]
    else:
        left = arr[ :, :slice_point]
        right = arr[ :, slice_point:]

    # check if either half of the split is too small to possibly be a valid slice
    # and give a score of zero accordingly
    if is_too_small(left):
        if is_too_small(right):
            return 0
        else:
            return 0 + ratio(right)
    elif is_too_small(right):
        return ratio(left) + 0
    else:
        return ratio(left) + ratio(right)
