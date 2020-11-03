import numpy as np


# https://stackoverflow.com/questions/15424449/calculating-nth-roots-of-unity-in-python
def nthRootsOfUnity(n):
    return np.exp(2j * np.pi / n * np.arange(n))


N = 48


def F(x):
    return 5 ** x % 48


if __name__ == '__main__':
    roots = nthRootsOfUnity(N)

    DFT_N = np.ones((N, N), dtype=np.complex128)
    for i in range(N):
        for j in range(N):
            DFT_N[i][j] = roots[(-i * j) % N]

    # print(DFT_N)

    F_kat = np.array([F(x) for x in range(N)]).reshape((N, 1)) / np.sqrt(N)

    # print(F_kat)

    print(DFT_N @ F_kat)
