# Applied_Project_And_Minor_Dissertation
#### Keith Nolan & Cuan O'Conner.


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






