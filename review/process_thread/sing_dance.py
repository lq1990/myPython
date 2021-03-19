import time
import multiprocessing
import os


def sing(num=3, songName='jay'):
    print("### sing pid: ", os.getpid())
    print("sing 父进程 ppid: ", os.getppid())
    for i in range(num):
        print("singing..., song is", songName)
        time.sleep(0.5)


def dance(num=3, act='eee'):
    print("### dance pid: ", os.getpid())
    print("dance ppid: ", os.getppid())
    for i in range(num):
        print("dancing..., act is ", act)
        time.sleep(0.5)


if __name__ == '__main__':
    print("main pid: ", os.getpid())
    # one process, this is main process 他也是子进程的父进程
    begin_t = time.time()
    sing() # pid is main.pid
    dance()
    print("dt[s]: ", time.time() - begin_t)

    # multi process, 这里会创建  子进程
    print("=======================")
    begin_t = time.time()
    sing_p = multiprocessing.Process(target=sing, args=(2, 'beautiful')) # sing.ppid is main.pid
    # 以元祖的方式传参，需要保证参数顺序 正确
    dance_p = multiprocessing.Process(target=dance, kwargs={'act': 'wawa'})
    # 以字典的方式传参，需要保证参数名即key 正确
    sing_p.start()
    dance_p.start()

    sing_p.join()
    dance_p.join()
    print("dt[s]: ", time.time() - begin_t)


