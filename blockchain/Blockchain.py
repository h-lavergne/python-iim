from Block import Block

class Blockchain(object):
    def __init__(self):
        self.blocks = []
        self.difficulty = 1

    def newBlock(self, data):
        lastBlock = self.blocks[-1]
        newId = lastBlock.id + 1
        lastBlockHash = lastBlock.blockHash
        return (
            Block(newId, lastBlockHash, data)
        )

    def addTransaction(self, block):
        self.blocks.append(block)
        print ("Block #" + str(block.id) + " ajouté à la blockchain (" + str(block.blockHash) + ")")
        print ("Nombre de tentatives :" + str(block.nonce))

    def createGenesis(self):
        genesis_block = Block(0, None, "69 la trik")
        genesis_block.mineBlock(self.difficulty)
        self.addTransaction(genesis_block)      