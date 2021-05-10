# Delta Coin Cryptocurrency
### Keith Nolan & Cuan O'Conchuir.

# About this Project
This project is a Blockchain network and Cryptocurrency.
The application is a allows users:\
• Fully functioning Blockchain application\
• With a Cryptocurrency\
• Allows users to create wallets.\
• Incorporates Network Transactions using a Publish/Subscribe model.\
• Has a transaction pool for unconfirmed transactions.\
• Allows users to mine transactions and receive currency for their effort.\
• Display all transactions on a public ledger that users of the system can view.\

# How to run this Project

**IMPORTANT: All commands should be run in a BASH or Linux terminal**
**Install Packages**

`python -m venv blockchain-env` This is for creating the environment for running the application in a safe space

`pip3 install -r requirements.txt` Install necessary plugins/resources

**Install node**
https://nodejs.org/en/download/


## Run the application and API
**Virtual Enviornment is set up to create an isolated environment to do tests without having if effect the whole system**

- Activate the virtual environment `source blockchain-env/bin/activate`

- Start the application and api `python3 -m backend.app`

**Seed the backend with 10 example blocks and 2 transactions each**
- Activate the virtual environment `source blockchain-env/bin/activate`
- `export SEED_DATA=True && python3 -m backend.app`

**Run the frontend**
When inside the front end directory:
`npm run start`

(NOTE: If this will not run, you will need to do an `npm install` first)


### Demos

**Run block class. shows an example of what is included in a block, and the difficulty**
`python -m backend.blockchain.block`


**Run a demo of the average rate of blocks - displays difficulty and mining (not necessary for any functionality, is purely with testing/demoing in mind)**
`python -m backend.scripts.average_block_rate`


**Run Demo of hex_to_binary class**
`python -m backend.utils.hex_to_binary`


**Run a test script that outputs transaction data and a mined blocks data**
`python -m backend.scripts.test_app`


---

### _References_

[1] The wiki information of Sha-2; Includes the sha-256; https://en.wikipedia.org/wiki/SHA-2

[2] Widget to show sha-256 in action; https://emn178.github.io/online-tools/sha256.html

[3] A fast and loose insight into hashing in a blockchain; https://blockgeeks.com/guides/what-is-hashing/

[4] Article that gives a good guide on how to implement a hashing function; https://analytics4all.org/tag/hash/

[5] json.dumps(); Useful for stringifying; https://docs.python.org/3/library/json.html

[6] hashlib python docs; https://docs.python.org/2/library/hashlib.html

[7] int() function; for string to int conversion and binary; https://docs.python.org/3.4/library/functions.html?highlight=int#int

[8] https://cloud.google.com/pubsub/docs/overview

[9] https://flask.palletsprojects.com/en/1.1.x/

[10] Loose inspiration taken for peer data validation; https://livecodestream.dev/post/from-zero-to-blockchain-in-python-part-1/

[11] Useful info on synching peers; https://bigishdata.com/2017/10/27/build-your-own-blockchain-part-2-syncing-chains-from-different-nodes/

[12] https://docs.python.org/3/library/uuid.html

[13] https://pycryptodome.readthedocs.io/en/latest/src/public_key/ecc.html

[14] https://cryptography.io/en/latest/hazmat/backends/

[15] PEM encoding Docs; https://pycryptodome.readthedocs.io/en/latest/src/io/pem.html

[16] Hazmat SubjectPublicKey information and examples used as inspiration for our code; https://programtalk.com/python-examples/cryptography.hazmat.primitives.serialization.PublicFormat.SubjectPublicKeyInfo/

[17] ECDSA and DSS info; https://pycryptodome.readthedocs.io/en/latest/src/signature/dsa.html

[18] Serialization; hazmat docs; https://cryptography.io/en/latest/hazmat/primitives/asymmetric/serialization.html

[19] Property Python: https://www.programiz.com/python-programming/property

[20] Flask CORS: https://pypi.org/project/Flask-Cors/

[21] useEffect hook; React; https://reactjs.org/docs/hooks-effect.html

[22] useState for state management hooks; React; https://reactjs.org/docs/hooks-state.html

[23] StackOverflown; Advice on use of set and clearInterval; https://stackoverflow.com/questions/5978519/how-to-use-setinterval-and-clearinterval
