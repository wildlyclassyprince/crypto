'''
Blockchain

    A digital ledger in which transactions made are
    recorded chronologically and publicly.

    In more general terms, it's a public database
    where new data are stored in a container called
    a block and are added to an immutable chain (hence
    blockchain) with data added in the past. In the case
    of Bitcoin and other cryptocurrencies, these data
    are groups of transactions. But, the data can be of
    any type.

    We'll start by first defining what our blocks will
    look like. In blockchain, each block is stored with
    a timestamp and, optionally, an index. In our simple
    implementation, call it SnakeCoin, we're going to
    store both. And to help ensure integrity throughout
    the blockchain, each block will have a self-identifying
    hash. Like Bitcoin, each block's hash will be a
    cryptographic hash of the block's index, timestamp,
    data, and the hash of the previous block's hash. The
    data can be anything we want.
'''

# Imports
import hashlib as hasher
import datetime as date

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update((str(self.index) +
                   str(self.timestamp) +
                   str(self.data) +
                   str(self.previous_hash)).encode())
        return sha.hexdigest()

# Genesis block
def create_genesis_block():
    '''
    Manually construct a block with index zero and arbitrary
    previous hash.
    '''
    return Block(0, date.datetime.now(), 'Genesis Block', '0')

# Next block
def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = 'This is block ' + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)

# Create the blockchain and add the genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Number of blocks after the genesis block
num_of_blocks_to_add = 20

# Adding blocks to the chain
for i in range(0, num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add

    # Make the results public
    print('Block #{} has been added to the blockchain.'.format(block_to_add.index))
    print('Hash: {}\n'.format(block_to_add.hash))
