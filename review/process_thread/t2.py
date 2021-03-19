import threading
import time


def task():
    time.sleep(0.5)
    print(threading.current_thread())


if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=task)
        t.start()


