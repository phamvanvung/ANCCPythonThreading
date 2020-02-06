import threading
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
    arguments = ["A", "B"]
    mt = threading.Thread(target=study, args=arguments)
    st = threading.Thread(target=listen_to_music, args=arguments)
    mt.start()
    st.start()
