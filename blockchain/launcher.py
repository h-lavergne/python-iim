from Blockchain import Blockchain
import sys

bc = Blockchain()
bc.createGenesis()
nbBlock = int(sys.argv[1])
for i in range(nbBlock):
    block = bc.newBlock("Transaction #" + str(i))
    block.mineBlock(bc.difficulty)
    bc.addTransaction(block)

