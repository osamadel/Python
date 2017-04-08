def stdDevOfLengths(L):
    N = len(L)
    std = 0
    if N == 0:
        return float('NaN')
    mean = sum(list(map(lambda x: len(x),L))) / float(N)
    for item in L:
        std += (len(item) - mean) ** 2
    return (std / N) ** 0.5

L = ['apples', 'oranges', 'kiwis', 'pineapples']
print(stdDevOfLengths(L))