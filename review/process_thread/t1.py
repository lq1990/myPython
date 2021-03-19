import threading
import time

def sing(num, name):
    for i in range(num):
        print(name, "is singing...")
        time.sleep(0.1)


def dance(num, name):
    for i in range(num):
        print(name, "is dancing...")
        time.sleep(0.1)


if __name__ == '__main__':
    # 有两种方式设置daemon
    sing_p = threading.Thread(target=sing, args=(10,'anna'), daemon=True)
    dance_p = threading.Thread(target=dance, kwargs={"num":10, 'name':'beta'})
    # sing_p.setDaemon(True)
    dance_p.setDaemon(True)

    sing_p.start()
    dance_p.start()

    # main
    print('=== main over ===')

