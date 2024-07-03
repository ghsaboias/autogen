# filename: verify_pdf.py
import os

def read_pdf_start(filename, num_bytes=1000):
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            start_bytes = f.read(num_bytes)
        print(f"First {num_bytes} bytes of {filename}:")
        print(start_bytes)
        print(f"\nFile size: {os.path.getsize(filename)} bytes")
    else:
        print(f"File {filename} not found.")

read_pdf_start("top_10_cryptocurrencies.pdf")
print("Verification complete.")