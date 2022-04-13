import threading
from datetime import datetime

def date_time(n):
    ## Print date and time specified in the question format
    for i in range(3):
        print(f'Thread-{n}: {datetime.now().strftime("%A %B %d %X %Y")}')
    print(f'Exiting Thread-{n}')


t1 = threading.Thread(target=date_time, args=(1,))
t2 = threading.Thread(target=date_time, args=(2,))
t1.start()
t2.start()
t1.join()
t2.join()