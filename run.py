import threading
import os


NOF_THREATS = 1
NOF_SECONDS = 28800 # 1 hour
TARGET_FILE = "targets_transport"

class myThread (threading.Thread):
    def __init__(self, target):
      threading.Thread.__init__(self)
      self.target = target

    def run(self):
       os.system("sudo docker run -it ddosify/ddosify ddosify -t "+str(self.target)+" -d "+str(NOF_SECONDS))


def run(targets):
    workers = []
    for idx, target in enumerate(targets):
        for i in range(NOF_THREATS):
            thr = myThread(target)
            thr.start()
            workers.append(thr)
    return workers

def read_file(name):
    with open(name) as file:
        targets = [line.rstrip('\n') for line in file]
    return targets

def join(workers):
    for worker in workers:
        worker.join()
        
def main():
    targets = read_file(TARGET_FILE)
    workers = run(targets)
    join(workers)


if __name__ == "__main__":
    main()
