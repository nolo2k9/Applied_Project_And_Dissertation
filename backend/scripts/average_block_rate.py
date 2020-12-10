from backend.blockchain.blockchain import Blockchain
from backend.config import SECS

import time

"""
This script to test blocks being mined.
Will show the average time it takes to mine the blocks.

"""

blockchain = Blockchain() #instantiate

times = [] # track how long it takes

"""
Measure the time it takes using a start and end point,
calling add_block() in between.
"""
for i in range(1000):
    start_time = time.time_ns()
    blockchain.add_block(i)
    end_time = time.time_ns()

    time_to_mine = (end_time - start_time) / SECS #displayed in seconds
    times.append(time_to_mine) # add to our list of times

    # get the average time
    average_time = sum(times) / len(times)

    # show new difficulty
    print(f'New block difficulty:  {blockchain.chain[-1].difficulty}')
    print(f'Time to mine new block: {time_to_mine}s')
    print(f'Average time to add blocks: {average_time}s\n')
