from multiprocessing import Process, cpu_count
import time
import os

from threading import Thread

# If we use Thread instead of Process, it will be a lot slower,
# because GIL does not allow multiple threads to run at the same time
# but processes can run at the same time.
class MuchCPU(Process):
    def run(self):
        print(os.getpid())
        for i in range(200_000_000):
            pass


if __name__ == "__main__":
    procs = [MuchCPU() for f in range(cpu_count())]
    t = time.time()
    for p in procs:
        p.start()
    for p in procs:
        p.join()
    print("work took {} seconds".format(time.time() - t))

