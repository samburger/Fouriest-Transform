"""
Computes the Fouriest transform of a given base-10 integer.
Based on the SMBC comic: http://www.smbc-comics.com/?id=2874
"""
from math import floor
number = 624

def convert_base(num,to_base):
    if num <= to_base:
        if to_base == 2:
            return str(num-1)
        else:
            return str(num)
    else:
        return convert_base((floor(num/to_base)),to_base) + str(divmod(num,to_base)[1])

"""
Once we reach a base of at least 10 (the input number), we can't get results of more digits than the input number.
So once we're past base 10, the first result of all 4s is the base of the Fouriest transform.
Otherwise if we find a base resulting in a number of 4s greater than the length of the input number, and if we have
tried all bases 2-9, we know that the base is the Fouriest transform.
"""
def fouriest_transform(num):
    cur_base = 4  # First base system where 4's exist.
    results = []
    max_fours = (0, 4)  # (number of fours, base producing that result)
    while True:
        results.append([convert_base(num, cur_base), cur_base, convert_base(num, cur_base).count('4')])
        if results[-1][2] > max_fours[0]:
            max_fours = (results[-1][2], results[-1][1])
        if cur_base > 9:
            if max_fours[0] >= len(str(num)):
                print("The Fouriest Transform of " + str(num) + " is " + str(convert_base(num,max_fours[1])) + " which is the base " + str(max_fours[1]) + " form.")
                return
        if cur_base == 100:
            print("No Fouriest Transform found in bases 4-100.")
            return
        cur_base += 1

fouriest_transform(number)