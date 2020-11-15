import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

B = 21
N = 256


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def ord(x):
    i = 1
    a = x
    while a % B != 1:
        a = (a * x) % B
        i += 1
    return i


# https://stackoverflow.com/questions/15424449/calculating-nth-roots-of-unity-in-python
def nthRootsOfUnity(n):
    return np.exp(2j * np.pi / n * np.arange(n))


if __name__ == '__main__':
    print(''.join(['{}: {}\n'.format(x, str(ord(x)) if gcd(x, B) == 1 else 'DNE') for x in range(1, B)]))
    A = 2


    # ordA = ord(A)

    def F(x):
        return A ** x % B


    collapsed_color = 11
    colors = np.asarray([1 if F(x) == collapsed_color else 0 for x in range(N)])

    colors = colors / np.linalg.norm(colors)
    print(colors)

    roots = nthRootsOfUnity(N)

    DFT_N = np.ones((N, N), dtype=np.complex128)
    for i in range(N):
        for j in range(N):
            DFT_N[i][j] = roots[-(i * j) % N]
    DFT_N /= np.sqrt(N)

    res = DFT_N @ colors

    # print(res)

    plt.plot(np.arange(N), np.sqrt(res.conj() * res), marker='o')
    plt.show()

    fmtcomplex = np.vectorize(lambda x: '{},{}'.format(x.real, x.imag))

    # np.savetxt('DFT1024.csv', fmtcomplex(DFT_N), delimiter=',', fmt='%s')
    # np.savetxt('res.csv', fmtcomplex(res), delimiter=',', fmt='%s')
