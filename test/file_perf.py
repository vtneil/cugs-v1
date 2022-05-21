from time import perf_counter

line_size = 10 ** 5
run_size = 20


def createTestFile(filename, lineno=1000):
    with open(filename, mode='w') as f:
        for i in range(1, lineno + 1):
            f.write('This is a test line number {}'.format(i))
            f.write('\n')
    return


def blocks(files, size=2 ** 16):
    while True:
        b = files.read(size)
        if not b: break
        yield b


def getLine1(filename):
    maxl = 0
    with open(filename) as f:
        for _ in f:
            maxl += 1
        return maxl


def getLine2(filename):
    with open(filename) as f:
        return len(f.readlines())


def getLine3(filename):
    return sum(1 for _ in open(filename))


def getLine4(filename):
    with open(filename, mode="r") as f:
        return sum(bl.count("\n") for bl in blocks(f))


if __name__ == '__main__':
    func_list = [
        getLine1,
        getLine2,
        getLine3,
        getLine4,
    ]

    # createTestFile('test_read.txt', line_size)

    for f in func_list:
        dt = []
        r = 0
        for _ in range(run_size):
            proc_t = perf_counter()
            r = f('test_read.txt')
            dt.append(perf_counter() - proc_t)
        print('Process', f.__name__, 'ended in', 1000 * sum(dt), 'ms', 'with time per loop=',
              (1000 * sum(dt) / run_size), 'ms')
        print('Output is', r)
