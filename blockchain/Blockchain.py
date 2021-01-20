from Block import Block

class Blockchain(object):
    def __init__(self):
        self.blocks = []
        self.difficulty = 2
        self.createGenesis()

    def newBlock(self, data):
        if len(self.blocks) == 0:
            self.createGenesis()
        lastBlock = self.blocks[-1]
        newId = lastBlock.id + 1
        lastBlockHash = lastBlock.blockHash
        return (
            Block(newId, lastBlockHash, data)
        )

    def addTransaction(self, block):
        self.blocks.append(block)
        return {
            "Block": "Block #" + str(block.id) + " ajoute a la blockchain (" + str(block.blockHash) + ")",
            "Nombre de tentatives" : block.nonce
        }
        # print ("Block #" + str(block.id) + " ajouté à la blockchain (" + str(block.blockHash) + ")")
        # print ("Nombre de tentatives :" + str(block.nonce))

    def createGenesis(self):
        genesis_block = Block(0, None, "69 la trik")
        genesis_block.mineBlock(self.difficulty)
        self.addTransaction(genesis_block)      