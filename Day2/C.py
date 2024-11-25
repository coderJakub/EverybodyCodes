from copy import deepcopy

with open('in.txt') as f:
    input = f.read()
runics = input.split('\n\n')[0].split(':')[1].split(',')
sentences = [list(line) for line in input.split('\n\n')[1].splitlines()]
marked = deepcopy(sentences)

runic_max_len = max([len(runic) for runic in runics])-1
stopper = len(sentences[0]) - runic_max_len

# Look horizontally
for i, sentence in enumerate(sentences):
    word =""
    for c in sentence:
        word += c
    for rune in runics:
        newWord = [word, word]
        if rune in word:
            newWord[0] = word.replace(rune, rune.lower())
        if rune in word[::-1]:
            newWord[1] = word[::-1].replace(rune, rune.lower())[::-1]
        for j, c in enumerate(marked[i]):
            if c.islower() or newWord[0][j].islower() or newWord[1][j].islower():
                marked[i][j] = word[j].lower()

# Look vertically
for j in range(len(sentences[0])):
    word = ""
    for i in range(len(sentences)):
        word += sentences[i][j]
    for rune in runics:
        newWord = [word, word]
        if rune in word:
            newWord[0] = word.replace(rune, rune.lower())
        if rune in word[::-1]:
            newWord[1] = word.replace(rune[::-1], rune.lower())
        for i, l in enumerate(marked):
            if marked[i][j].islower() or newWord[0][i].islower() or newWord[1][i].islower():
                marked[i][j] = word[i].lower()

# Look wrapped
for i, sentence in enumerate(sentences):
    word =""
    for c in sentence:
        word += c
    for rune in runics:
        wrapped_word = word[stopper:]+word[:stopper]
        newWord = [wrapped_word, wrapped_word]
        if rune in wrapped_word:
            newWord[0] = wrapped_word.replace(rune, rune.lower())
        if rune in wrapped_word[::-1]:
            newWord[1] = wrapped_word[::-1].replace(rune, rune.lower())[::-1]
        un_wrapped_n = [newWord[0][stopper:]+newWord[0][:stopper],newWord[1][stopper:]+newWord[1][:stopper]]
        
        for j, c in enumerate(marked[i]):
            if c.islower() or un_wrapped_n[0][j].islower() or un_wrapped_n[1][j].islower():
                marked[i][j] = word[j].lower()
                
count = 0                    
for word in marked:
    for c in word:
        if c.islower():
            count += 1
print(count)