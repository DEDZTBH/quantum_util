import numpy as np

HALF_AMPL = 2 ** (-1 / 2)

H_ones = np.asarray([
    [1, 1],
    [1, -1]
])


def H_to_n(n):
    N = 2 ** n
    Hn = H_ones
    for _ in range(n - 1):
        Hn = np.kron(Hn, H_ones)
    return N, Hn


# args is an array of arguments for convenience
def F(args):
    x, y, z = args
    if x + y + z >= 2:
        return 1
    else:
        return 0


if __name__ == '__main__':
    n = 3
    N, Hn = H_to_n(n)
    print('sqrt(1/{}) times'.format(N))
    for r in range(N):
        for c in range(N):
            num = Hn[r][c]
            if num > 0:
                print('+', end='')
            print('{} '.format(num), end='')
        print()
    print()

    argss = [np.asarray(list(bin(num)[2:].zfill(n))).astype(int) for num in range(N)]

    print('sqrt(1/{}) times'.format(N))
    ttlist = []
    for args in argss:
        print(args, end=' ')
        if F(args) == 0:
            ttlist.append(1)
            print('+1')
        else:
            ttlist.append(-1)
            print('-1')

    print()
    ttvec = np.asarray(ttlist).reshape((N, 1))
    # print(ttvec)
    result = Hn.dot(ttvec) / N
    for i, args in enumerate(argss):
        print('{} {}'.format(args, result[i]))
