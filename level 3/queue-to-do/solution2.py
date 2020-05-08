from functools import reduce
def calc_xor(start, end):

    if (end - start) == 0:
        return 0
    if (end - start) == 1:
        return start
    if (end - start) <= 4:
        return reduce(lambda x, y: x ^ y, range(start, end))
    else:
        begin_range = (start, start / 4 * 4 + 4)
        ###print("Begin range",begin_range)
        end_range = (end / 4 * 4, end)
        ###print("End range",end_range)
        return calc_xor(*begin_range) ^ calc_xor(*end_range)


def solution(start, length):
    range_list = [(start + (length - l) * length, start + (length - l) * length + l) for l in range(length, 0, -1)]
    final_xor_list = [calc_xor(start, end) for start, end in range_list]
    return reduce(lambda x, y: x ^ y, final_xor_list)



solution(0,3)