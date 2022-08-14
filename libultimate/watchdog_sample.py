import sys
import os
import time
import datetime
import logging
from watchdog.observers.polling import PollingObserver as Observer
from watchdog.events import LoggingEventHandler, RegexMatchingEventHandler
 
class MyFileWatchHandler(RegexMatchingEventHandler):
    def __init__(self):
        super().__init__()

    def on_created(self, event):
        pass

    def on_modified(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        with open(filepath, 'r') as f:
            data = f.read()
            print(data)
        print(f"{datetime.datetime.now()} {filename} changed")

    def on_deleted(self, event):
        pass

    def on_moved(self, event):
        pass

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = MyFileWatchHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()
