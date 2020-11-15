import numpy as np


# https://stackoverflow.com/questions/15424449/calculating-nth-roots-of-unity-in-python
def nthRootsOfUnity(n):
    return np.exp(2j * np.pi / n * np.arange(n))


n = 4
N = 2 ** n

if __name__ == '__main__':
    roots = nthRootsOfUnity(N)
    print(roots)
    print([np.arccos(roots[2 ** (n - 1 - j)].real) for j in range(1, n)])
