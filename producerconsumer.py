import time
from concurrent.futures import ThreadPoolExecutor
import threading


class ProducerConsumer:
    def __init__(self):
        self.value = 0
        self.p_lock = threading.Lock()
        self.c_lock = threading.Lock()
        self.c_lock.acquire()

    def produce(self):
        for i in range(5):
            self.p_lock.acquire()
            self.value = i + 1
            print(f'Produced {i + 1}')
            self.c_lock.release()
            time.sleep(2)

    def consume(self):
        for i in range(5):
            self.c_lock.acquire()
            print(f'Consumed {self.value}')
            self.p_lock.release()
            time.sleep(1)


if __name__ == '__main__':
    pc = ProducerConsumer()
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(pc.produce)
        executor.submit(pc.consume)
