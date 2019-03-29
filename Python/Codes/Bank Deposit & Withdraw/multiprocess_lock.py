import time
import datetime
import multiprocessing

def deposit(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value + 1
        print('count of balance is {}'.format(balance.value))
        lock.release()

def withdraw(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value - 1
        print('count of balance is decrement {}'.format(balance.value))
        lock.release()


if __name__ == '__main__':

    tim = time.time()
    today=datetime.date.today()

    balance = multiprocessing.Value('i', 200)
    lock = multiprocessing.Lock()
    d = multiprocessing.Process(target=deposit,args=(balance,lock))
    w = multiprocessing.Process(target=withdraw,args=(balance,lock))
    d.start()
    w.start()
    d.join()
    w.join()
    print(balance.value)
    print("The full time is :" + str(time.time()-tim )+"seconds")
    print(today.month)