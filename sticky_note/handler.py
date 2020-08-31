import logging
from threading import Lock
rem_item = []
lock = Lock()
def add_rem(item:str):
    global rem_item
    global lock
    lock.acquire(blocking=True)
    rem_item.append(item)
    lock.release()

def remove_rem(idx:int)->bool:
    global rem_item
    if len(rem_item) < idx:
        return False
    global lock
    lock.acquire(blocking=True)
    rem_item.pop(idx)
    lock.release
    return True

def list_rem()->str:
    global rem_item
    global lock
    lock.acquire(blocking=True)
    if  len(rem_item) == 0:
        lock.release()
        return "沒東西啦 臭ㄐㄐ"
    else:
        s = "剩下這些(OuO):\n"
        for i in range(len(rem_item)):
            s += f"{i}:{rem_item[i]}\n"
        lock.release()
        return s