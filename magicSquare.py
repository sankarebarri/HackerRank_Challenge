def magicSquare(s):
    '''
    It checked if a 3x3 matrix is a magic square.

    Parameters
    ----------
    s : matrix x

    Returns
    -------
    True: if it is a magic matrix
    False: if it is not

    '''
    row = []
    for i in range(3):
        row.append((sum(s[i])))
        
    column = []
    for i in range(3):
        column.append((s[0][i]+s[1][i]+s[2][i]))
        
    diag = []
    diag.append((s[0][0]+s[1][1]+s[2][2]))
    diag.append((s[0][2]+s[1][1]+s[2][0]))
        
    magic_list = [row, column, diag]

    for i in magic_list:
        for j in i:
            if j != 15:
                return False
                break
    return True