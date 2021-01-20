from flask import Flask, request, jsonify
import requests
from Blockchain import Blockchain
from Block import Block
from utils import calculateHash
import redis

app =  Flask(__name__)

db = redis.Redis(host='redis', port=6379, decode_responses=True)


bc = Blockchain()

@app.route("/")
def test():
    return jsonify('Api working good'), 200


#we define the route /
@app.route('/chain', methods=['GET'])
def chain():
    blocks = []
    for b in bc.blocks:
        blocks.append({
            "block": b.__str__()
        })
    return jsonify(blocks)

@app.route('/block/new', methods=['POST'])
def new_block():
    req = request.json
    if len(bc.blocks) == 0:
        bc.createGenesis()
    lastBlock = bc.blocks[-1]
    newId = lastBlock.id + 1
    lastBlockHash = lastBlock.blockHash
    b = Block(newId, lastBlockHash, req['data'])
    
    return jsonify(bc.addTransaction(b))

@app.route('/launcher', methods=["POST"])
def launch():
    req = request.json
    response = []
    for i in range(req['nbBlock']):
        b = bc.newBlock("Transaction # " + str(i))
        b.mineBlock(bc.difficulty)
        response.append(bc.addTransaction(b))
    
    db.set('blocks', bc.blocks)
    return jsonify(db.get('blocks'))

@app.route('/reset', methods=["GET"])
def reset_blockchain():
    bc.blocks = []
    return jsonify('Blockchain reseted'), 200

@app.route('/update/block', methods=["POST"])
def update_block():
    req = request.json
    block_id = int(req['id'])
    new_val = req['new_val']

    try:
        block = bc.blocks[block_id - 1]
        if block != None:
            block.hashBody = new_val
            block.blockHash = calculateHash(block.__str__())
            return jsonify(block.__str__()), 200
    except:
        return jsonify("Block not found"), 404



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug = True)   