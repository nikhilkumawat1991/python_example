import threading
import time

status = "hello"

def get_databroker_status():
    print("inside databroker")
    while True:
        print("inside status")
        time.sleep(2)

if __name__ == '__main__':
    while True:
        if status != None:
            print("inside if ")
            databroker_thread = threading.Thread(target=get_databroker_status)
            databroker_thread.daemon = True
            databroker_thread.start()
            print("thread over")
            break