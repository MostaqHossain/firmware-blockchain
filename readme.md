# **Blockchain-Based Firmware Integrity Verification**

## **Overview**
This document details the steps taken to implement a blockchain-based firmware integrity verification system on the Sepolia Testnet using Solidity smart contracts and Infura.

---
## **Prerequisites**
- Installed **Python** (for computing firmware hash)
- **Infura** account to connect to Ethereum Testnet
- **MetaMask** wallet with Sepolia ETH
- **Remix IDE** for smart contract deployment

---
## **Step 1: Compute Firmware Hash**

### **Command Used:**
```python
import hashlib

file_path = "<YOUR_LOCAL_FOLDER_ADDRESS>\Arduino-COMBINED-dfu-usbserial-atmega16u2-Mega2560-Rev3.hex"

with open(file_path, "rb") as f:
    firmware_data = f.read()
    firmware_hash = hashlib.sha256(firmware_data).hexdigest()

print("Firmware Hash:", firmware_hash)
```

### **Output:**
```
Firmware Hash: a9c390a9b5ec.......
```

---
## **Step 2: Connect to Ethereum Testnet via Infura**

### **Python Code:**
```python
from web3 import Web3

infura_url = "https://sepolia.infura.io/v3/YOUR_INFURA_PROJECT_ID"
w3 = Web3(Web3.HTTPProvider(infura_url))

if w3.is_connected():
    print("Connected to Sepolia Testnet")
else:
    print("Connection Failed")
```

### **Output:**
```
Connected to Sepolia Testnet
```

---
## **Step 3: Deploy Smart Contract to Sepolia Testnet**
- Open **Remix IDE**
- Paste Solidity Smart Contract
- Compile and Deploy using **Injected Web3**

### **Issue Encountered:**
```
Gas estimation failed. Transaction execution will likely fail.
Error: toAddressIsNull
```

### **Resolution:**
- Ensured MetaMask is connected and account has Sepolia ETH.
- Redeployed contract successfully.

### **Transaction Confirmation:**
✅ **Deployed Smart Contract Successfully**

📌 **Etherscan Verification:**
![Transaction Confirmation](https://github.com/MostaqHossain/firmware-blockchain/blob/main/tx_hash.png)

---
## **Step 4: Store Firmware Hash on Blockchain**

### **Smart Contract Function Call:**
Function: `storeFirmwareHash(string deviceID, string hash)`

### **Inputs:**
```
DeviceID: "Device123"
Hash: "a9c390a9b5ec85.............."
```

### **Transaction Success Message:**
```
✅ Firmware hash stored successfully!
```

---
## **Step 5: Verify Firmware Hash**

### **Function Call:**
Function: `getFirmwareHash(string deviceID)`

### **Input:**
```
DeviceID: "Device123"
```

### **Output:**
```
Retrieved Hash: a9c390a9b5ec85dfdbacea42f2c.............
✅ Hash Matched!
```

---
## **Final Verification on Etherscan**
📌 **Etherscan Transaction Screenshot:**
![Etherscan Verification](https://github.com/MostaqHossain/firmware-blockchain/blob/main/tx_verification.png)

---
## **Next Steps & Enhancements**
- **Automate hash computation** with a monitoring script.
- **Integrate decentralized identity (DID)** for authentication.
- **Enhance security** by signing firmware hashes before storage.

---
### **Conclusion**
This implementation successfully stored and verified firmware integrity using blockchain. By leveraging Ethereum's Sepolia Testnet, we ensured firmware authenticity, mitigating risks of malicious modifications.
