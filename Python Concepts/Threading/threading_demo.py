from threading import Thread
from time import sleep


class Hello(Thread):
    def run(self):
        for _ in range(8):
            print("Hello",end="-")
            sleep(1)


class Hi(Thread):
    def run(self):
        for _ in range(8):
            print("Hi",end="-")
            sleep(1)


hello = Hello()
hi = Hi()
hello.start()
sleep(0.2)
hi.start()

hi.join()
hello.join()
print("bye")