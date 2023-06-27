"""
from multiprocessing import(
    Process,
    Lock, RLock, Semaphore, Queue, Condition, Event, Barrier,
    Pipe, Value, Array, Manager
)
"""


# parent_connがsendしたらchild_connが値を受け取る

import logging
import multiprocessing
import time

logging.basicConfig(
    level=logging.DEBUG, format='$(processName)s: %(message)s')


def f(conn):
    conn.send(['test'])
    time.sleep(5)
    conn.close()


if __name__ == '__main__':
    # 二つの変数にそれぞれプロセスを代入する　
    parent_conn, child_conn = multiprocessing.Pipe
    # プロセスがスタート
    p = multiprocessing.Process(target=f, args=(parent_conn, ))
    p.start()
    logging.debug(child_conn.recv())
