import contextlib
import time

import httpx
import threading

amount = 0


def run():
    for _ in range(69420):
        with contextlib.suppress(Exception):
            httpx.get(
                url="https://camo.githubusercontent.com/0839b3024a405a758ccfd537e0fba76bb825dae4580dc5247c4472521e3461fa/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d4e73686f757426636f6c6f723d626c756576696f6c6574267374796c653d666f722d7468652d6261646765"
            )
            global amount
            amount += 1
            print(amount)
            time.sleep(2)


for _ in range(100):
    threading.Thread(target=run).start()
    print("Thread started")
