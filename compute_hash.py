import hashlib

def compute_firmware_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):  # Read file in chunks of 4KB
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()

# Use your actual firmware file path
firmware_path = r"C:\Drive_D\TnTech\Spring 2025\CSC 7970 CPS\term-paper-tw\Arduino-COMBINED-dfu-usbserial-atmega16u2-Mega2560-Rev3.hex"

firmware_hash = compute_firmware_hash(firmware_path)
print(f"Firmware Hash: {firmware_hash}")

 a9c390a9b5ec85dfdbacea42f2c30e2e30cab602a06a0276c6fc6e8f400c9971