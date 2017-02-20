from funcs import is_valid
from gez import is_too_small
from brett import get_slice_pos
from liam import slice_pizza

def divide(pizza, pos ):
    """
    divide(pizza, pos, slices)

    input: 
        pizza:  np.array() of doubles containing ones (T), zeros (M) (or small negs)
        pos:    array of positions relative to the mothership pizza, r1, r2, c1, c2
        slices: list containing position array which describe slices

    recursive pizza slicing according to minimum ingredients L and maximum cells H
    """
    # Pizza is small enough and has enough ingredients, save it!
    if is_valid(pizza):
        return [pos] 

    # Pizza is too small to be a slice, give up.
    elif is_too_small(pizza):
        return []

    # Pizza needs to be divided further
    else:
        # Get the side along which slicing should occur, and index of where to slice
        side, idx, to_bin = get_slice_pos(pizza)
        if to_bin:
            return []

        # Slice! Retrieve two new pizzas and their relpositions to the mothership
        pizza1, pizza2, pos1, pos2 = slice_pizza(pizza, pos, idx, is_rows=side)

        # Recursify ;-) 
        slices = []
        slices.extend(divide(pizza1,pos1))
        slices.extend(divide(pizza2,pos2))
        return slices
