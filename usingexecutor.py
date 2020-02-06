from concurrent.futures import ThreadPoolExecutor
import time
import random


def study(fname, lname):
    for i in range(10):
        print(f'{fname} {lname} is studying {i}...')
        time.sleep(random.random())


def listen_to_music(fname, lname):
    for i in range(10):
        print(f'{fname} {lname} is listening to music {i}...')
        time.sleep(random.random())


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(study, "A", "B")
        executor.submit(listen_to_music, "A", "B")
        # arguments = [["A", "C"], ["B", "D"]]
        # executor.map(study, *arguments)


