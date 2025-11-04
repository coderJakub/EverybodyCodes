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

import sys
import os
import subprocess
import time

def createFile(file, content=""):
    if not os.path.isfile(file):
        with open(file, "w") as f:
            f.write(content)
            
def startProcess(file, inFile):
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

cwd = os.getcwd()

day = int(sys.argv[1])
dayDir = f'{cwd}/Day{day:02}'
os.makedirs(dayDir, exist_ok=True)

testFile = dayDir+"/test.txt"
createFile(testFile)
parts = [sys.argv[2]] if len(sys.argv)>2 else range(1,4)

print(f"{BLUE}Results for day {day}{RESET}")

for part in parts:
    file = f"{dayDir}/p{part}.py"
    inFile = dayDir+f"/in{part}.txt"
    createFile(file, TEMPLATE)
    createFile(inFile)
    
    if not len(sys.argv) > 3:
        startProcess(file, inFile)
    else:
        subprocess.run(["py", file, testFile])