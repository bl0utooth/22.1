def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

    for num in range (start, stop + 1): 
        print(num)


count_up(5, 7)        
