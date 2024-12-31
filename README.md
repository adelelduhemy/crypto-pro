


# Attendance System using Blockchain

## 📋 Project Description
The Attendance System is a Python-based blockchain application designed to securely record and verify student attendance. It utilizes cryptographic key pairs for identity verification and ensures data integrity by leveraging blockchain technology.

![Attendance System Diagram](https://via.placeholder.com/600x300?text=Attendance+System+Diagram)

---

## 🌟 Features
- **Blockchain Technology**: Securely records attendance data in an immutable ledger.
- **Digital Signatures**: Ensures the authenticity of attendance records using cryptographic signatures.
- **Student Registration**: Assigns unique public-private key pairs to each student for secure identity verification.
- **Attendance Verification**: Validates all attendance records in the blockchain to detect tampering or invalid entries.
- **Genesis Block**: Establishes a secure starting point for the blockchain.

---

## 🛠 Requirements
- Python 3.8 or higher
- Required Libraries:
  - `cryptography`

To install the necessary dependencies, run:
```bash
pip install cryptography
```

---

## 📦 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/attendance-system-blockchain.git
   cd attendance-system-blockchain
   ```
2. Install dependencies:
   ```bash
   pip install cryptography
   ```

---

## 🚀 Usage
1. Run the demo program to test the attendance system:
   ```bash
   python demo.py
   ```
2. Follow the prompts to:
   - Register students
   - Record their attendance
   - Verify the blockchain's integrity
   - Display the blockchain's contents

---

## 📁 File Structure
```
attendance-system-blockchain/
│
├── attendance_system.py  # Implements the main Attendance System
├── blockchain.py         # Defines the Blockchain and Block classes
├── demo.py               # Demonstrates the usage of the attendance system
├── security.py           # Handles cryptographic operations
└── README.md             # Project description and instructions
```

---

## ⚙ Configuration
- **Genesis Block**: The first block is created automatically when the blockchain is initialized.
- **Student Keys**: Each student is assigned a unique public-private key pair during registration.

---

## 📊 Attendance Workflow
1. **Register Student**: Each student is assigned a unique public-private key pair.
2. **Record Attendance**: The student’s ID and timestamp are signed with their private key, creating a secure attendance record.
3. **Verify Attendance**: The system validates each block in the blockchain using the corresponding public key.
4. **Display Blockchain**: Prints the details of all blocks in the chain for review.

---

## 📫 Support
For support, please open an issue in the repository or contact the project maintainers.

---

## 📄 License
This project is licensed under the MIT License. See the `LICENSE` file for details.

