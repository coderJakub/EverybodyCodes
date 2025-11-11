import sys
import os
import subprocess
import time
import requests
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def createFile(file: str, content: str = ""):
    if not os.path.exists(file) or os.path.getsize(file) == 0:
        open(file, "w").write(content)

def startProcess(file: str, inFile: str):
    process = subprocess.Popen(
        ["python", file, inFile],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    
    text = ''
    while process.poll() is None:
        text = '.' if len(text) > 2 else text+'.'
        sys.stdout.write(f"\r   {RED}Part {part}: {YELLOW}{text}{RESET}{END}")
        sys.stdout.flush()
        time.sleep(0.5)

    output, _ = process.communicate()
    sys.stdout.write(f"\r   {RED}Part {part}: {GREEN}{output.strip()}{RESET}{END}\n")
    sys.stdout.flush()

def getCookie() -> dict | None:
    if "cookie.txt" not in os.listdir():
        print(f"{RED}WARNING: cookie.txt file not found! Please create it with your session cookie from everybody.codes to get input data.{RESET}")
        return
    cookie = open("cookie.txt").read().strip()
    return {"Cookie": f"everybody-codes={cookie}"}
    
def decryptData(data: str, key: str) -> str:
    keyB = key.encode()
    iv = keyB[:16]
    
    cipher = Cipher(algorithms.AES(keyB), modes.CBC(iv))
    decryptor = cipher.decryptor()
    input_bytes = bytes.fromhex(data)
    decrypted_bytes = decryptor.update(input_bytes) + decryptor.finalize()
    pad_length = decrypted_bytes[-1]
    result = decrypted_bytes[:-pad_length].decode()
    return result

def getInputData(day: int, part: int) -> str:
    if (headers := getCookie()) is None:
        return ""
    try:
        seed = requests.get(f"https://everybody.codes/api/user/me", headers=headers).json()['seed']
        data = requests.get(f"https://everybody-codes.b-cdn.net/assets/2025/{day}/input/{seed}.json", headers=headers).json()
        key = requests.get(f"https://everybody.codes/api/event/2025/quest/{day}", headers=headers).json()
    except Exception as e:
        print(f"{RED}ERROR: Could not retrieve input data for day {day}, part {part}.")
        return ""
    
    if key.get(f'key{part}') is None:
        return ""
    return decryptData(data[f"{part}"], key[f'key{part}'])

TEMPLATE = """import sys

fileName = sys.argv[1]
with open(fileName) as f:
    content = f.read()
    
data = content
R = len(data)
#C = len(data[0])

res = 0
for el in data:
    continue


print(res)"""

YELLOW = "\x1b[33m"
GREEN = "\x1b[32m"
RESET = "\x1b[0m"
BLUE = "\x1b[34m"
RED = "\x1b[31m"
END = "\x1b[K"

cwd = os.getcwd()

if len(sys.argv) < 2:
    print(f"{RED}Please provide the day number as an argument.{RESET}")
    sys.exit(1)
    
day = int(sys.argv[1])
# Create day directory if it doesn't exist
dayDir = f'{cwd}/Day{day:02}'
os.makedirs(dayDir, exist_ok=True)

# Create a file for personal test cases
testFile = dayDir+"/test.txt"
createFile(testFile)

# Determine which parts to run
parts = [sys.argv[2]] if len(sys.argv)>2 else range(1,4)

print(f"{BLUE}Results for day {day}{RESET}")

for part in parts:
    file = f"{dayDir}/p{part}.py"
    inFile = dayDir+f"/in{part}.txt"
    
    # Create a python file for the part if it doesn't exist and create input file with input data
    createFile(file, TEMPLATE)
    createFile(inFile, getInputData(day, part))
    
    # If there is a third argument, run with personal test case (test.txt)
    if not len(sys.argv) > 3:
        startProcess(file, inFile)
    else:
        subprocess.run(["py", file, testFile])