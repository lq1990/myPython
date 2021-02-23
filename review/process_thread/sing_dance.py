import time
import multiprocessing


def sing(num=3, songName='jay'):
    for i in range(num):
        print("singing..., song is", songName)
        time.sleep(0.5)


def dance(num=3, act='eee'):
    for i in range(num):
        print("dancing..., act is ", act)
        time.sleep(0.5)


if __name__ == '__main__':
    # one process
    begin_t = time.time()
    sing()
    dance()
    print("dt[s]: ", time.time() - begin_t)

    # multi process
    print("=======================")
    begin_t = time.time()
    sing_p = multiprocessing.Process(target=sing, args=(2, 'beautiful'))
    # 以元祖的方式传参，需要保证参数顺序 正确
    dance_p = multiprocessing.Process(target=dance, kwargs={'act': 'wawa'})
    # 以字典的方式传参，需要保证参数名即key 正确
    sing_p.start()
    dance_p.start()

    sing_p.join()
    dance_p.join()
    print("dt[s]: ", time.time() - begin_t)


