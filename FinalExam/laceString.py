#PROBLEM 5  (10 points possible)
#Suppose you are given two strings (they may be empty), s1 and s2. You
#would like to "lace" these strings together, by successively alternating
#elements of each string (starting with the first character of s1). If
#one string is longer than the other, then the remaining elements of the
#longer string should simply be added at the end of the new string.

#For example, if we lace 'abcd' and 'efghi',
#we would get the new string: 'aebfcgdhi'.

#Write an iterative procedure, called laceStrings(s1, s2) that does this.

#Note: You will only get ten checks. Use these judiciously.

def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    new_lace = ''
    len_s1 = len(s1)
    len_s2 = len(s2)
    if len_s2 == len_s1:
      for index in range(len_s1):
        new_lace += s1[index] + s2[index]
    else:
      lace = min(len_s2, len_s1)
      for j in range(lace):
        new_lace += s1[j] + s2[j]
      if len_s2 < len_s1:
        new_lace += s1[len_s2:]
      else:
        new_lace += s2[len_s1:]
    return new_lace


laceStrings('Shruthik','alle')
print(laceStrings('Shruthik', 'alle'))
