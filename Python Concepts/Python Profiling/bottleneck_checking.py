import cProfile
import time


def fast_function():
    time.sleep(0.1)


def slow_function():
    time.sleep(3)


def main():
    fast_function()
    slow_function()


cProfile.run('main()')
