# filename: install_libraries.py
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

libraries = ["requests", "reportlab"]

for lib in libraries:
    install(lib)

print("Libraries installed successfully.")