import concurrent
from collections import Counter
from concurrent.futures.thread import ThreadPoolExecutor
import time
from urllib.request import urlopen


def task(v):
    url = "http://nginx/"
    with urlopen(url) as response:
        text = response.read().decode("utf-8")
        return text


def main():

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = []
        for i in range(100):
            time.sleep(0.05)
            future = executor.submit(task, i)
            futures.append(future)
        concurrent.futures.wait(futures)

    print(Counter(f.result() for f in futures))

if __name__ == "__main__":
    main()
