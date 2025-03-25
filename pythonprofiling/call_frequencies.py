import cProfile


def find_sum():
    return sum(range(2000))


def main():
    for i in range(1000):
        find_sum()

cProfile.run('main()')