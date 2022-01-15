def kangaroo(x1, v1, x2, v2):
    '''
    You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. 
    If it is possible, return YES, otherwise return NO.

    int x1, int v1: starting position and jump distance for kangaroo 1
    int x2, int v2: starting position and jump distance for kangaroo 2
    
    Returns: string: either YES or NO

    '''
    if (v1 > v2) and (x2 - x1) % (v2 - v1) == 0:
        return "YES"
    else:
        return "NO"