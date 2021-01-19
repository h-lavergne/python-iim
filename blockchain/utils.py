from hashlib import sha256
from datetime import datetime
import sys

def calculateHash(block):
    bloc = str(block)
    return(sha256(bloc.encode('utf-8')).hexdigest())

def getBlockchainZeros(difficulty):
    return "0" * difficulty

def saveBlockIntoFile(hash):
    fr = open("hashStorage.txt", 'r')
    f = open("hashStorage.txt", 'a')
    if hash in fr.read():
        print("Element already saved")
        return hash
    else :
        f.write(hash)
        f.write('\n')
    f.close()
    fr.close()