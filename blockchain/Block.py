import time
from utils import getBlockchainZeros 
from hashlib import sha256
from utils import calculateHash

class Block(object):
    def __init__(self, id, previousHash, hashBody):
        self.id = id
        self.previousHash = previousHash
        self.hashBody = hashBody
        self.timestamp = time.time()
        self.nonce = 0
        self.blockHash = calculateHash(self)
    
    def __str__(self):
        return str(self.id) + str(self.previousHash) + str(self.hashBody) + str(self.timestamp) + str(self.nonce)
        
    def mineBlock(self, difficulty):
        zeros = str(getBlockchainZeros(difficulty))
        self.nonce = self.nonce + 1
        while self.blockHash[0:len(zeros)] != zeros:
            self.nonce += 1
            self.blockHash = calculateHash(self)
