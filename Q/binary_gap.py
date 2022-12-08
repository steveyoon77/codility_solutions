def solution(num):
    gap = max_gap = 0
    start = 0
    while num > 0:
        if start == 0:
            if bin(num & 0b1) == '0b1':
                start = 1
            else:
                num = num >> 1
            continue
        if bin(num & 0b1) == '0b0':
            gap += 1
        else:
            max_gap = max(gap, max_gap)
            gap = 0
        num = num >> 1

    return max_gap
