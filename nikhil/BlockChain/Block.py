from hashlib import *
from datetime import *

class Block:
    def __init__(self,timestamp='',data=""):
        self.data=data
        self.timestamp=timestamp
        self.prevHash=""
        self.hash=self.gethash()
    def gethash(self):
        mystr=str(self.data)+self.timestamp+self.prevHash
        return str(sha256(mystr.encode()).hexdigest())
class BlockChain:
    def __init__(self):
        self.chain = [Block(str(datetime.now()))]
    def getLastBlock(self):
        return self.chain[len(self.chain) - 1]
    def addBlock(self,block):
        block.prevHash = self.getLastBlock().hash
        block.hash = block.gethash()
        self.chain.append(block)
myobj = BlockChain()
myobj.addBlock(Block(str(datetime.now()),['Hello','world']))
myobj.addBlock(Block(str(datetime.now()),['New','World']))
for x in myobj.chain:
    print(x.prevHash)
    print(x.data)
    print(x.hash)