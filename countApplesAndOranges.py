def countApplesAndOranges(s, t, a, o, apples, oranges):
    '''
    Sam's house has an apple tree and an orange tree that yield an abundance of fruit. Using the information given below, 
    determine the number of apples and oranges that land on Sam's house.

    In the diagram below:

    The red region denotes the house, where  is the start point, and  is the endpoint. The apple tree is to the left of the house, 
    and the orange tree is to its right.
    Assume the trees are located on a single point, where the apple tree is at point , and the orange tree is at point .
    When a fruit falls from its tree, it lands  units of distance from its tree of origin along the -axis. *A negative value of 
    means the fruit fell  units to the tree's left, and a positive value of  means it falls  units to the tree's right. *
    The function accepts following parameters:
    #  1. INTEGER s
    #  2. INTEGER t
    #  3. INTEGER a
    #  4. INTEGER o
    #  5. INTEGER_ARRAY apples
    #  6. INTEGER_ARRAY oranges

    returns a tuple of number apples and oranges that fell in the house
    '''
    a_count = 0 # apple count
    for i in apples:
        if (i+a) in range(s, t+1):
            a_count += 1
    
    o_count = 0 # orange account
    for i in oranges:
        if (i+o) in range(s, t+1):
            o_count += 1
            
    return (a_count, o_count)