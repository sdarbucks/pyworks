import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" % i)
print('Start')

threads = []  #[0, 1, 2, 3 4]
for i in range(5):
    t = threading.Thread(target = long_task)  # 실행할 작업 생성
    threads.append(t)

for t in threads:
    t.start()

print("End")