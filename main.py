from input.recorder import Recorder
from multiprocessing import Queue

def main():
    data_queue = Queue()
    recorder = Recorder(data_queue)
    recorder.start()

    while True:
        if data_queue.empty():
            continue

        print(data_queue.get())

if __name__ == "__main__":
    main()