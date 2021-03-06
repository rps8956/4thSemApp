import threading


# Buffer size
N = 10
# Buffer init
buf = [0] * N


full_count = threading.Semaphore(0)
empty_count = threading.Semaphore(N)


def produce():
    print("One item produced!")
    return 1


def producer():
    front = 0
    while True:
        x = produce()
        empty_count.acquire()
        buf[front] = x
        full_count.release()
        front = (front + 1) % N


def consume(y):
    print("One item consumed!")


def consumer():
    rear = 0
    while True:
        full_count.acquire()
        y = buf[rear]
        empty_count.release()
        consume(y)
        rear = (rear + 1) % N


producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()