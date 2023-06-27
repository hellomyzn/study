import logging
import threading
import time


logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker1(d, lock):
    logging.debug('start')
    with lock:
        i = d['x']
        time.sleep(5)
        d['x'] = i + 1
        logging.debug(d)
        with lock:
            d['x'] = i + 1
    logging.debug('end')


def worker2(d, lock):
    logging.debug('start')
    lock.acquire()
    i = d['x']
    d['x'] = i + 1
    logging.debug(d)
    lock.release()
    logging.debug('end')

if __name__ == '__main__':


    d = {'x': 0}
    lock2 = threading.Lock()
    lock = threading.RLock()

    t1 = threading.Thread(target=worker1, args=(d, lock))
    t2 = threading.Thread(target=worker2, args=(d, lock))
    t1.start()
    t2.start()


    # t = threading.Timer(3, worker1) # スレッドのタイマーを使って始める時間を遅らせる
    # t.start()


    # for _ in range(5):
    #     t = threading.Thread(target=worker1)
    #     t.setDaemon(True) #このt1の処理が長い時にまたないで処理を終了する
    #     t.start()
    #
    # print(threading.enumerate())
    # for thread in threading.enumerate():
    #     if thread is threading.currentThread():
    #         print(thread)
    #         continue
    #     thread.join()
    #
    #
    #
    # t2 = threading.Thread(target=worker2)
    # t1.start() #スレッドが走る
    # t2.start()
    #
    # print('started')
    #
    # t1.join()　# setDeamonしたやつでも処理が終わるまで待つ
    # t2.join()　#デーモン化してないやつでも明示的に書くのが暗黙の了解
