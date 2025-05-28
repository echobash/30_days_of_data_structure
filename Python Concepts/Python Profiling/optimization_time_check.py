import cProfile


def main():
    sum_final = 0
    for i in range(1000000):
        sum_final += i
    return sum_final


cProfile.run('main()')

def find_sum():
    return sum(range(1000000))

cProfile.run('find_sum()')