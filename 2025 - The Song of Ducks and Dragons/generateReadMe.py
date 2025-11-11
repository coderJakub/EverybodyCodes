import requests

content ="""# 🧩 Everybody Codes 2025 
This directory contains my solutions for the coding challenge event [Everybody Codes 2025: The Song of Ducks and Dragons](https://everybody.codes/event/2025/quests). Each day's challenge is organized into its own folder, with separate files for each part of the challenge. I used mostly `Python` to solve the challenges.

## 🚀 Running the solutions:
### Prerequisites
- Python 3.x installed on your machine.
- to be able to download the input files you have to create a file `cookie.txt` in this directory and put in your session cookie from everybody.codes 
    - you can find your session cookie by pressing `F12` in your browser, going to the `Application` tab, and looking for the `session` cookie under `Cookies` for the `everybody.codes` domain.

### Instructions    
```bash
python runDay.py <day>
```
- Replace `<day>` with the day number you want to run (e.g., `9`, `22`).
- you can also run a specific part of a day by providing a second argument:
    - if you want to run it with a personal testcase specified in `test.txt` you can add a third argument `t`
```bash
python runDay.py <day> <part> [t]
```

##  📅 Personal Progress

| Day | Part 1 | Part 2 | Part 3 |
|-----|:------:|:------:|:------:|
"""

def getCookie() -> dict:
    with open("cookie.txt") as f:
        cookie = f.read().strip()
        return {
            "Cookie": f"everybody-codes={cookie}"
        }

def getAnswer(day: int) -> iter:
    return requests.get(f"https://everybody.codes/api/event/2025/quest/{day}", headers=getCookie()).json()

def isFinished(data: str, part: int, day: int) -> str:
    return '❌' if data.get(f'answer{part}') is None else f'[✅](https://github.com/coderJakub/EverybodyCodes/tree/main/2025%20-%20The%20Song%20of%20Ducks%20and%20Dragons/Day{day:02}/p{part}.py)'


YELLOW = "\033[93m"
GREEN = "\033[92m"
RESET = "\033[0m"

seed = requests.get("https://everybody.codes/api/user/me", headers=getCookie()).json()['seed']

for day in range(1, 21):
    print(f"\r{YELLOW}Loading day {day}!{RESET}", end="", flush=True)
    data = getAnswer(day)
    content += f"| **{day}**  | {isFinished(data, 1, day)} | {isFinished(data, 2, day)} | {isFinished(data, 3, day)} |\n"
    
content += """
---
Legend: ✅ = Solved ❌ = Not solved

---

*@2025 Jakub Kliemann*"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
    
print(f"\r{GREEN}✅ Finished generating README!{RESET}     ")