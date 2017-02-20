import numpy as np
from gez import *

def remove_slice_copy( pizza, rows, cols):
    """
    set area given by (rows,cols) to fill
    returns new pizza
    """
    result = np.copy(pizza)
    result[ rows[0]:rows[1]+1, cols[0]:cols[1]+1 ]= -1e-50
    return result

def remove_slice(pizza,rows,cols):
    """
    set area given by (rows,cols) to fill
    writes in place
    """
    pizza[ rows[0]:rows[1]+1, cols[0]:cols[1]+1 ]= -1e-50
    return pizza

def slice_pizza( pizza, pos, idx, is_rows=True):
    """
    pizza : np 2d array, pizza
    pos: positions of lower left and upper right
    idx : integer, slice index (slices from 0 up to idx)
    is_rows : bool, slicing on a row index?
    """
    if( is_rows):
        L = pizza[ :idx, :]
        R = pizza[ idx:, :]
        L_pos = Pos( pos.r1 , pos.c1, pos.r1+idx-1, pos.c2 )
        R_pos = Pos( pos.r1+idx, pos.c1 , pos.r2, pos.c2 )
    else:
        L = pizza[ :, :idx]
        R = pizza[ :, idx:]
        L_pos = Pos( pos.r1, pos.c1, pos.r2, pos.c1+idx-1 )
        R_pos = Pos( pos.r1, pos.c1+idx, pos.r2, pos.c2 )
    return L, R, L_pos, R_pos
