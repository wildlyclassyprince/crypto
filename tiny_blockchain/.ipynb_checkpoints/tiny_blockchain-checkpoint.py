# -*-coding: utf-8 -*-

'''
Blockchain

    A digital ledger in which transactions made are
    recorded chronologically and publicly.

    In more general terms, it's a public database
    where new data are stored in a container called
    a block and are added to an immutable chain (hence
    blockchain) with data added in the past. In the case
    of Bitcoin and other cryptocurrencies, these data
    are groups of transactions. However, the data can be
    of any type.

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
import server

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

'''
A Proof-of-Work algorithm is essentially an algorithm that generates an item that is difficult to create but easy to verify. The item is called the proof and, as it sounds, it is proof that a computer performed a certain amount of work.

In SnakeCoin, we'll create a somewhat simple Proof-of-Work algorithm. To create a new block, a miner's computer will have to increment a number. When that number is divisible by 9 (the number of letters in "SnakeCoin") and the proof number of the last block, a new SnakeCoin block will be mined and the miner will be given a brand new SnakeCoin.
'''

miner_address = 'q3nf394hjg-random-miner-address-34nf3i4nflkn3oi'

def proof_of_work(last_proof):
    # Create variables that will be used to find our proof of work
    incrementor - last_proof + 1
    # Keep incrementing the incrementor until it's equal to a number
    # divisible by 9 and the proof of work of the previous block
    # in the chain
    while not (incrementor % 9 == 0 and incrementor % last_proof == 0):
        incrementor += 1
    # Once that number is found, we can return it as a proof of our work
    return incrementor

@node.route('/mine', method=['GET'])
def mine():
    # Get the last proof of work
    last_block = blockchain[len(blockchain) - 1]
    last_proof = last_block.data['proof-of-work']
    # Find the proof of work for the current block being mined
    # Note: the program will hang here until a new proof of work is found
    proof = proof_of_work(last_proof)
    # Once we find a valid proof of work, we know we can mine a block so
    # we reward the miner by adding a transactionself.
    this_nodes_transactions.append(
        {'from' : 'network', 'to' : miner_address, 'amount' : 1}
    )
    # Now we can gather the data needed to create a new block
    new_block_data = {
        'proof-of-work' : proof,
        'transaction' : list(this_nodes_transactions)
    }
    new_block_index = last_block.index + 1
    new_block_timestamp = this_timestamp = date.datetime.now()
    last_block_hash = last_block.hash
    # Empty transaction list
    this_nodes_transactions[:] = []
    # Now create the new block!
    mined_block = Block(
        new_block_index,
        new_block_timestamp,
        new_block_data,
        last_block_hash
    )
    blockchain.append(mined_block)
    # Let the client know we mined a block
    return json.dumps({
        'index' : new_block_index,
        'timestamp' : str(new_block_timestamp),
        'data' : new_block_data,
        'hash' : last_block_hash
    }) + '\n'

'''
If blockchains are decentralized, how do we make sure that the same chain is on every node?

To do this, we make each node broadcast its version of the chain to the others and allow them to receive the chains of other nodes. After that, each node has to verify the other nodes' chains so that every node in the network can come to a consesus of what the resulting blockchain will look like. This is called a consesus algorithm.

Our consesus algorithm will be rather simple: if a node's chain is different from another's (i.e., there is a conflict), then the longest chain in the network stays and all shorter chains will be deleted. If there is no conflict between the chains in our network, then we carry on.
'''

@node.route('/blocks', methods=['GET'])
def get_blocks():
    chain_to_send = blockchain
    # Convert our blocks into dictionaries so we can send them as json objects later
    for block in chain_to_send:
        block_index = str(block.index)
        block_timestamp = str(block.timestamp)
        block_data = str(block.data)
        block_hash = block.hash
        block = {
            'index' : block_index,
            'timestamp' : block_timestamp,
            'data' : block_data,
            'hash' : block_hash
        }
        # Send our chain to whomever requested it
        chain_to_send = json.dumps(chain_to_send)
        return chain_to_send

def find_new_chains():
    # Get the blockchain of every other node
    other_chains = list()
    for node_url in peer_nodes:
        # Get their chains using a GET request
        block = requests.get(node_url + '/blocks').content
        # Convert the JSON object to a Python dictionary
        block = json.loads(block)
        # Add it to our list
        other_chains.append(block)
    return other_chains

def consesus():
    # Get the blocks from other nodes
    other_chains = find_new_chains()
    # If our chain isn't longest, then we store the longest chain
    longest_chain = blockchain
    for chain in other_chains:
        if len(longest_chain) < len(chain):
            longest_chain = chain
    # If the longest chain wasn't ours, then we set our chain to the longest
    blockchain = longest_chain
