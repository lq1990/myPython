import time
import multiprocessing


def work():
    for i in range(10):
        print("working...")
        time.sleep(0.2)


def rest():
    for i in range(10):
        print("take a rest...")
        time.sleep(0.2)


# 默认，主进程会等待 子进程执行结束的。除非把某个子进程设置为daemon=True
if __name__ == '__main__':
    work_p = multiprocessing.Process(target=work)
    work_p.daemon = True # 设置守护主进程，主进程退出后 子进程直接销毁，不在执行子进程中的代码
    work_p.start()

    rest_p = multiprocessing.Process(target=rest)
    rest_p.start() # 由于rest_p 没有设置 守护主进程，因此即使当主进程结束后，rest_p依旧会执行

    # main
    time.sleep(1)
    print("=== main finishes! ===") # 当主进程结束后， 设置了daemon后 子进程会直接被销毁


