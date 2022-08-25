def permutation(n):
    if n <= 1:
        return 1
    else:
        return n * permutation(n - 1)

def arrangement(n, k):
    return permutation(n) / permutation(n - k)

def combination(n, k):
    return permutation(n) / permutation(n - k) / permutation(k)

