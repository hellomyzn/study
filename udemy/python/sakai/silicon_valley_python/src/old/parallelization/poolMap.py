#　使うのが便利　短縮できる


import logging
import multiprocessing
import time

logging.basicConfig(
    level = logging.DEBUG, format='%(processName)s: %(message)s')

def worker1(i):
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')
    return i * 2


if __name__ == '__main__':
    # t1 = multiprocessing.Process(target=worker1, args=(i,))
    #プールの数でワーカの数を指定する
    with multiprocessing.Pool(3) as p:
        # やり方1
        # r = p.map(worker1, [100, 200])
        # logging.debug('executed')
        # logging.debug(r)


        # やり方2
        r = p.map_async(worker1, [100, 200])
        logging.debug('executed')
        logging.debug(r.get())


        # やり方3
        # imapはイテレータなので繰り返し処理で実行する
        r = p.imap(worker1, [100, 200])
        logging.debug('executed')

        for i in r:
            logging.debug(i)


        # p1 = p.apply_async(worker1, (100, ))
        # p2 = p.apply_async(worker1, (100, ))
        # logging.debug(p1.get())
        # logging.debug(p2.get()) # ワーカーのリターンをgetする
