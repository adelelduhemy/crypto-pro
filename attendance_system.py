import time
from blockchain import Blockchain, Block
from security import generate_key_pair, sign_data, verify_signature

class AttendanceSystem:
    def __init__(self):
        self.blockchain = Blockchain()
        self.students = {}  # Maps student IDs to (private_key, public_key)

    def register_student(self, student_id):
        private_key, public_key = generate_key_pair()
        self.students[student_id] = (private_key, public_key)
        print(f"Student {student_id} registered with public key {public_key}")

    def record_attendance(self, student_id):
        if student_id not in self.students:
            print("Student not registered!")
            return

        private_key, public_key = self.students[student_id]
        timestamp = time.ctime()
        data = student_id + timestamp
        signature = sign_data(private_key, data)

        new_block = Block(
            index=len(self.blockchain.chain),
            student_id=student_id,
            timestamp=timestamp,
            signature=signature.hex(),
            previous_hash=self.blockchain.get_latest_block().hash
        )
        self.blockchain.add_block(new_block)
        print(f"Attendance recorded for {student_id}.")

    def verify_attendance(self):
        for block in self.blockchain.chain[1:]:
            student_id = block.student_id
            _, public_key = self.students[student_id]

            data = student_id + block.timestamp
            if not verify_signature(public_key, data, bytes.fromhex(block.signature)):
                print(f"Invalid signature in block {block.index}.")
                return False
        print("All attendance records are valid.")
        return True

    def display_blockchain(self):
        for block in self.blockchain.chain:
            print(f"Block {block.index}: {block.__dict__}")
