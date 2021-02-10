# Applied_Project_And_Minor_Dissertation
### Keith Nolan & Cuan O'Conchuir.

# About the Blockchain
A Blockchain is a decentralised and distributed ledger that stores data such as transactions. This data is publically shared accross all nodes on its network.

It is a collection of blocks and each block acts as a unit of storage. The blockchain stores the following fields.

Data field: The data field stores information about the block itself.

Hash: Each block is given a value that is a random set of characters. The hash is generated from a cryptographic hash function. Tis function generates a unique output for every unique input that it is given.
Included in the blocks hash is the data that it needs to store and when that block was created.

Last_hash: This contains the hash of the block that came before it and is included in every new block created. This creates links or a chain between blocks, as it references the block that came before it.

The ledger is decentralised which means that nobody has the core responsibilty of updating the ledger. This means that you are not placing all of your trust in one central authority like a bank, the blockchain is trustless.

# About the Cryptocurrency
Cryptocurrency leverages the blockchain to keep a public database of transactions. To stop attacks such as double spending a cryptocurrency uses cryptography to
protect the blockchain. Cryptography is used to create signatures. Unlike handwritten signatures, but have more security as it solves the problem of inpersonation. If a person wishes to record a transaction int the blockchain they have to stamp it with their digital signature. The signature is based on two cryptographic keys. One of these keys is public and the other is private.

## Wallets
Wallets store the public and private key for the owner. They track your balance in the currency. A wallet has a unqiue address which enables you to send and receive currency to and from your wallet. The private key enables wallets to generate signatures to make the transactions official.

## Mining
Miners enable transactions to be added to the blockchain. When a transaction is made within the network, it joins the transaction pool. After being admitted to the transaction pool, the transaction will be in an unconfirmed state. Miners take unconfirmed transactions and must complete a proof of work. This is a computational puzzle the miners must solve. These puzzles are difficult to solve with a low probability of solving them randomly. It is computationally expensive to solve this puzzle. When this is solved the miner will be granted the right to add this block to the chain. When the solution has been agreed upon the miner will receive currency which is added to their wallet.

## Proof of work

## Hashing 
The functional description of what hashing is, is basically taking in an input of any length, in this case our block information and then using that information and encrytping/hashing it into an output of a fixed length. The commonly used hashing function is the Sha-256 algorithm [1]. I've included in the references section a fun online widget that very simply explains what is meant by the opening sentence of this section [2].

Hash functions consist of a set of 5 properties:
1. That no matter how many times you input the same data, you will always get the same result back.
2. The function should in-theory be able to return the hash of an input quickly.
3. It should be infeasable to determine the data based on the ouputted hash.
4. Even the smallest change of the input, should always change the output.
5. Each input should have its own unique hash i.e. no two hashes should end up the same.

The way the hash is implemented into the blockchain is essentially much like the pointers to data in a linked list. Each block contains the data and a hash pointer that points to the previous block, creating a chain. The hash pointer contains the address of the previous block and the hash of the data inside the previous block. This is what makes blockchain so reliable in its security. If a hacker attempts to hack a block or change the data in one of the blocks this change in data means the hash of the data will also change. The blocks with hash pointers that are reliant on the previous hash can now no longer find that hash value because the data has changed.

### Python Version
It is important to use python 3.8 as some modules and their method calls are only present in 3.7 and beyond.

## Commands to run files/environments
**IMPORTANT: All commands should be run in a BASH or Linux terminal**
**Install Packages**

```python -m venv blockchain-env``` This is for creating the environment for running the application in a safe space

```pip3 install -r requirements.txt``` Install necessary plugins/resources

**Run the application and API**
**Virtual Enviornment set up to create an isolated environment to do tests without having if effect the whole system**
- Activate the virtual environment ```source blockchain-env/bin/activate```

- Start the application and api ```python3 -m backend.app```

### Demos
**Run block class. shows an example of what is included in a block, and the difficulty**
```python -m backend.blockchain.block```
**Run a demo of the average rate of blocks - displays difficulty and mining (not necessary for any functionality, is purely with testing/demoing in mind)**
```python -m backend.scripts.average_block_rate```
**Run Demo of hex_to_binary class**
```python -m backend.utils.hex_to_binary```


***
### *References*
[1] The wiki information of Sha-2; Includes the sha-256; https://en.wikipedia.org/wiki/SHA-2

[2] Widget to show sha-256 in action; https://emn178.github.io/online-tools/sha256.html

[3] A fast and loose insight into hashing in a blockchain; https://blockgeeks.com/guides/what-is-hashing/

[4] Article that gives a good guide on how to implement a hashing function; https://analytics4all.org/tag/hash/

[5] json.dumps(); Useful for stringifying; https://docs.python.org/3/library/json.html

[6] hashlib python docs; https://docs.python.org/2/library/hashlib.html

[7] int() function; for string to int conversion and binary; https://docs.python.org/3.4/library/functions.html?highlight=int#int

[8] https://cloud.google.com/pubsub/docs/overview

[9] https://flask.palletsprojects.com/en/1.1.x/
