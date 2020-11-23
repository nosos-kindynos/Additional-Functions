def estimate_time(processer_frequency,accuracy):
    from functools import reduce
    n=len(paths)
    def ncr(n, r):
        r = min(r, n-r)
        numer = reduce(op.mul, range(n, n-r, -1), 1)
        denom = reduce(op.mul, range(1, r+1), 1)
        return numer // denom  # or / in Python 2
    s=0
    for i in range(1, n+1):
        s += i*accuracy*(ncr(n, i))
        k = s/(processer_frequency)
    return(k)
