import numpy as np

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
    pos: [[r1,c1],[r2,c2]], positions of lower left and upper right
    idx : integer, slice index (slices from 0 up to idx)
    is_rows : bool, slicing on a row index?
    """
    if( is_rows):
        L = pizza[ :idx, :]
        R = pizza[ idx:, :]
        L_pos = [ pos[0] , [ pos[0][0]+idx, pos[1][1]] ]
        R_pos = [ [pos[0][0]+idx,pos[0][1]] , pos[1] ]
    else:
        L = pizza[ :, :idx]
        R = pizza[ :, idx:]
        L_pos = 0
        R_pos = 1
    return L, R, L_pos, R_pos
