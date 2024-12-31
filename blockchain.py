import hashlib
import json

class Block:
    def __init__(self, index, student_id, timestamp, signature, previous_hash):
        self.index = index
        self.student_id = student_id
        self.timestamp = timestamp
        self.signature = signature
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_content = (str(self.index) + self.student_id + self.timestamp + 
                         self.signature + self.previous_hash)
        return hashlib.sha256(block_content.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", "0", "0", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, block):
        if block.previous_hash == self.get_latest_block().hash:
            self.chain.append(block)
        else:
            raise ValueError("Invalid block: Incorrect previous hash.")

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.calculate_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
        return True
