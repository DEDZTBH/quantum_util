N = 96


def ord(x):
    i = 1
    a = x
    while a % N != 0:
        a = (a + x) % N
        i += 1
    return i


if __name__ == '__main__':
    print(''.join(['{}: {}\n'.format(x, ord(x)) for x in range(1, N)]))
