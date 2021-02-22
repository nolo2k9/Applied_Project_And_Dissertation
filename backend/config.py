"""
This file contains global values for this project
"""
# global variable for nano seconds
NANOS = 1
# global variable for Microseconds seconds
MICROS = 1000 * NANOS
# global variable for nano Milli-Seconds
MILLIS = 1000 * MICROS
# global variable for seconds
SECS = 1000 * MILLIS

# Declaring a mining rate for blocks
MINE_RATE = 4 * SECS

# Declaring a starting balance for each wallet
STARTING_BALANCE = 1000
#Reward in Deltacoin for mining a block
MINING_REWARD = 25

MINING_REWARD_INPUT = {'address': '*--official-mining-reward --*'}
