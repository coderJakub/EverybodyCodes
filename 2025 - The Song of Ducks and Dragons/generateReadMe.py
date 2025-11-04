import requests

content ="""# 🧩 Everybody Codes 2025 

[Everybody Codes](https://everybody.codes/event/2025/quests) ist ein jährliches Programmier-Event, das im Stil von Advent of Code oder anderen Coding-Challenges aufgebaut ist. Das Event dauert 20 Tage (typischerweise im November). Jeder Tag besteht aus 3 Teilen, die jeweils eine eigene Herausforderung darstellen.

##  📅 Fortschritt

| Tag | Teil 1 | Teil 2 | Teil 3 |
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
Legende: ✅ = Gelöst ❌ = Nicht geschafft

---

*@2025 Jakub Kliemann*
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
    
print(f"\r{GREEN}✅ Finished generating README!{RESET}     ")