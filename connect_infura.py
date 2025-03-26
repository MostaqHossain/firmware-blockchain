from web3 import Web3

# Replace 'YOUR_INFURA_PROJECT_ID' with your actual Infura Project ID
infura_url = "https://sepolia.infura.io/v3/8f120f59cc49482c938f40058b4aaec9"

# Connect to Infura
web3 = Web3(Web3.HTTPProvider(infura_url))

# Check connection
if web3.is_connected():
    print("✅ Connected to Ethereum Testnet (Sepolia)!")
else:
    print("❌ Connection failed.")
