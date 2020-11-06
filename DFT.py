import numpy as np
import matplotlib.pyplot as plt


# https://stackoverflow.com/questions/15424449/calculating-nth-roots-of-unity-in-python
def nthRootsOfUnity(n):
    return np.exp(2j * np.pi / n * np.arange(n))


N = 48

# def F(x):
#     return 1 if x % 5 == 0 else 0


Fs = [
    lambda x: 1,
    lambda x: x % 2,
    lambda x: x % 3,
    lambda x: 1 if x % 3 == 0 else 0,
    lambda x: 1 if x % 3 == 1 else 0,
    lambda x: 1 if x % 3 == 2 else 0,
    lambda x: 1 if x % 4 == 0 else 0,
    lambda x: 1 if x % 5 == 0 else 0,
    lambda x: 5 ** x % 48
]

if __name__ == '__main__':
    roots = nthRootsOfUnity(N)

    DFT_N = np.ones((N, N), dtype=np.complex128)
    for i in range(N):
        for j in range(N):
            DFT_N[i][j] = roots[(-i * j) % N]
    DFT_N /= np.sqrt(N)

    # print(np.round(DFT_N, 5))

    for F in Fs:
        F_kat = np.array([F(x) for x in range(N)]).reshape((N, 1)) / np.sqrt(N)

        # print(F_kat)

        res = DFT_N @ F_kat
        # print(np.round(res, 5))

        plt.plot(np.arange(N), res.conj() * res, marker='o')
        plt.show()
