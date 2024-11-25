with open('in.txt') as f:
    input = f.read()
runics = input.split('\n\n')[0].split(':')[1].split(',')
sentence = input.split('\n\n')[1].split(' ')
marked = sentence.copy()

for i,word in enumerate(sentence):
    for left in True, False:
        for runic in runics:
            if left and runic in word:
                r = runic.lower()
                w = word.replace(runic,r)
            elif not left and runic[::-1] in word:
                r = runic.lower()
                w = word[::-1].replace(runic,r)[::-1]
            else:
                continue
            nw = word
            for j,c in enumerate(marked[i]):
                if c.islower() or w[j].islower():
                    nw = nw[:j] + nw[j].lower() + nw[j+1:]
            marked[i] = nw

count = 0                    
for word in marked:
    for c in word:
        if c.islower():
            count += 1
print(count)