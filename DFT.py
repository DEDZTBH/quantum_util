import numpy as np
import matplotlib.pyplot as plt


# https://stackoverflow.com/questions/15424449/calculating-nth-roots-of-unity-in-python
def nthRootsOfUnity(n):
    return np.exp(2j * np.pi / n * np.arange(n))


N = 16

Fs = [
    # lambda x: 1,
    # lambda x: x % 2,
    # lambda x: x % 3,
    # lambda x: 1 if x % 3 == 0 else 0,
    # lambda x: 1 if x % 3 == 1 else 0,
    # lambda x: 1 if x % 3 == 2 else 0,
    # lambda x: 1 if x % 4 == 0 else 0,
    # lambda x: 1 if x % 5 == 0 else 0,
    # lambda x: 5 ** x % 48,
    # lambda x: np.sqrt(3) if x % 3 == 0 else 0,
    # lambda x: np.sqrt(3) if x % 3 == 1 else 0,
    # lambda x: np.sqrt(3) if x % 3 == 2 else 0,
    # lambda x: 2 if x % 4 == 1 else 0,
    lambda x: (33 ** x) % 91,
]

if __name__ == '__main__':
    roots = nthRootsOfUnity(N)

    DFT_N = np.ones((N, N), dtype=np.complex128)
    for i in range(N):
        for j in range(N):
            DFT_N[i][j] = roots[-(i * j) % N]
    DFT_N /= np.sqrt(N)

    print(DFT_N)

    for F in Fs:
        F_kat = np.asarray([F(x) for x in range(N)]).reshape((N, 1)) / np.sqrt(N)

        # print(F_kat)
        print(np.linalg.norm(F_kat))

        res = DFT_N @ F_kat

        # print(res)

        plt.plot(np.arange(N), np.sqrt(res.conj() * res), marker='o')
        plt.show()

        fmtcomplex = np.vectorize(lambda x: '{},{}'.format(x.real, x.imag))
        np.savetxt('DFT16.csv', fmtcomplex(DFT_N), delimiter=',', fmt='%s')
