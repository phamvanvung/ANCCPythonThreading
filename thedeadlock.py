from concurrent.futures import ThreadPoolExecutor
import threading
import time


class Projector:
    def __init__(self):
        self.lock = threading.Lock()

    def acquire(self, name):
        print(f'{name} is acquiring the projector')
        self.lock.acquire()
        print(f'The projector is granted to {name}')

    def release(self, name):
        self.lock.release()
        print(f'{name} released the projector')


class Computer:
    def __init__(self):
        self.lock = threading.Lock()

    def acquire(self, name):
        print(f'{name} is acquiring the computer')
        self.lock.acquire()
        print(f'The computer is granted to {name}')

    def release(self, name):
        self.lock.release()
        print(f'{name} released the computer')


def present(name, resource1, resource2):
    resource1.acquire(name)
    time.sleep(2)
    resource2.acquire(name)
    time.sleep(2)
    print('Completed the presentation')
    resource1.release(name)
    resource2.release(name)


if __name__ == '__main__':
    projector = Projector()
    computer = Computer()
    transactions = [["A", "B"], [projector, computer], [computer, projector]]
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(present, *transactions)
