import sys

sys.setrecursionlimit(15000)


def dialer(start, hops, cache={}):
    if (start, hops) in cache:
        return cache[(start, hops)]
    result = dialer_uncached(start, hops)
    cache[(start, hops)] = result
    return result


def dialer_uncached(start, hops):
    if hops == 0:
        return 1
    return sum([0 + dialer(n, hops - 1) for n in neighbours(start)])


def dialer_dp(start, hops):
    prev_hops = [1] * 10
    current_hops = [1] * 10
    for i in range(0, hops):
        for j in range(0, 10):
            current_hops[j] = sum([prev_hops[n] for n in neighbours(j)])
        prev_hops = current_hops.copy()

    return current_hops[start]


def neighbours(position):
    p = {
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [3, 9, 0],
        5: [],
        6: [1, 7, 0],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4],
        0: [4, 6],
    }
    return p[position]
