def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    # Your code here
    oddNums = []
    for i in L:

        if L.count(i) % 2 is not 0:
            oddNums.append(i)
        
    if not oddNums:
        return None
    return max(oddNums)


a = largest_odd_times([3, 9, 5, 3, 5, 3])
print(a)
